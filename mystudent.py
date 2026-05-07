# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_student_univercity.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1143, 606)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.student_id_box = QLineEdit(self.centralwidget)
        self.student_id_box.setObjectName(u"student_id_box")
        self.student_id_box.setGeometry(QRect(420, 70, 231, 31))
        self.student_id = QLabel(self.centralwidget)
        self.student_id.setObjectName(u"student_id")
        self.student_id.setGeometry(QRect(280, 70, 141, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.student_id.setFont(font)
        self.firstname = QLabel(self.centralwidget)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(280, 130, 31, 41))
        self.firstname.setFont(font)
        self.firstname_box = QLineEdit(self.centralwidget)
        self.firstname_box.setObjectName(u"firstname_box")
        self.firstname_box.setGeometry(QRect(420, 140, 231, 31))
        self.lastname = QLabel(self.centralwidget)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(280, 190, 71, 41))
        self.lastname.setFont(font)
        self.lastname_box = QLineEdit(self.centralwidget)
        self.lastname_box.setObjectName(u"lastname_box")
        self.lastname_box.setGeometry(QRect(420, 200, 231, 31))
        self.sex = QLabel(self.centralwidget)
        self.sex.setObjectName(u"sex")
        self.sex.setGeometry(QRect(280, 270, 71, 41))
        self.sex.setFont(font)
        self.male = QRadioButton(self.centralwidget)
        self.male.setObjectName(u"male")
        self.male.setGeometry(QRect(430, 280, 98, 24))
        self.femalle = QRadioButton(self.centralwidget)
        self.femalle.setObjectName(u"femalle")
        self.femalle.setGeometry(QRect(530, 280, 98, 24))
        self.major = QLabel(self.centralwidget)
        self.major.setObjectName(u"major")
        self.major.setGeometry(QRect(280, 350, 71, 41))
        self.major.setFont(font)
        self.major_box = QComboBox(self.centralwidget)
        self.major_box.setObjectName(u"major_box")
        self.major_box.setGeometry(QRect(420, 350, 231, 26))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(290, 440, 361, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_button = QMenuBar(MainWindow)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setGeometry(QRect(0, 0, 1143, 33))
        MainWindow.setMenuBar(self.menu_button)
        self.menu_button_2 = QStatusBar(MainWindow)
        self.menu_button_2.setObjectName(u"menu_button_2")
        MainWindow.setStatusBar(self.menu_button_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.student_id.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e2b\u0e31\u0e2a\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.firstname.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d", None))
        self.lastname.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.sex.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1e\u0e28", None))
        self.male.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e32\u0e22", None))
        self.femalle.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e0d\u0e34\u0e07", None))
        self.major.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e32\u0e02\u0e32\u0e27\u0e34\u0e0a\u0e32", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e49\u0e32\u0e07", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e01\u0e49\u0e44\u0e02", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
    # retranslateUi

