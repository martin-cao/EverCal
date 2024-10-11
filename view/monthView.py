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
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_monthView(object):
    def setupUi(self, monthView):
        if not monthView.objectName():
            monthView.setObjectName(u"monthView")
        monthView.resize(771, 536)
        self.gridLayout_2 = QGridLayout(monthView)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_monthView_day_0 = QLabel(monthView)
        self.label_monthView_day_0.setObjectName(u"label_monthView_day_0")

        self.horizontalLayout_3.addWidget(self.label_monthView_day_0)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_monthView_day_1 = QLabel(monthView)
        self.label_monthView_day_1.setObjectName(u"label_monthView_day_1")

        self.horizontalLayout_4.addWidget(self.label_monthView_day_1)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_monthView_day_2 = QLabel(monthView)
        self.label_monthView_day_2.setObjectName(u"label_monthView_day_2")

        self.horizontalLayout_6.addWidget(self.label_monthView_day_2)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.label_monthView_day_3 = QLabel(monthView)
        self.label_monthView_day_3.setObjectName(u"label_monthView_day_3")

        self.horizontalLayout_5.addWidget(self.label_monthView_day_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 3, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.label_monthView_day_4 = QLabel(monthView)
        self.label_monthView_day_4.setObjectName(u"label_monthView_day_4")

        self.horizontalLayout_8.addWidget(self.label_monthView_day_4)


        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 4, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.label_monthView_day_5 = QLabel(monthView)
        self.label_monthView_day_5.setObjectName(u"label_monthView_day_5")

        self.horizontalLayout_7.addWidget(self.label_monthView_day_5)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 5, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.label_monthView_day_6 = QLabel(monthView)
        self.label_monthView_day_6.setObjectName(u"label_monthView_day_6")

        self.horizontalLayout_9.addWidget(self.label_monthView_day_6)


        self.gridLayout.addLayout(self.horizontalLayout_9, 0, 6, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_monthView_calendarGrid = QGridLayout()
        self.gridLayout_monthView_calendarGrid.setSpacing(0)
        self.gridLayout_monthView_calendarGrid.setObjectName(u"gridLayout_monthView_calendarGrid")

        self.gridLayout_2.addLayout(self.gridLayout_monthView_calendarGrid, 2, 0, 1, 1)


        self.retranslateUi(monthView)

        QMetaObject.connectSlotsByName(monthView)
    # setupUi

    def retranslateUi(self, monthView):
        monthView.setWindowTitle(QCoreApplication.translate("monthView", u"Form", None))
        self.label_monthView_header.setText(QCoreApplication.translate("monthView", u"**September** 2024", None))
        self.pushButton_monthView_header_previous.setText("")
        self.pushButton_monthView_header_today.setText(QCoreApplication.translate("monthView", u"Today", None))
        self.pushButton_monthView_header_next.setText("")
        self.label_monthView_day_0.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
        self.label_monthView_day_1.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
        self.label_monthView_day_2.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
        self.label_monthView_day_3.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
        self.label_monthView_day_4.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
        self.label_monthView_day_5.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
        self.label_monthView_day_6.setText(QCoreApplication.translate("monthView", u"TextLabel", None))
    # retranslateUi

