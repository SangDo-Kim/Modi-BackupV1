# Modi-Backup V1.0
Written by SangDo_Kim, https://sangdo-kim.blogspot.com
This Python program backs ups files in a folder and sub-folders to a ZIP file.
ZIP file name example: doc_folder_20240518_161411.zip.
It also provides options to backup only new or modified files, or all files.
이 파이선 프로그램은 폴더 및 그 하위 폴더의 파일들을 ZIP 파일로 백업합니다.
ZIP 파일 이름 예: doc_folder_20240518_161411.zip.
또한 새 파일 또는 변경된 파일만 백업할지, 모든 파일을 백업할지도 선택할 수 있습니다.

sangdo_mod package (not in Python Package Index (PyPI), but it's my own custom package):
The main py file imports as follows:
- from sangdo_mod.config import Config
- from sangdo_mod.time_stamp import get_time_stamp
You need to import sangdo_mod package which are in my_module folder,
or just copy needed modules (py files) above into the same folder with main py and change the import statements.

V1.0
- Initial creation
