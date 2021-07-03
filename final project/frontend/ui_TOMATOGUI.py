# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TOMATOGUIqYTxpQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import source

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        MainWindow.setMinimumSize(QSize(880, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"background-color: none;")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Roboto Condensed Light")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(20)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color: rgb(60, 231, 195);")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color: none;\n"
"\n"
"")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.labelimage = QLabel(self.content_bar)
        self.labelimage.setObjectName(u"labelimage")
        self.labelimage.setGeometry(QRect(320, 90, 201, 181))
        self.labelimage.setFrameShape(QFrame.WinPanel)
        self.labelimage.setFrameShadow(QFrame.Sunken)
        self.browse = QPushButton(self.content_bar)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(80, 30, 171, 31))
        self.browse.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 255, 255, 255), stop:0.653409 rgba(43, 130, 130, 255));\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);")
        self.browse.clicked.connect(self.browse1)
        self.pushbuttondetect = QPushButton(self.content_bar)
        self.pushbuttondetect.setObjectName(u"pushbuttondetect")
        self.pushbuttondetect.setGeometry(QRect(360, 290, 121, 31))
        self.pushbuttondetect.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 255, 255, 255), stop:0.772727 rgba(43, 130, 130, 255));\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);")
        self.pushbuttondetect.clicked.connect(self.tomato)
        self.labeldisease = QLabel(self.content_bar)
        self.labeldisease.setObjectName(u"labeldisease")
        self.labeldisease.setGeometry(QRect(40, 340, 211, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setPointSize(14)
        self.labeldisease.setFont(font2)
        self.labeldisease.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.diseasedisplay = QLabel(self.content_bar)
        self.diseasedisplay.setObjectName(u"diseasedisplay")
        self.diseasedisplay.setGeometry(QRect(270, 340, 311, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Black")
        font3.setPointSize(11)
        self.diseasedisplay.setFont(font3)
        self.diseasedisplay.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius:10px;\n"
"}")
        self.diseasedisplay.setAlignment(Qt.AlignCenter)
        self.pushbuttonsolution = QPushButton(self.content_bar)
        self.pushbuttonsolution.setObjectName(u"pushbuttonsolution")
        self.pushbuttonsolution.setGeometry(QRect(360, 390, 121, 31))
        self.pushbuttonsolution.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(85, 255, 255, 255), stop:0.772727 rgba(43, 130, 130, 255));\n"
"font: 87 14pt \"Segoe UI Black\";\n"
"color: rgb(0, 0, 0);")
        self.pushbuttonsolution.clicked.connect(self.tomato1)
        self.solution = QLabel(self.content_bar)
        self.solution.setObjectName(u"solution")
        self.solution.setGeometry(QRect(120, 440, 650, 100))
        self.solution.setFont(font3)
        self.solution.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius:10px;\n"
"}")
        self.solution.setAlignment(Qt.AlignLeft)
        self.label = QLabel(self.content_bar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 20, 241, 371))
        self.label.setStyleSheet(u"image: url(:/newPrefix/ClipartKey_107809.png);")
        self.filename = QLineEdit(self.content_bar)
        self.filename.setObjectName(u"filename")
        self.filename.setGeometry(QRect(270, 29, 321, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Black")
        font4.setPointSize(10)
        self.filename.setFont(font4)
        self.filename.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color: rgb(33, 33, 75);")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font5 = QFont()
        font5.setFamily(u"Roboto")
        self.label_credits.setFont(font5)
        self.label_credits.setStyleSheet(u"color: rgb(128, 102, 168);")

        self.verticalLayout_3.addWidget(self.label_credits)


        self.horizontalLayout_2.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def browse1(self):
        fname = QFileDialog.getOpenFileName(None,'Open file ','d:\ ', "Image files (*.jpg *.gif)")
        imagePath = fname[0]
        self.filename.setText(imagePath)
        pixmap = QPixmap(imagePath)
        pixmap5 = pixmap.scaled(200,200)
        self.labelimage.setPixmap(QPixmap(pixmap5))

    def tomato(self):
        import cv2
        import tensorflow as tf
        import numpy as np
        def prepare(filepath):
            img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
            img_array = img_array / 255
            new_array = cv2.resize(img_array, (224, 224))
            return new_array.reshape(-1, 224, 224, 3)

        model = tf.keras.models.load_model("vgg_19tl.model")

        import matplotlib.pyplot as plt
        def myfun(path):
            list1=["Bacterial_spot","Early_Blight","Septoria Leaf Mold","Yellow Leaf Curl Virus","Mosaic Virus","Healthy"]
            sol=["1.Copper fungicides will deny bacterial spot growth for two to four weeks after application.\n"
                 "2.Copper sprays are most effective when used before any signs of the disease are present as"
                 "a preventative treatment.",
                 "1.Good airflow will help keep the plants dry.Provide space for plants.\n"
                 "\n2.Copper or sulphur sprays and biofungicide serenade can prevent growth of fungus on "
                 "other parts.",
                "1.Copper sprays and Serenade® are somewhat effective at halting the spread of symptoms."
                 "\n2.Remove infected leaves to prevent the spread of spores to other leaves, as water "
                 "splashing on the leaves helps transmit the disease.",
                 "\n1.If symptomatic plants have no whiteflies on the lower leaf surface, these plants"
                 "can be cut from the garden and BURIED in the compost."
        "\n2.If whiteflies are beginning to appear, spray with azadirachtin (Neem), pyrethrin or"
                 "insecticidal soap.  insecticides be rotated at each spraying." 
        "\n3.Spray the undersides of the leaves thoroughly.",
                "1.Remove all infected plants and destroy them. Do NOT put them in the compost pile,"
                 "as the virus may persist in infected plant matter"
            "2.Monitor the rest of your plants closely, especially those that were located near "
                 "infected plants."
            "3.Disinfect gardening tools after every use.",
                "The leaf is healthy!!!! "]
            img = plt.imread(path)
            prediction = model.predict([prepare(path)])
            a=np.argmax(prediction)
            print(list1[a])
            plt.imshow(img)
            print("\nSolution:\n")
            print(sol[a])
            self.diseasedisplay.setText(list1[a])

        var=self.filename.text()   
        myfun(var)
        
        
        
    def tomato1(self):
        import cv2
        import tensorflow as tf
        import numpy as np
        def prepare(filepath):
            img_array = cv2.imread(filepath, cv2.IMREAD_COLOR)
            img_array = img_array / 255
            new_array = cv2.resize(img_array, (224, 224))
            return new_array.reshape(-1, 224, 224, 3)

        model = tf.keras.models.load_model("vgg_19tl.model")

        import matplotlib.pyplot as plt
        def myfun(path):
            list1=["Bacterial_spot","Early_Blight","Septoria Leaf Mold","Yellow Leaf Curl Virus","Mosaic Virus","Healthy"]
            sol=["1.Copper fungicides will deny bacterial spot growth for two to four weeks after application."
                 "\n2.Copper sprays are most effective when used before any signs of the disease are present as"
                 "a preventative treatment.",
                 "1.Good airflow will help keep the plants dry.Provide space for plants.\n"
                 "\n2.Copper or sulphur sprays and biofungicide serenade can prevent growth of fungus on "
                 "other parts.",
                "1.Copper sprays and Serenade® are somewhat effective at halting the spread of symptoms."
                 "\n2.Remove infected leaves to prevent the spread of spores to other leaves, as water "
                 "splashing on the leaves helps transmit the disease.",
                 "1.If symptomatic plants have no whiteflies on the lower leaf surface, these plants"
                 "can be cut from the garden and BURIED in the compost."
        "\n2.If whiteflies are beginning to appear, spray with azadirachtin (Neem), pyrethrin or"
                 "insecticidal soap.  insecticides be rotated at each spraying." 
        "\n3.Spray the undersides of the leaves thoroughly.",
                "1.Remove all infected plants and destroy them. Do NOT put them in the compost pile,"
                 "as the virus may persist in infected plant matter"
            "\n2.Monitor the rest of your plants closely, especially those that were located near "
                 "infected plants."
            "\n3.Disinfect gardening tools after every use.",
                "The leaf is healthy!!!! "]
            img = plt.imread(path)
            prediction = model.predict([prepare(path)])
            a=np.argmax(prediction)
            print(list1[a])
            plt.imshow(img)
            print("\nSolution:\n")
            print(sol[a])
            self.solution.setText(sol[a])
        var=self.filename.text()   
        myfun(var)
        
         
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"<strong>TOMATO LEAF DISEASE DETECTION", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.labelimage.setText("")
        self.browse.setText(QCoreApplication.translate("MainWindow", u"BROWSE ", None))
        self.pushbuttondetect.setText(QCoreApplication.translate("MainWindow", u"DETECT", None))
        self.labeldisease.setText(QCoreApplication.translate("MainWindow", u"Detected Disease :", None))
        self.diseasedisplay.setText("")
        self.pushbuttonsolution.setText(QCoreApplication.translate("MainWindow", u"SOLUTION", None))
        self.solution.setText("")
        self.label.setText("")
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"PROJECT BY : VISHAL , SUSHANTH , SHAILESH", None))
    # retranslateUi

