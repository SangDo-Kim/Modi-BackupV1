"""# Modi-Backup V1.0
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
"""

import fnmatch
import glob
import os
import zipfile

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from modi_backup_ui import Ui_MainWindow
from my_constants import MyCons
from sangdo_mod.config import Config
from sangdo_mod.time_stamp import get_time_stamp
from get_matched_files import get_matched_files
from dict_data import DictData


try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'sangdo-kim.software.modi-backup.100'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Modi-Backup V1.0")
        self.matched_list = []
        self.backup_log = DictData("backup_log.json")
        self.backup_log.load_from_file()

        # It is part of backup zip file name.
        self.dir_name = None

        # Load config file
        self.my_config = MyConfig()
        if self.my_config.load_from_file():
            self.label_source.setText(self.my_config.source_folder)
            self.label_target.setText(self.my_config.target_folder)
            self.lineEdit_pattern.setText(self.my_config.pattern)
            if self.my_config.all_or_mod == "mod":
                self.radioButton_mod.setChecked(True)
            else:
                self.radioButton_all.setChecked(True)
            self.comboBox_sub_level.setCurrentIndex(self.my_config.sub_level)
        else:
            # If there is no config file.
            self.radioButton_all.setChecked(True)

        # Other initialization
        self.show_last_backup()

        # Connect: Buttons
        self.pushButton_source_select.clicked.connect(self.select_source_folder)
        self.pushButton_target_select.clicked.connect(self.select_target_folder)
        self.pushButton_backup.clicked.connect(self.backup)
        self.pushButton_source_open.clicked.connect(self.open_source)
        self.pushButton_target_open.clicked.connect(self.open_target)
        self.pushButton_count.clicked.connect(self.count_matched_files)

        # Connect: Update self.label_matched
        self.lineEdit_pattern.textChanged.connect(self.label_matched_reset)
        self.comboBox_sub_level.currentIndexChanged.connect(self.label_matched_reset)

    def select_source_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select a Folder")
        if folder_path:
            self.label_source.setText(folder_path)
        else:
            self.label_source.setText(MyCons.not_selected_yet)
        self.label_matched_reset()
        self.show_last_backup()

    def select_target_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select a Folder")
        if folder_path:
            self.label_target.setText(folder_path)
        else:
            self.label_target.setText(MyCons.not_selected_yet)
        self.show_last_backup()

    def backup(self):
        self.update_my_config()
        self.my_config.save_to_file()

        if self.label_source.text() == MyCons.none_str:
            QMessageBox.information(self, "Info",
                "Select a folder to backup first."
                )
            return

        if self.label_target.text() == MyCons.none_str:
            QMessageBox.information(self, "Info",
                "Select a folder to save backup ZIP file first."
                )
            return

        if self.label_matched.text() == MyCons.none_str:
            self.count_matched_files()
            QCoreApplication.processEvents()

        if len(self.matched_list) == 0:
            QMessageBox.information(self, "Info",
                "No files to backup with the current conditions. Consider changing folder or file types"
                )
            return None

        zip_filename = self.get_zip_filename()
        zip_full_path = os.path.join(self.label_target.text(), zip_filename)

        backed_up_no = 0
        source_path_len = len(self.label_source.text())
        with zipfile.ZipFile(zip_full_path, 'w') as zipf:
            for file_path in self.matched_list:
                if os.path.exists(file_path):
                    modified_datetime = os.path.getmtime(file_path)
                    if self.radioButton_mod.isChecked():
                        try:
                            modified_datetime_backup = self.backup_log.dict[file_path]
                        except KeyError:
                            # This file has not been backed up, so go on to the next process.
                            pass
                        else:
                            if modified_datetime_backup == modified_datetime:
                                # Skip this file
                                continue
                            else:
                                # This file has been backed up, but it has been modified after backup.
                                pass

                    zipf.write(file_path, file_path[source_path_len:])
                    backed_up_no += 1
                    self.backup_log.dict[file_path] = modified_datetime
                else:
                    continue

        if backed_up_no == 0:
            # The new backup file contains 0 files
            try:
                os.remove(zip_full_path)
            except OSError as e:
                self.statusbar.showMessage(f"Error: {e.strerror}")

        self.backup_log.save_to_file()

        if self.radioButton_mod.isChecked():
            QMessageBox.information(self, "Info",
                                    f"Only for new or modified files, {backed_up_no} files were backed up!"
                                    )
        else:
            QMessageBox.information(self, "Info",
                                    f"For all the files matched with the conditions, "
                                    f"{backed_up_no} files were backed up!"
                                    )
        self.statusbar.showMessage(f"{backed_up_no} files were backed up!", 10000)
        self.show_last_backup()

    def update_my_config(self):
        self.my_config.source_folder = self.label_source.text()
        self.my_config.target_folder = self.label_target.text()
        self.my_config.pattern = self.lineEdit_pattern.text()
        if self.radioButton_mod.isChecked():
            self.my_config.all_or_mod = "mod"
        else:
            self.my_config.all_or_mod = "all"
        self.my_config.sub_level = self.comboBox_sub_level.currentIndex()

    def open_source(self):
        os.startfile(self.label_source.text())

    def open_target(self):
        os.startfile(self.label_target.text())

    def count_matched_files(self):
        if self.label_source.text() == MyCons.none_str:
            QMessageBox.information(self, "Info",
                "Select a folder to backup first."
                )
            return

        self.label_matched.setText(f"Counting...")
        QCoreApplication.processEvents()

        self.get_matched_list()
        matched_list_no = len(self.matched_list)
        self.label_matched.setText(f"{matched_list_no} files are searched with the current conditions.")

    def get_matched_list(self):
        sub_level = self.comboBox_sub_level.currentIndex()
        if sub_level == 5:
            sub_level = 99

        self.matched_list = get_matched_files(
            self.label_source.text(),
            self.lineEdit_pattern.text(),
            sub_level
        )

    def label_matched_reset(self):
        self.label_matched.setText(MyCons.none_str)
        self.matched_list = []

    def get_zip_filename(self):
        self.get_dir_name()
        filename = self.dir_name + "_" + get_time_stamp() + ".zip"

        return filename

    def show_last_backup(self):
        self.get_dir_name()
        if (
                self.label_target.text() == MyCons.none_str
                or self.label_source.text() == MyCons.none_str
                ):
            self.label_last_backup.setText(MyCons.none_str)
        else:
            glob_pattern = f"{self.label_target.text()}/{self.dir_name}*.zip"
            zip_files = glob.glob(glob_pattern)
            if len(zip_files) > 0:
                zip_file_path = zip_files[-1]
                _, zip_filename = os.path.split(zip_file_path)
                self.label_last_backup.setText(zip_filename)
            else:
                self.label_last_backup.setText(MyCons.none_str)

    def get_dir_name(self):
        path = self.label_source.text().replace("/", "\\")
        path_split = path.split("\\")
        if len(path_split[-1]) > 0:
            self.dir_name = path_split[-1]
        elif len(path_split) >= 2:
            self.dir_name = path_split[-2]
            if self.dir_name.find(":") >= 0:
                self.dir_name = self.dir_name.replace(":", " Drive")
        else:
            self.dir_name = None


class MyConfig(Config):
    def __init__(self):
        super().__init__()
        self.source_folder = ""
        self.target_folder = ""
        self.pattern = ""
        self.all_or_mod = ""     # values: "all", "mod". Backup all matched or only modified.
        self.sub_level = 0


app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec()
