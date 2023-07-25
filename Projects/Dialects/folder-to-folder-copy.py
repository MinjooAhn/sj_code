# 소스 폴더 안의 파일들을 목적지 폴더로 복사하는 코드
import os
import shutil

source_folder = r""  # 데이터 폴더 경로
saving_folder = r""  # 저장 폴더 경로

# 저장 폴더 경로가 없을 경우 제작
if not os.path.exists(saving_folder):
    os.makedirs(saving_folder)

# 데이터 폴더 안의 파일들 복사
for item in os.listdir(source_folder):
    item_path = os.path.join(source_folder, item)
    destination_path = os.path.join(saving_folder, item)

    # 저장 폴더로 파일 붙여넣기
    shutil.copy(item_path, destination_path)

print("Contents moved successfully!")