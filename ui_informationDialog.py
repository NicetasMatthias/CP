# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'informationDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1218, 538)
        Dialog.setModal(True)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.InfoLabel = QLabel(Dialog)
        self.InfoLabel.setObjectName(u"InfoLabel")

        self.verticalLayout.addWidget(self.InfoLabel)

        self.InfoTextBrowser = QTextBrowser(Dialog)
        self.InfoTextBrowser.setObjectName(u"InfoTextBrowser")

        self.verticalLayout.addWidget(self.InfoTextBrowser)

        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelPic1 = QLabel(self.tabWidgetPage1)
        self.labelPic1.setObjectName(u"labelPic1")

        self.verticalLayout_4.addWidget(self.labelPic1)

        self.verticalLayout_4.setStretch(0, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.verticalLayout_5 = QVBoxLayout(self.tabWidgetPage2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelPic2 = QLabel(self.tabWidgetPage2)
        self.labelPic2.setObjectName(u"labelPic2")

        self.verticalLayout_5.addWidget(self.labelPic2)

        self.verticalLayout_5.setStretch(0, 1)
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.tabWidgetPage3 = QWidget()
        self.tabWidgetPage3.setObjectName(u"tabWidgetPage3")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidgetPage3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelPic3 = QLabel(self.tabWidgetPage3)
        self.labelPic3.setObjectName(u"labelPic3")

        self.verticalLayout_3.addWidget(self.labelPic3)

        self.verticalLayout_3.setStretch(0, 1)
        self.tabWidget.addTab(self.tabWidgetPage3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.InfoLabel.setText("")
        self.labelPic1.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("Dialog", u"1", None))
        self.labelPic2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("Dialog", u"2", None))
        self.labelPic3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage3), QCoreApplication.translate("Dialog", u"3", None))
    # retranslateUi

