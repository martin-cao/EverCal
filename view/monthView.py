# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monthView.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_monthView(object):
    def setupUi(self, monthView):
        if not monthView.objectName():
            monthView.setObjectName(u"monthView")
        monthView.resize(693, 428)
        self.verticalLayout = QVBoxLayout(monthView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_monthView_header = QLabel(monthView)
        self.label_monthView_header.setObjectName(u"label_monthView_header")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_monthView_header.sizePolicy().hasHeightForWidth())
        self.label_monthView_header.setSizePolicy(sizePolicy)
        self.label_monthView_header.setMinimumSize(QSize(192, 32))
        self.label_monthView_header.setMaximumSize(QSize(192, 32))
        font = QFont()
        font.setPointSize(24)
        self.label_monthView_header.setFont(font)
        self.label_monthView_header.setTextFormat(Qt.TextFormat.MarkdownText)
        self.label_monthView_header.setWordWrap(False)

        self.horizontalLayout_2.addWidget(self.label_monthView_header)

        self.horizontalSpacer = QSpacerItem(40, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_monthView_header_previous = QPushButton(monthView)
        self.pushButton_monthView_header_previous.setObjectName(u"pushButton_monthView_header_previous")
        sizePolicy.setHeightForWidth(self.pushButton_monthView_header_previous.sizePolicy().hasHeightForWidth())
        self.pushButton_monthView_header_previous.setSizePolicy(sizePolicy)
        self.pushButton_monthView_header_previous.setMinimumSize(QSize(32, 32))
        self.pushButton_monthView_header_previous.setMaximumSize(QSize(32, 32))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.pushButton_monthView_header_previous.setIcon(icon)

        self.horizontalLayout.addWidget(self.pushButton_monthView_header_previous)

        self.pushButton_monthView_header_today = QPushButton(monthView)
        self.pushButton_monthView_header_today.setObjectName(u"pushButton_monthView_header_today")
        sizePolicy.setHeightForWidth(self.pushButton_monthView_header_today.sizePolicy().hasHeightForWidth())
        self.pushButton_monthView_header_today.setSizePolicy(sizePolicy)
        self.pushButton_monthView_header_today.setMinimumSize(QSize(70, 32))
        self.pushButton_monthView_header_today.setMaximumSize(QSize(70, 32))

        self.horizontalLayout.addWidget(self.pushButton_monthView_header_today)

        self.pushButton_monthView_header_next = QPushButton(monthView)
        self.pushButton_monthView_header_next.setObjectName(u"pushButton_monthView_header_next")
        sizePolicy.setHeightForWidth(self.pushButton_monthView_header_next.sizePolicy().hasHeightForWidth())
        self.pushButton_monthView_header_next.setSizePolicy(sizePolicy)
        self.pushButton_monthView_header_next.setMinimumSize(QSize(32, 32))
        self.pushButton_monthView_header_next.setMaximumSize(QSize(32, 32))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.pushButton_monthView_header_next.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton_monthView_header_next)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_monthView_calendarGrid = QGridLayout()
        self.gridLayout_monthView_calendarGrid.setObjectName(u"gridLayout_monthView_calendarGrid")

        self.verticalLayout.addLayout(self.gridLayout_monthView_calendarGrid)


        self.retranslateUi(monthView)

        QMetaObject.connectSlotsByName(monthView)
    # setupUi

    def retranslateUi(self, monthView):
        monthView.setWindowTitle(QCoreApplication.translate("monthView", u"Form", None))
        self.label_monthView_header.setText(QCoreApplication.translate("monthView", u"**September** 2024", None))
        self.pushButton_monthView_header_previous.setText("")
        self.pushButton_monthView_header_today.setText(QCoreApplication.translate("monthView", u"Today", None))
        self.pushButton_monthView_header_next.setText("")
    # retranslateUi

