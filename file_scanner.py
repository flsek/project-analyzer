"""
프로젝트 파일 스캔 및 분석 유틸리티
"""

import os
import fnmatch
from pathlib import Path
from typing import Dict, List, Tuple
from config import IGNORE_PATTERNS, HIGH_PRIORITY_FILES, MEDIUM_PRIORITY_FILES, MAX_FILE_SIZE, MAX_FILES_TO_ANALYZE

class FileScanner:
    def __init__(self):
        self.ignore_patterns = IGNORE_PATTERNS
        self.high_priority = HIGH_PRIORITY_FILES
        self.medium_priority = MEDIUM_PRIORITY_FILES
    
    def scan_project(self, root_path: str) -> Dict:
        """프로젝트 전체를 스캔하여 구조화된 정보 반환"""
        if not os.path.exists(root_path):
            raise FileNotFoundError(f"경로를 찾을 수 없습니다: {root_path}")
        
        project_data = {
            'root_path': root_path,
            'structure': self._get_directory_tree(root_path),
            'key_files': self._extract_key_files(root_path),
            'file_stats': self._get_file_statistics(root_path)
        }
        
        return project_data
    
    def _should_ignore(self, path: str) -> bool:
        """파일/폴더를 무시해야 하는지 확인"""
        name = os.path.basename(path)
        
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(name, pattern):
                return True
        
        return False
    
    def _get_directory_tree(self, root_path: str, max_depth: int = 3) -> str:
        """디렉토리 구조를 트리 형태로 반환"""
        tree_lines = []
        
        def add_to_tree(current_path: str, prefix: str = "", depth: int = 0):
            if depth > max_depth:
                return
            
            items = []
            try:
                for item in os.listdir(current_path):
                    if not self._should_ignore(os.path.join(current_path, item)):
                        items.append(item)
            except PermissionError:
                return
            
            items.sort()
            
            for i, item in enumerate(items):
                item_path = os.path.join(current_path, item)
                is_last = (i == len(items) - 1)
                
                current_prefix = "└── " if is_last else "├── "
                tree_lines.append(f"{prefix}{current_prefix}{item}")
                
                if os.path.isdir(item_path):
                    extension = "    " if is_last else "│   "
                    add_to_tree(item_path, prefix + extension, depth + 1)
        
        tree_lines.append(os.path.basename(root_path) + "/")
        add_to_tree(root_path)
        
        return "\n".join(tree_lines)
    
    def _extract_key_files(self, root_path: str) -> Dict[str, str]:
        """중요한 파일들의 내용을 추출"""
        key_files = {}
        files_found = []
        
        # 모든 파일을 수집하고 우선순위별로 정렬
        for root, dirs, files in os.walk(root_path):
            dirs[:] = [d for d in dirs if not self._should_ignore(os.path.join(root, d))]
            
            for file in files:
                file_path = os.path.join(root, file)
                if not self._should_ignore(file_path):
                    files_found.append((file, file_path, self._get_file_priority(file)))
        
        # 우선순위별로 정렬 (높은 우선순위부터)
        files_found.sort(key=lambda x: x[2], reverse=True)
        
        # 상위 파일들의 내용 읽기
        for file_name, file_path, priority in files_found[:MAX_FILES_TO_ANALYZE]:
            try:
                file_size = os.path.getsize(file_path)
                if file_size > MAX_FILE_SIZE:
                    continue
                
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    relative_path = os.path.relpath(file_path, root_path)
                    key_files[relative_path] = content
                    
            except Exception as e:
                print(f"파일 읽기 실패: {file_path}, 오류: {e}")
        
        return key_files
    
    def _get_file_priority(self, filename: str) -> int:
        """파일의 우선순위를 반환 (높을수록 중요)"""
        if filename in self.high_priority:
            return 3
        elif filename in self.medium_priority:
            return 2
        elif self._is_source_file(filename):
            return 1
        else:
            return 0
    
    def _is_source_file(self, filename: str) -> bool:
        """소스 코드 파일인지 확인"""
        source_extensions = [
            '.py', '.js', '.jsx', '.ts', '.tsx',
            '.java', '.cpp', '.c', '.h', '.hpp',
            '.go', '.rs', '.php', '.rb', '.swift',
            '.kt', '.scala', '.cs', '.html', '.css',
            '.vue', '.svelte', '.dart'
        ]
        
        return any(filename.endswith(ext) for ext in source_extensions)
    
    def _get_file_statistics(self, root_path: str) -> Dict:
        """파일 통계 정보 수집"""
        stats = {
            'total_files': 0,
            'total_dirs': 0,
            'file_types': {},
            'total_size': 0
        }
        
        for root, dirs, files in os.walk(root_path):
            dirs[:] = [d for d in dirs if not self._should_ignore(os.path.join(root, d))]
            stats['total_dirs'] += len(dirs)
            
            for file in files:
                file_path = os.path.join(root, file)
                if not self._should_ignore(file_path):
                    stats['total_files'] += 1
                    
                    # 파일 확장자별 통계
                    ext = os.path.splitext(file)[1].lower()
                    if not ext:
                        ext = 'no_extension'
                    stats['file_types'][ext] = stats['file_types'].get(ext, 0) + 1
                    
                    # 파일 크기
                    try:
                        stats['total_size'] += os.path.getsize(file_path)
                    except OSError:
                        pass
        
        return stats