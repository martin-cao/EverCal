# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eventMonthView.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(12, 13, 193, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_eventMonthView_calendarLabel = QLabel(self.widget)
        self.label_eventMonthView_calendarLabel.setObjectName(u"label_eventMonthView_calendarLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_eventMonthView_calendarLabel.sizePolicy().hasHeightForWidth())
        self.label_eventMonthView_calendarLabel.setSizePolicy(sizePolicy)
        self.label_eventMonthView_calendarLabel.setMinimumSize(QSize(4, 12))
        self.label_eventMonthView_calendarLabel.setMaximumSize(QSize(4, 12))
        self.label_eventMonthView_calendarLabel.setAutoFillBackground(True)
        self.label_eventMonthView_calendarLabel.setStyleSheet(u"background-color: {green}; corner-radius: {6px};")
        self.label_eventMonthView_calendarLabel.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_eventMonthView_calendarLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_eventMonthView_eventTitle = QLabel(self.widget)
        self.label_eventMonthView_eventTitle.setObjectName(u"label_eventMonthView_eventTitle")
        sizePolicy.setHeightForWidth(self.label_eventMonthView_eventTitle.sizePolicy().hasHeightForWidth())
        self.label_eventMonthView_eventTitle.setSizePolicy(sizePolicy)
        self.label_eventMonthView_eventTitle.setMinimumSize(QSize(0, 16))
        self.label_eventMonthView_eventTitle.setMaximumSize(QSize(600, 16))

        self.horizontalLayout.addWidget(self.label_eventMonthView_eventTitle)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_eventMonthView_time = QLabel(self.widget)
        self.label_eventMonthView_time.setObjectName(u"label_eventMonthView_time")
        sizePolicy.setHeightForWidth(self.label_eventMonthView_time.sizePolicy().hasHeightForWidth())
        self.label_eventMonthView_time.setSizePolicy(sizePolicy)
        self.label_eventMonthView_time.setMinimumSize(QSize(28, 16))
        self.label_eventMonthView_time.setMaximumSize(QSize(56, 16))

        self.horizontalLayout.addWidget(self.label_eventMonthView_time)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_eventMonthView_eventTitle.setText(QCoreApplication.translate("Form", u"EventTitle", None))
        self.label_eventMonthView_time.setText(QCoreApplication.translate("Form", u"12:00 AM", None))
    # retranslateUi

