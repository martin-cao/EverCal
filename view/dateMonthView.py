# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dateMonthView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(582, 556)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_dateMonthView_date = QLabel(Form)
        self.label_dateMonthView_date.setObjectName(u"label_dateMonthView_date")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dateMonthView_date.sizePolicy().hasHeightForWidth())
        self.label_dateMonthView_date.setSizePolicy(sizePolicy)
        self.label_dateMonthView_date.setMinimumSize(QSize(31, 16))
        self.label_dateMonthView_date.setMaximumSize(QSize(31, 16))

        self.horizontalLayout.addWidget(self.label_dateMonthView_date)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_dateMonthView = QVBoxLayout()
        self.verticalLayout_dateMonthView.setObjectName(u"verticalLayout_dateMonthView")
        self.verticalLayout_dateMonthView.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        self.verticalLayout.addLayout(self.verticalLayout_dateMonthView)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_dateMonthView_date.setText(QCoreApplication.translate("Form", u"Date", None))
    # retranslateUi

