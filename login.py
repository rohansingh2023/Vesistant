# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
# import homePage
import mysql.connector
import cv2
from txttsp import speak
import gui8
from Ai_Assistant import AiAssistant
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from gui8 import Ui_MainWindow
import sys
import homePage2


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(1128, 787)
        width = 1128
        height = 787
        Form.setFixedSize(width, height)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "")
        Form.setWindowIcon(QtGui.QIcon("images/window_logo.jpg"))
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(260, 430, 261, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "background-color: rgb(170,170,170);\n"
                                    "border:3px solid #747474;\n"
                                    "border-radius: 10px;\n"
                                    "font:Arial;\n"
                                    "}\n"
                                    "QLineEdit:Focus{\n"
                                    "border:3px solid rgb(0,0,255);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 220, 151, 41))
        self.pushButton_2.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(170,170,170);\n"
                                        "border-radius: 20px;\n"
                                        "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "border:3px solid #747474;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: #a5b6ff;\n"
                                        "border:5px solid #0000ff ;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 1131, 801))
        self.label_4.setStyleSheet("color: rgb(0, 0, 255);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: rgb(0, 0, 0);")
        self.label_4.setText("")
        # self.label_4.setPixmap(QtGui.QPixmap("images/newai.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 410, 261, 31))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
                                      "background-color: #a6b7ff;\n"
                                      "border:3px solid rgb(0,0,170);\n"
                                      "border-radius: 10px;\n"
                                      "font:Arial;\n"
                                      "}\n"
                                      "QLineEdit:Focus{\n"
                                      "border:3px solid #ffff00;\n"
                                      "background-color: #ffffd9;\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 620, 151, 41))
        self.pushButton_3.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(0,0,0);\n"
                                        "color: #fff;\n"
                                        "border:0.5px solid rgb(0,255,0);\n"
                                        "border-radius: 10px;\n"
                                        "font: 75 8pt ;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(0,255,0);\n"
                                        "color: #fff\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 490, 171, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 400, 171, 51))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font: 12pt \"MS Shell Dlg 2\";\n"
                                   "background-color: none")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 500, 261, 31))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
                                      "background-color: #a6b7ff;\n"
                                      "border:3px solid rgb(0,0,170);\n"
                                      "border-radius: 10px;\n"
                                      "font:Arial;\n"
                                      "}\n"
                                      "QLineEdit:Focus{\n"
                                      "border:3px solid #ffff00;\n"
                                      "background-color: #ffffd9;\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(160, 90, 531, 51))
        self.label_7.setStyleSheet("color: #fff;\n"
                                   "font: 20pt ;\n"
                                   "font-style: Bold;\n"
                                   "background-color: none;\n"
                                   "")
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 220, 151, 41))
        self.pushButton_4.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(0, 0, 0);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "border-radius: 10px;\n"
                                        "font: 75 8pt \"MS Shell Dlg 2\";\n"
                                        "border:1px solid rgb(0,0,255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(0,0,255);\n"
                                        "color: #fff\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(640, 200, 401, 331))
        self.label.setStyleSheet(
            "background-image: url(images/login.gif);")
        self.label.setText("")
        self.movie = QtGui.QMovie("images/login.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(480, 620, 191, 41))
        self.pushButton_5.setStyleSheet("\n"
                                        "QPushButton{\n"
                                        "background-color: rgb(0,0,0);\n"
                                        "color: #fff;\n"
                                        "border:0.5px solid rgb(255,0,0);\n"
                                        "border-radius: 10px;\n"
                                        "font: 75 8pt ;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(255,0,0);\n"
                                        "color: #fff\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(90, 330, 561, 2))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 320, 41, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_5.clicked.connect(self.go_to_homePage)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_4.clicked.connect(self.detect_face)
        self.pushButton_4.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(self.go_to_mainPage)
        self.pushButton_3.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def go_to_homePage(self):
        self.window = QtWidgets.QMainWindow()
        # self.ui = homePage.UI_Window()
        self.ui = homePage2.Ui_MainWindow()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()

    def go_to_mainPage(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = gui8.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def detect_face(self):
        speak("Recognizing the User")

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_img, scaleFactor, minNeighbors)

            confidence = 0
            s = ""

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)

                id, pred = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int(100*(1-pred/300))

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="face_rec"
                )
                mycursor = mydb.cursor()
                mycursor.execute(
                    "select name from user_table where id="+str(id))
                s = mycursor.fetchone()
                s = ''+''.join(s)

                if confidence > 70:
                    cv2.putText(
                        img, s, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)

                    # self.go_to_mainPage()
                    # break

                else:
                    cv2.putText(
                        img, "UNKNOWN", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

            # if confidence > 70:
            #     self.go_to_mainPage()

            return img, confidence, s

        # loading classifier
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img, confidence, s = draw_boundary(img, faceCascade, 1.3, 6,
                                               (255, 255, 255), "Face", clf)
            cv2.imshow("face Detection", img)

            if confidence > 70:
                self.go_to_mainPage()
                speak("User login successfull")
                speak("Welcome " + s)
                speak("Click the Run button to start the assistant")
                break

            if cv2.waitKey(1) == 13:
                break
        video_capture.release()
        cv2.destroyAllWindows()
        return s

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGIN"))
        self.pushButton_2.setText(_translate("Form", "FACE LOGIN"))
        self.pushButton_3.setText(_translate("Form", "LOGIN"))
        self.label_5.setText(_translate("Form", "ENTER PASSWORD"))
        self.label_6.setText(_translate("Form", "ENTER USERNAME"))
        self.label_7.setText(_translate(
            "Form", "LOGIN USING FACE RECOGNITION"))
        self.pushButton_4.setText(_translate("Form", "FACE LOGIN"))
        self.pushButton_5.setText(_translate("Form", "Go Back to Home Page"))
        self.label_2.setText(_translate("Form", "   OR"))
# import test1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
