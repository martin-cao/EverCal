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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(582, 556)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_dateMonthView = QVBoxLayout()
        self.verticalLayout_dateMonthView.setSpacing(0)
        self.verticalLayout_dateMonthView.setObjectName(u"verticalLayout_dateMonthView")
        self.verticalLayout_dateMonthView.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)

        self.gridLayout.addLayout(self.verticalLayout_dateMonthView, 1, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(509, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label_dateMonthView_date = QLabel(Form)
        self.label_dateMonthView_date.setObjectName(u"label_dateMonthView_date")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dateMonthView_date.sizePolicy().hasHeightForWidth())
        self.label_dateMonthView_date.setSizePolicy(sizePolicy)
        self.label_dateMonthView_date.setMinimumSize(QSize(36, 16))
        self.label_dateMonthView_date.setMaximumSize(QSize(36, 16))
        self.label_dateMonthView_date.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout.addWidget(self.label_dateMonthView_date, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_dateMonthView_date.setText(QCoreApplication.translate("Form", u"Date", None))
    # retranslateUi

