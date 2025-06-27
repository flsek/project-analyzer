# 🚀 Project Analyzer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Anthropic](https://img.shields.io/badge/Powered%20by-Anthropic%20Claude-orange.svg)](https://www.anthropic.com/)
[![GitHub stars](https://img.shields.io/github/stars/flsek/project-analyzer.svg)](https://github.com/flsek/project-analyzer/stargazers)

> 🤖 AI를 활용한 프로젝트 자동 분석 도구

프로젝트 구조를 스캔하고 AI가 상세한 기술 분석 리포트를 생성합니다.

## ✨ 주요 기능

- 📁 **자동 프로젝트 구조 분석** - 디렉토리와 파일을 지능적으로 스캔
- 🔍 **기술 스택 자동 감지** - 사용된 언어, 프레임워크, 도구 식별
- 🏗 **아키텍처 패턴 분석** - 설계 패턴과 구조적 특징 파악
- 📚 **맞춤형 학습 로드맵** - 난이도별 학습 순서 제안
- 💡 **개선 제안사항** - 코드 품질, 성능, 보안 관련 조언
- 📊 **마크다운 리포트** - 읽기 쉬운 형태로 결과 제공

## 📖 지원하는 프로젝트 타입

- ⚛️ **React/Next.js** - JavaScript/TypeScript 웹 앱
- 🍃 **Spring Boot** - Java 엔터프라이즈 애플리케이션
- 🐍 **Python** - Django, Flask, FastAPI 프로젝트
- 🔗 **Node.js** - Express, NestJS 백엔드
- 📱 **Mobile** - React Native, Flutter
- 🐳 **DevOps** - Docker, Kubernetes 설정
- 🎮 **게임** - Unity, Unreal Engine 프로젝트
- 📊 **데이터** - Jupyter Notebook, ML 프로젝트

## 🚀 빠른 시작

### 1. 설치

```bash
# 저장소 클론
git clone https://github.com/flsek/project-analyzer.git
cd project-analyzer

# 의존성 설치
pip install -r requirements.txt
```

### 2. API 키 발급

1. Anthropic Console 접속
2. 회원가입 또는 로그인
3. API Keys 메뉴 클릭
4. Create Key 버튼 클릭
5. 생성된 키 복사 (sk-ant-api03-xxxxx 형태)

### 3. API 키 발급

```bash
python main.py /path/to/your/project --api-key your_anthropic_api_key
```

## 📚 상세 사용 방법

### 🔧 기본 명령어

```bash
# 현재 디렉토리 분석
python main.py . --api-key sk-ant-api03-xxxxx

# 특정 프로젝트 분석
python main.py /Users/username/my-project --api-key sk-ant-api03-xxxxx

# Windows 경로 예시
python main.py C:\dev\my-project --api-key sk-ant-api03-xxxxx
```

## 📄 결과를 파일로 저장

```bash
# 마크다운 파일로 저장
python main.py ./my-react-app --api-key sk-ant-api03-xxxxx --output report.md

# 프로젝트 이름으로 파일명 자동 생성
python main.py ./agent-codegen --api-key sk-ant-api03-xxxxx --output agent_codegen_analysis.md
```

## 🔍 상세 진행 과정 확인

```bash
# 분석 과정을 실시간으로 확인
python main.py ./my-project --api-key sk-ant-api03-xxxxx --verbose

# 결과 예시:
# 🔍 프로젝트 분석을 시작합니다...
# 📁 분석 대상: ./my-project
# 📊 프로젝트 파일을 스캔하는 중...
#    ✅ 총 156개 파일, 23개 디렉토리 발견
#    📄 12개 주요 파일 분석 대상 선정
# 🤖 Anthropic API로 프로젝트를 분석하는 중...
# ✅ 분석 완료!
```

🌍 환경 변수로 API 키 설정 (선택사항)
매번 API 키를 입력하기 번거롭다면:
macOS/Linux:
bash# ~/.zshrc 또는 ~/.bashrc에 추가
export ANTHROPIC_API_KEY="sk-ant-api03-xxxxx"

# 터미널 재시작 후

python main.py ./my-project
Windows:
cmd# 환경 변수 설정
setx ANTHROPIC_API_KEY "sk-ant-api03-xxxxx"

# 새 명령프롬프트에서

python main.py ./my-project
💡 실사용 예시
예시 1: React 프로젝트 분석
bashpython main.py ./my-react-app --api-key sk-ant-api03-xxxxx --output react_analysis.md --verbose
결과: React, TypeScript, Webpack 등 기술 스택 자동 감지, 컴포넌트 구조 분석, 성능 최적화 제안
예시 2: Spring Boot 프로젝트 분석
bashpython main.py ./spring-backend --api-key sk-ant-api03-xxxxx --output spring_report.md
결과: Java, Spring Boot, JPA 등 파악, 레이어 아키텍처 분석, 보안 개선 제안
예시 3: Python ML 프로젝트 분석
bashpython main.py ./ml-model --api-key sk-ant-api03-xxxxx --output ml_analysis.md
결과: Pandas, NumPy, TensorFlow 등 감지, 데이터 파이프라인 분석, ML 모델 최적화 제안
📊 분석 결과 예시
생성되는 리포트에는 다음 내용이 포함됩니다:
markdown# 🚀 프로젝트 분석 리포트

## 📋 프로젝트 개요

- 프로젝트 목적과 주요 기능
- 대상 사용자와 사용 사례

## 🛠 기술 스택

- 프로그래밍 언어: React, TypeScript
- 프레임워크/라이브러리: Next.js, Tailwind CSS
- 데이터베이스: PostgreSQL
- 배포/인프라: Vercel, Docker

## 🏗 아키텍처 분석

- 컴포넌트 기반 아키텍처
- 상태 관리: Redux Toolkit
- API 통신: Axios + React Query

## ⚙️ 설치 및 실행 방법

1. 의존성 설치: npm install
2. 개발 서버 실행: npm run dev
3. 빌드: npm run build

## 📚 학습 로드맵

### 🔰 초급 (필수 기초)

- JavaScript ES6+ 문법
- React 기본 개념 (컴포넌트, JSX, Props, State)

### 🔵 중급 (핵심 기술)

- TypeScript 기본 문법
- Next.js 라우팅과 SSR/SSG
- CSS-in-JS와 Tailwind

### 🔴 고급 (심화 기술)

- 성능 최적화 (Code Splitting, Lazy Loading)
- 고급 상태 관리 패턴
- 테스팅 (Jest, React Testing Library)

## 💡 개선 제안

- 테스트 코드 커버리지 향상
- 번들 크기 최적화
- 접근성(a11y) 개선
  ⚙️ 고급 사용법
  🎯 특정 파일 타입만 분석
  bash# config.py 파일을 수정하여 분석 대상 커스터마이징 가능

# HIGH_PRIORITY_FILES, MEDIUM_PRIORITY_FILES 리스트 수정

🔧 분석 결과 커스터마이징
bash# project_analyzer.py의 \_build_analysis_prompt 메서드 수정

# 원하는 분석 항목 추가/제거 가능

🚨 주의사항
API 사용량 관리

비용 발생: Anthropic API 사용량에 따라 비용이 청구됩니다
토큰 제한: 대용량 프로젝트는 분석 시간이 오래 걸릴 수 있습니다
API 키 보안: API 키를 GitHub에 커밋하지 마세요

지원하지 않는 파일

바이너리 파일 (이미지, 동영상 등)
1MB 이상 대용량 파일
.git, node_modules 등 자동 제외

🔧 문제 해결
❌ "API 키 오류"
bash# API 키가 올바른지 확인

# Anthropic Console에서 크레딧 잔액 확인

❌ "파일 접근 권한 오류"
bash# 프로젝트 폴더 읽기 권한 확인
chmod -R 755 /path/to/project
❌ "모듈을 찾을 수 없음"
bash# 의존성 재설치
pip install -r requirements.txt --force-reinstall
❌ "분석 결과가 너무 짧음"
bash# 주요 파일이 없는 경우 발생

# README.md, package.json 등 설정 파일 확인

🤝 기여하기
이 프로젝트를 개선하고 싶으시다면:

Fork 버튼 클릭
기능 브랜치 생성: git checkout -b feature/amazing-feature
변경사항 커밋: git commit -m 'Add amazing feature'
브랜치에 Push: git push origin feature/amazing-feature
Pull Request 생성

기여 아이디어

새로운 프로그래밍 언어 지원 추가
분석 정확도 개선
새로운 출력 형식 지원 (JSON, HTML 등)
성능 최적화
다국어 지원

📄 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다.
MIT License

Copyright (c) 2025 flsek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
🙏 감사 인사

Anthropic: 강력한 Claude AI 모델 제공
Python 커뮤니티: 훌륭한 라이브러리 생태계
모든 기여자들: 프로젝트 개선에 참여해주신 분들

⭐ 이 프로젝트가 도움이 되셨다면 Star를 눌러주세요!
Made with ❤️ by flsek
