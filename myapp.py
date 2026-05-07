# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QRadioButton, QSizePolicy, QStatusBar, QToolBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1172, 894)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionedit = QAction(MainWindow)
        self.actionedit.setObjectName(u"actionedit")
        self.actionsetting = QAction(MainWindow)
        self.actionsetting.setObjectName(u"actionsetting")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name = QLabel(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(150, 70, 61, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.name.setFont(font)
        self.name_box = QLineEdit(self.centralwidget)
        self.name_box.setObjectName(u"name_box")
        self.name_box.setGeometry(QRect(230, 70, 231, 121))
        self.address = QLabel(self.centralwidget)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(150, 200, 61, 31))
        self.address.setFont(font)
        self.addess_box = QLineEdit(self.centralwidget)
        self.addess_box.setObjectName(u"addess_box")
        self.addess_box.setGeometry(QRect(230, 210, 231, 121))
        self.birdday_box = QDateTimeEdit(self.centralwidget)
        self.birdday_box.setObjectName(u"birdday_box")
        self.birdday_box.setGeometry(QRect(230, 360, 194, 26))
        self.e1 = QCheckBox(self.centralwidget)
        self.e1.setObjectName(u"e1")
        self.e1.setGeometry(QRect(230, 470, 84, 24))
        self.e2 = QCheckBox(self.centralwidget)
        self.e2.setObjectName(u"e2")
        self.e2.setGeometry(QRect(330, 470, 84, 24))
        self.e3 = QCheckBox(self.centralwidget)
        self.e3.setObjectName(u"e3")
        self.e3.setGeometry(QRect(430, 470, 84, 24))
        self.male = QRadioButton(self.centralwidget)
        self.male.setObjectName(u"male")
        self.male.setGeometry(QRect(230, 420, 98, 24))
        self.women = QRadioButton(self.centralwidget)
        self.women.setObjectName(u"women")
        self.women.setGeometry(QRect(330, 420, 98, 24))
        self.birdday = QLabel(self.centralwidget)
        self.birdday.setObjectName(u"birdday")
        self.birdday.setGeometry(QRect(140, 350, 61, 31))
        self.birdday.setFont(font)
        self.sex = QLabel(self.centralwidget)
        self.sex.setObjectName(u"sex")
        self.sex.setGeometry(QRect(140, 420, 61, 31))
        self.sex.setFont(font)
        self.educational = QLabel(self.centralwidget)
        self.educational.setObjectName(u"educational")
        self.educational.setGeometry(QRect(140, 460, 61, 31))
        self.educational.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1172, 33))
        self.menufile = QMenu(self.menubar)
        self.menufile.setObjectName(u"menufile")
        self.menuExt = QMenu(self.menubar)
        self.menuExt.setObjectName(u"menuExt")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QToolBar(MainWindow)
        self.toolBar_3.setObjectName(u"toolBar_3")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar_3)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuExt.menuAction())
        self.menufile.addAction(self.actionopen)
        self.menufile.addAction(self.actionedit)
        self.menufile.addAction(self.actionsetting)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionedit.setText(QCoreApplication.translate("MainWindow", u"edit", None))
        self.actionsetting.setText(QCoreApplication.translate("MainWindow", u"setting", None))
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d \u0e2a\u0e01\u0e38\u0e25", None))
        self.address.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48", None))
        self.e1.setText(QCoreApplication.translate("MainWindow", u"\u0e1b.\u0e15\u0e23\u0e35", None))
        self.e2.setText(QCoreApplication.translate("MainWindow", u"\u0e1b.\u0e42\u0e17", None))
        self.e3.setText(QCoreApplication.translate("MainWindow", u"\u0e1b.\u0e40\u0e2d\u0e01", None))
        self.male.setText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e23\u0e30\u0e40\u0e17\u0e22", None))
        self.women.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e2d\u0e21", None))
        self.birdday.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e19\u0e40\u0e01\u0e34\u0e14", None))
        self.sex.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1e\u0e28", None))
        self.educational.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e38\u0e12\u0e34\u0e01\u0e32\u0e23\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        self.menuExt.setTitle(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.toolBar_3.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_3", None))
    # retranslateUi

