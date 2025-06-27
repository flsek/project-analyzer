"""
Anthropic API를 사용한 프로젝트 분석 클래스
"""

import anthropic
from typing import Dict
from config import API_MAX_TOKENS, API_MODEL

class ProjectAnalyzer:
    def __init__(self, api_key: str):
        """
        ProjectAnalyzer 초기화
        
        Args:
            api_key: Anthropic API 키
        """
        self.client = anthropic.Anthropic(api_key=api_key)
    
    def analyze_project(self, project_data: Dict) -> str:
        """
        프로젝트 데이터를 분석하여 상세한 리포트 생성
        
        Args:
            project_data: 스캔된 프로젝트 데이터
            
        Returns:
            분석 결과 마크다운 텍스트
        """
        prompt = self._build_analysis_prompt(project_data)
        
        try:
            response = self.client.messages.create(
                model=API_MODEL,
                max_tokens=API_MAX_TOKENS,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            return response.content[0].text
            
        except Exception as e:
            return f"❌ API 호출 실패: {str(e)}\n\n기본 분석 결과를 제공합니다.\n\n{self._generate_basic_analysis(project_data)}"
    
    def _build_analysis_prompt(self, project_data: Dict) -> str:
        """분석을 위한 프롬프트 생성"""
        
        # 파일 내용을 포맷팅
        files_content = self._format_files_content(project_data['key_files'])
        
        # 파일 통계 포맷팅
        stats = project_data['file_stats']
        file_types_str = ", ".join([f"{ext}({count})" for ext, count in list(stats['file_types'].items())[:10]])
        
        prompt = f"""다음 프로젝트를 상세히 분석하고 개발자를 위한 완전한 가이드를 작성해주세요.

## 📊 프로젝트 기본 정보
- 총 파일 수: {stats['total_files']}개
- 총 디렉토리 수: {stats['total_dirs']}개  
- 주요 파일 타입: {file_types_str}
- 프로젝트 크기: {stats['total_size'] / 1024 / 1024:.2f}MB

## 📁 프로젝트 구조
## 📄 주요 파일 내용
{files_content}

---

위 정보를 바탕으로 아래 형식에 맞춰 **한국어로** 상세한 분석 리포트를 작성해주세요:

# 🚀 프로젝트 분석 리포트

## 📋 프로젝트 개요
- 이 프로젝트가 무엇을 하는지 명확히 설명
- 주요 기능과 목적
- 대상 사용자 또는 사용 사례

## 🛠 기술 스택
- **프로그래밍 언어**: 
- **프레임워크/라이브러리**: 
- **데이터베이스**: 
- **배포/인프라**: 
- **개발 도구**: 

## 🏗 아키텍처 분석
- 전체적인 시스템 구조
- 주요 컴포넌트와 그들의 역할
- 데이터 흐름과 처리 방식
- 디자인 패턴 또는 아키텍처 패턴

## ⚙️ 설치 및 실행 방법
1. **필수 요구사항**
2. **설치 단계**  
3. **실행 방법**
4. **환경 설정**

## 📚 학습 로드맵
이 프로젝트를 완전히 이해하고 기여하기 위해 학습해야 할 기술들을 **난이도 순**으로 나열:

### 🔰 초급 (필수 기초)
- 

### 🔵 중급 (핵심 기술)
- 

### 🔴 고급 (심화 기술)  
- 

## 💡 개선 제안
- 코드 품질 향상 방안
- 성능 최적화 포인트
- 보안 고려사항
- 확장성 개선 방안

각 섹션을 가능한 구체적이고 실용적으로 작성해주세요."""

        return prompt
    
    def _format_files_content(self, key_files: Dict[str, str]) -> str:
        """파일 내용을 포맷팅"""
        if not key_files:
            return "주요 파일을 찾을 수 없습니다."
        
        formatted_content = []
        
        for file_path, content in key_files.items():
            # 내용이 너무 길면 앞부분만 표시
            display_content = content[:2000] + "..." if len(content) > 2000 else content
            
            formatted_content.append(f"""
### {file_path}
""")
        
        return "\n".join(formatted_content)
    
    def _generate_basic_analysis(self, project_data: Dict) -> str:
        """API 호출 실패시 기본 분석 결과 생성"""
        stats = project_data['file_stats']
        
        # 주요 기술 추측
        tech_stack = []
        file_types = stats['file_types']
        
        if '.py' in file_types:
            tech_stack.append("Python")
        if '.js' in file_types or '.jsx' in file_types:
            tech_stack.append("JavaScript/React")
        if '.ts' in file_types or '.tsx' in file_types:
            tech_stack.append("TypeScript")
        if '.java' in file_types:
            tech_stack.append("Java")
        if '.go' in file_types:
            tech_stack.append("Go")
        
        basic_analysis = f"""
# 🚀 기본 프로젝트 분석

## 📋 프로젝트 개요
- 총 파일 수: {stats['total_files']}개
- 총 디렉토리 수: {stats['total_dirs']}개
- 프로젝트 크기: {stats['total_size'] / 1024 / 1024:.2f}MB

## 🛠 감지된 기술 스택
{', '.join(tech_stack) if tech_stack else '자동 감지 실패'}

## 📁 프로젝트 구조
## 📄 주요 파일
{', '.join(list(project_data['key_files'].keys())[:10])}

⚠️ 상세한 분석을 위해서는 Anthropic API 키가 필요합니다.
"""
        return basic_analysis