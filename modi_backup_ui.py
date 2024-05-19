# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modi_backup_uixzkZFr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 536)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 60))
        self.label_title.setAutoFillBackground(False)
        self.label_title.setStyleSheet(u"QLabel {\n"
"    background-color: #4A5D5E;\n"
"}")
        self.label_title.setPixmap(QPixmap(u":/icons/modi_backup_logo_banner_60.png"))

        self.verticalLayout_3.addWidget(self.label_title)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setStyleSheet(u"QTextBrowser {\n"
"    background-color: transparent;\n"
"	color: rgb(0, 0, 0)\n"
"}")
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_3.addWidget(self.textBrowser)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 200))
        self.groupBox.setMaximumSize(QSize(16777215, 200))
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_matched = QLabel(self.groupBox)
        self.label_matched.setObjectName(u"label_matched")

        self.gridLayout.addWidget(self.label_matched, 6, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 32))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.pushButton_source_open = QPushButton(self.groupBox)
        self.pushButton_source_open.setObjectName(u"pushButton_source_open")
        self.pushButton_source_open.setMinimumSize(QSize(25, 25))
        self.pushButton_source_open.setMaximumSize(QSize(25, 25))
        self.pushButton_source_open.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/open_folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_source_open.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_source_open, 0, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)

        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)

        self.comboBox_sub_level = QComboBox(self.groupBox)
        self.comboBox_sub_level.addItem("")
        self.comboBox_sub_level.addItem("")
        self.comboBox_sub_level.addItem("")
        self.comboBox_sub_level.addItem("")
        self.comboBox_sub_level.addItem("")
        self.comboBox_sub_level.addItem("")
        self.comboBox_sub_level.setObjectName(u"comboBox_sub_level")
        self.comboBox_sub_level.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.comboBox_sub_level, 4, 2, 1, 1)

        self.pushButton_count = QPushButton(self.groupBox)
        self.pushButton_count.setObjectName(u"pushButton_count")
        icon1 = QIcon()
        icon1.addFile(u":/icons/search64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_count.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton_count, 6, 0, 1, 1)

        self.pushButton_source_select = QPushButton(self.groupBox)
        self.pushButton_source_select.setObjectName(u"pushButton_source_select")
        self.pushButton_source_select.setMinimumSize(QSize(120, 25))
        self.pushButton_source_select.setMaximumSize(QSize(120, 25))
        self.pushButton_source_select.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_source_select, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(False)
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)

        self.label_source = QLabel(self.groupBox)
        self.label_source.setObjectName(u"label_source")

        self.gridLayout.addWidget(self.label_source, 0, 2, 1, 1)

        self.lineEdit_pattern = QLineEdit(self.groupBox)
        self.lineEdit_pattern.setObjectName(u"lineEdit_pattern")

        self.gridLayout.addWidget(self.lineEdit_pattern, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        self.groupBox_2.setFont(font)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_target_select = QPushButton(self.groupBox_2)
        self.pushButton_target_select.setObjectName(u"pushButton_target_select")
        self.pushButton_target_select.setMinimumSize(QSize(0, 25))
        self.pushButton_target_select.setMaximumSize(QSize(120, 25))
        self.pushButton_target_select.setIcon(icon)

        self.gridLayout_2.addWidget(self.pushButton_target_select, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_target = QLabel(self.groupBox_2)
        self.label_target.setObjectName(u"label_target")
        self.label_target.setMinimumSize(QSize(0, 32))

        self.gridLayout_2.addWidget(self.label_target, 0, 2, 1, 1)

        self.radioButton_mod = QRadioButton(self.groupBox_2)
        self.radioButton_mod.setObjectName(u"radioButton_mod")

        self.gridLayout_2.addWidget(self.radioButton_mod, 3, 2, 1, 1)

        self.pushButton_backup = QPushButton(self.groupBox_2)
        self.pushButton_backup.setObjectName(u"pushButton_backup")
        icon2 = QIcon()
        icon2.addFile(u":/icons/backup_icon32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_backup.setIcon(icon2)

        self.gridLayout_2.addWidget(self.pushButton_backup, 2, 0, 1, 1)

        self.pushButton_target_open = QPushButton(self.groupBox_2)
        self.pushButton_target_open.setObjectName(u"pushButton_target_open")
        self.pushButton_target_open.setMinimumSize(QSize(25, 25))
        self.pushButton_target_open.setMaximumSize(QSize(25, 25))
        self.pushButton_target_open.setIcon(icon)

        self.gridLayout_2.addWidget(self.pushButton_target_open, 0, 4, 1, 1)

        self.radioButton_all = QRadioButton(self.groupBox_2)
        self.radioButton_all.setObjectName(u"radioButton_all")

        self.gridLayout_2.addWidget(self.radioButton_all, 2, 2, 1, 1)

        self.label_last_backup = QLabel(self.groupBox_2)
        self.label_last_backup.setObjectName(u"label_last_backup")
        self.label_last_backup.setMinimumSize(QSize(0, 32))

        self.gridLayout_2.addWidget(self.label_last_backup, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Written by SangDo_Kim, <a href=\"https://sangdo-kim.blogspot.com\"><span style=\" text-decoration: underline; color:#0078d7;\">https://sangdo-kim.blogspot.com</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program can backup files in a folder and sub-folders to a zip file (e.g: doc_folde"
                        "r_20240518_161411.zip)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">It also provides options to backup only new or modified files, or all files.</p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Folder and files to backup", None))
        self.label_matched.setText(QCoreApplication.translate("MainWindow", u"*None*", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Files to backup:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Subfolder level:", None))
        self.pushButton_source_open.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tip: Level 1 means subfolders are included. Level 2 means subfolders of subfolders are also included.", None))
        self.comboBox_sub_level.setItemText(0, QCoreApplication.translate("MainWindow", u"No subfolder", None))
        self.comboBox_sub_level.setItemText(1, QCoreApplication.translate("MainWindow", u"Level 1", None))
        self.comboBox_sub_level.setItemText(2, QCoreApplication.translate("MainWindow", u"Level 2", None))
        self.comboBox_sub_level.setItemText(3, QCoreApplication.translate("MainWindow", u"Level 3", None))
        self.comboBox_sub_level.setItemText(4, QCoreApplication.translate("MainWindow", u"Level 4", None))
        self.comboBox_sub_level.setItemText(5, QCoreApplication.translate("MainWindow", u"All the levels", None))

        self.pushButton_count.setText(QCoreApplication.translate("MainWindow", u"Count files", None))
        self.pushButton_source_select.setText(QCoreApplication.translate("MainWindow", u"Select a folder", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tip: Add file types separated by semicolons (;). e.g: *.txt; *.xls; *.doc or for all files: *.*", None))
        self.label_source.setText(QCoreApplication.translate("MainWindow", u"*Not selected yet*", None))
        self.lineEdit_pattern.setText(QCoreApplication.translate("MainWindow", u"*.*", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Back them up!", None))
        self.pushButton_target_select.setText(QCoreApplication.translate("MainWindow", u"Select a folder", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Last backup:", None))
        self.label_target.setText(QCoreApplication.translate("MainWindow", u"*Not selected yet*", None))
        self.radioButton_mod.setText(QCoreApplication.translate("MainWindow", u"Only new or modified files", None))
        self.pushButton_backup.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.pushButton_target_open.setText("")
        self.radioButton_all.setText(QCoreApplication.translate("MainWindow", u"All files", None))
        self.label_last_backup.setText(QCoreApplication.translate("MainWindow", u"*None*", None))
    # retranslateUi

