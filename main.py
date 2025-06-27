#!/usr/bin/env python3
"""
프로젝트 분석 도구 - 메인 실행 파일
Anthropic API를 사용하여 프로젝트를 분석하고 상세한 리포트를 생성합니다.
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

from file_scanner import FileScanner
from project_analyzer import ProjectAnalyzer

def main():
    parser = argparse.ArgumentParser(
        description='🚀 프로젝트 분석 도구 - Anthropic API로 프로젝트를 분석합니다.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python main.py /path/to/project --api-key your_api_key
  python main.py . --api-key your_api_key --output report.md
  python main.py ~/my-project --api-key your_api_key --verbose
        """
    )
    
    parser.add_argument(
        'project_path',
        help='분석할 프로젝트의 경로'
    )
    
    parser.add_argument(
        '--api-key',
        required=True,
        help='Anthropic API 키 (필수)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='결과를 저장할 파일 경로 (기본값: 콘솔 출력)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='상세한 진행 과정 출력'
    )
    
    args = parser.parse_args()
    
    # 경로 검증
    project_path = os.path.abspath(args.project_path)
    if not os.path.exists(project_path):
        print(f"❌ 오류: 경로를 찾을 수 없습니다: {project_path}")
        sys.exit(1)
    
    if not os.path.isdir(project_path):
        print(f"❌ 오류: 디렉토리가 아닙니다: {project_path}")
        sys.exit(1)
    
    try:
        print("🔍 프로젝트 분석을 시작합니다...")
        print(f"📁 분석 대상: {project_path}")
        
        # 1. 파일 스캔
        if args.verbose:
            print("📊 프로젝트 파일을 스캔하는 중...")
        
        scanner = FileScanner()
        project_data = scanner.scan_project(project_path)
        
        if args.verbose:
            stats = project_data['file_stats']
            print(f"   ✅ 총 {stats['total_files']}개 파일, {stats['total_dirs']}개 디렉토리 발견")
            print(f"   📄 {len(project_data['key_files'])}개 주요 파일 분석 대상 선정")
        
        # 2. AI 분석
        if args.verbose:
            print("🤖 Anthropic API로 프로젝트를 분석하는 중...")
        
        analyzer = ProjectAnalyzer(args.api_key)
        analysis_result = analyzer.analyze_project(project_data)
        
        # 3. 결과 출력/저장
        if args.output:
            output_path = os.path.abspath(args.output)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"<!-- 생성일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -->\n")
                f.write(f"<!-- 분석 대상: {project_path} -->\n\n")
                f.write(analysis_result)
            
            print(f"✅ 분석 완료! 결과가 저장되었습니다: {output_path}")
            
        else:
            print("\n" + "="*80)
            print("📋 프로젝트 분석 결과")
            print("="*80)
            print(analysis_result)
            print("="*80)
        
        if args.verbose:
            print(f"🎉 분석이 성공적으로 완료되었습니다!")
            
    except KeyboardInterrupt:
        print("\n⚠️ 사용자에 의해 중단되었습니다.")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ 오류 발생: {str(e)}")
        if args.verbose:
            import traceback
            print("상세 오류 정보:")
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()