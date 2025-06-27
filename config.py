"""
프로젝트 분석 도구 설정 파일
"""

# 파일 크기 제한 (1MB)
MAX_FILE_SIZE = 1024 * 1024

# 무시할 디렉토리/파일 패턴
IGNORE_PATTERNS = [
    '.git', '.gitignore',
    'node_modules', 'package-lock.json',
    '__pycache__', '*.pyc', '.pytest_cache',
    '.venv', 'venv', 'env',
    'dist', 'build', 'target',
    '.DS_Store', 'Thumbs.db',
    '*.log', '*.tmp'
]

# 우선순위가 높은 파일들
HIGH_PRIORITY_FILES = [
    'README.md', 'README.rst', 'README.txt',
    'package.json', 'package-lock.json',
    'requirements.txt', 'pyproject.toml', 'setup.py',
    'Dockerfile', 'docker-compose.yml', 'docker-compose.yaml',
    'pom.xml', 'build.gradle', 'build.gradle.kts',
    'Makefile', 'CMakeLists.txt',
    '.env.example', 'config.yml', 'config.yaml'
]

# 중간 우선순위 파일들
MEDIUM_PRIORITY_FILES = [
    'main.py', '__main__.py', 'app.py',
    'index.js', 'main.js', 'app.js',
    'App.jsx', 'index.html',
    'main.go', 'main.rs', 'main.cpp'
]

# 분석할 최대 파일 개수
MAX_FILES_TO_ANALYZE = 20

# API 관련 설정
API_MAX_TOKENS = 4000
API_MODEL = "claude-sonnet-4-20250514"