# 소스 폴더내 세부폴더 데이터를 소스 폴더로 옮기는 코드
# 데이터 중 컬렉터 데이터 폴더 별로 파일이 정리 된 경우가 있어서 제작
import os
import shutil

source_folder = r""  # 소스 폴더 경로

# 폴더 경로를 모아주는 리스트
file_paths = []

# 세부폴더 내 탐색
for root, dirs, files in os.walk(source_folder):
    for file in files:
        file_path = os.path.join(root, file)
        file_paths.append(file_path)  # 폴더 경로를 리스트에 추가

# 리스트 내 파일들을 소스폴더로 이동
for file_path in file_paths:
    shutil.move(file_path, source_folder)

print("Files moved successfully!")
