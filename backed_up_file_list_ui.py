# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'backed_up_file_list_uiRVoYnS.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.WindowModal)
        MainWindow.resize(278, 413)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 21))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QRect(10, 40, 261, 51))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"        color: rgb(0, 0, 0);\n"
"		font: 9pt \"\ub9d1\uc740 \uace0\ub515\";\n"
"    }")
        self.plainTextEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 140, 261, 251))
        self.label_zip_name = QLabel(self.centralwidget)
        self.label_zip_name.setObjectName(u"label_zip_name")
        self.label_zip_name.setGeometry(QRect(10, 90, 251, 16))
        self.label_size = QLabel(self.centralwidget)
        self.label_size.setObjectName(u"label_size")
        self.label_size.setGeometry(QRect(10, 110, 101, 16))
        self.pushButton_open_folder = QPushButton(self.centralwidget)
        self.pushButton_open_folder.setObjectName(u"pushButton_open_folder")
        self.pushButton_open_folder.setGeometry(QRect(250, 110, 21, 24))
        icon = QIcon()
        icon.addFile(u":/icons/open_folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_open_folder.setIcon(icon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Backed up file list", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Backed up file list", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"For all the files matched with the conditions, 00 files were backed up!", None))
        self.label_zip_name.setText(QCoreApplication.translate("MainWindow", u"Python Programs_20240526_154826.zip", None))
        self.label_size.setText(QCoreApplication.translate("MainWindow", u"Size: 29KB", None))
        self.pushButton_open_folder.setText("")
    # retranslateUi

