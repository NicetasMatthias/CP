# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1313, 526)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.symmKeyLineEdit = QLineEdit(self.groupBox)
        self.symmKeyLineEdit.setObjectName(u"symmKeyLineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.symmKeyLineEdit)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.senderGroupBox = QGroupBox(self.groupBox_2)
        self.senderGroupBox.setObjectName(u"senderGroupBox")
        self.formLayout_2 = QFormLayout(self.senderGroupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.senderGroupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.senderOpenLineEdit = QLineEdit(self.senderGroupBox)
        self.senderOpenLineEdit.setObjectName(u"senderOpenLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.senderOpenLineEdit)

        self.label_5 = QLabel(self.senderGroupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.senderPrivateLineEdit = QLineEdit(self.senderGroupBox)
        self.senderPrivateLineEdit.setObjectName(u"senderPrivateLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.senderPrivateLineEdit)


        self.verticalLayout_5.addWidget(self.senderGroupBox)

        self.receiverGroupBox = QGroupBox(self.groupBox_2)
        self.receiverGroupBox.setObjectName(u"receiverGroupBox")
        self.formLayout = QFormLayout(self.receiverGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.receiverGroupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.receiverOpenLineEdit = QLineEdit(self.receiverGroupBox)
        self.receiverOpenLineEdit.setObjectName(u"receiverOpenLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.receiverOpenLineEdit)

        self.label_3 = QLabel(self.receiverGroupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.receiverPrivateLineEdit = QLineEdit(self.receiverGroupBox)
        self.receiverPrivateLineEdit.setObjectName(u"receiverPrivateLineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.receiverPrivateLineEdit)


        self.verticalLayout_5.addWidget(self.receiverGroupBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.genKeysPushButton = QPushButton(self.groupBox_2)
        self.genKeysPushButton.setObjectName(u"genKeysPushButton")

        self.horizontalLayout_2.addWidget(self.genKeysPushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_6.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_6 = QGroupBox(self.groupBox_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.groupBox_6)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_6)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.cipherTextEdit = QPlainTextEdit(self.groupBox_6)
        self.cipherTextEdit.setObjectName(u"cipherTextEdit")

        self.verticalLayout_2.addWidget(self.cipherTextEdit)


        self.horizontalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.receivedPlainTextEdit = QPlainTextEdit(self.groupBox_6)
        self.receivedPlainTextEdit.setObjectName(u"receivedPlainTextEdit")

        self.verticalLayout_3.addWidget(self.receivedPlainTextEdit)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.OriginalEcpLineEdit = QLineEdit(self.groupBox_5)
        self.OriginalEcpLineEdit.setObjectName(u"OriginalEcpLineEdit")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.OriginalEcpLineEdit)

        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.senderHashLineEdit = QLineEdit(self.groupBox_5)
        self.senderHashLineEdit.setObjectName(u"senderHashLineEdit")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.senderHashLineEdit)


        self.horizontalLayout_5.addLayout(self.formLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(255, 89, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_13)

        self.decryptedEcpLineEdit = QLineEdit(self.groupBox_5)
        self.decryptedEcpLineEdit.setObjectName(u"decryptedEcpLineEdit")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.decryptedEcpLineEdit)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.CalculatedEcpLineEdit = QLineEdit(self.groupBox_5)
        self.CalculatedEcpLineEdit.setObjectName(u"CalculatedEcpLineEdit")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.CalculatedEcpLineEdit)

        self.receiverHashLineEdit = QLineEdit(self.groupBox_5)
        self.receiverHashLineEdit.setObjectName(u"receiverHashLineEdit")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.receiverHashLineEdit)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_15)


        self.horizontalLayout_5.addLayout(self.formLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_5)

        self.groupBox_7 = QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.encKeyLineEdit = QLineEdit(self.groupBox_7)
        self.encKeyLineEdit.setObjectName(u"encKeyLineEdit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.encKeyLineEdit)


        self.horizontalLayout_3.addLayout(self.formLayout_4)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.decrKeyLineEdit = QLineEdit(self.groupBox_7)
        self.decrKeyLineEdit.setObjectName(u"decrKeyLineEdit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.decrKeyLineEdit)


        self.horizontalLayout_3.addLayout(self.formLayout_5)


        self.verticalLayout_4.addWidget(self.groupBox_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.proceedPushButton = QPushButton(self.groupBox_3)
        self.proceedPushButton.setObjectName(u"proceedPushButton")

        self.horizontalLayout_4.addWidget(self.proceedPushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_8 = QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_16 = QLabel(self.groupBox_8)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_6.addWidget(self.label_16)

        self.aesPushButton = QPushButton(self.groupBox_8)
        self.aesPushButton.setObjectName(u"aesPushButton")

        self.verticalLayout_6.addWidget(self.aesPushButton)


        self.verticalLayout_11.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.groupBox_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_17 = QLabel(self.groupBox_9)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_7.addWidget(self.label_17)

        self.rsaPushButton = QPushButton(self.groupBox_9)
        self.rsaPushButton.setObjectName(u"rsaPushButton")

        self.verticalLayout_7.addWidget(self.rsaPushButton)


        self.verticalLayout_11.addWidget(self.groupBox_9)

        self.groupBox_12 = QGroupBox(self.groupBox_4)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_18 = QLabel(self.groupBox_12)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_8.addWidget(self.label_18)

        self.hashPushButton = QPushButton(self.groupBox_12)
        self.hashPushButton.setObjectName(u"hashPushButton")

        self.verticalLayout_8.addWidget(self.hashPushButton)


        self.verticalLayout_11.addWidget(self.groupBox_12)

        self.groupBox_10 = QGroupBox(self.groupBox_4)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_19 = QLabel(self.groupBox_10)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_9.addWidget(self.label_19)

        self.ecpPushButton = QPushButton(self.groupBox_10)
        self.ecpPushButton.setObjectName(u"ecpPushButton")

        self.verticalLayout_9.addWidget(self.ecpPushButton)


        self.verticalLayout_11.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox_4)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_20 = QLabel(self.groupBox_11)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_10.addWidget(self.label_20)

        self.finalPushButton = QPushButton(self.groupBox_11)
        self.finalPushButton.setObjectName(u"finalPushButton")

        self.verticalLayout_10.addWidget(self.finalPushButton)


        self.verticalLayout_11.addWidget(self.groupBox_11)


        self.horizontalLayout_6.addWidget(self.groupBox_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Keys", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Symm key", None))
        self.senderGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sender", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Open key", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Private key", None))
        self.receiverGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Receiver", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Open key", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Private key", None))
        self.genKeysPushButton.setText(QCoreApplication.translate("MainWindow", u"Gen keys", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Demostration", None))
        self.groupBox_6.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Plaint text", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Enc text", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Decr text", None))
        self.groupBox_5.setTitle("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Original ecp", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Sender hash", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Decrypted ecp", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Calculated ecp", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Receiver hash", None))
        self.groupBox_7.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Enc key", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Decr key", None))
        self.proceedPushButton.setText(QCoreApplication.translate("MainWindow", u"Proced", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.groupBox_8.setTitle("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"AES_INF", None))
        self.aesPushButton.setText(QCoreApplication.translate("MainWindow", u"AES", None))
        self.groupBox_9.setTitle("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"RSA_INF", None))
        self.rsaPushButton.setText(QCoreApplication.translate("MainWindow", u"RSA", None))
        self.groupBox_12.setTitle("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"HASH_INF", None))
        self.hashPushButton.setText(QCoreApplication.translate("MainWindow", u"HASH", None))
        self.groupBox_10.setTitle("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"ECP_INF", None))
        self.ecpPushButton.setText(QCoreApplication.translate("MainWindow", u"ECP", None))
        self.groupBox_11.setTitle("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"FINAL_INF", None))
        self.finalPushButton.setText(QCoreApplication.translate("MainWindow", u"FINAL", None))
    # retranslateUi

