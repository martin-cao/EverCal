# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EverCal.ui'
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
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(865, 693)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridWidget = QWidget(self.centralwidget)
        self.gridWidget.setObjectName(u"gridWidget")
        self.gridLayout = QGridLayout(self.gridWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.gridWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_day = QWidget()
        self.tab_day.setObjectName(u"tab_day")
        self.gridLayout_5 = QGridLayout(self.tab_day)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.tab_day)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_day, "")
        self.tab_week = QWidget()
        self.tab_week.setObjectName(u"tab_week")
        self.gridLayout_3 = QGridLayout(self.tab_week)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.tab_week)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_week, "")
        self.tab_month = QWidget()
        self.tab_month.setObjectName(u"tab_month")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_month.sizePolicy().hasHeightForWidth())
        self.tab_month.setSizePolicy(sizePolicy)
        self.tab_month.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(self.tab_month)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_monthView = QGridLayout()
        self.gridLayout_monthView.setSpacing(0)
        self.gridLayout_monthView.setObjectName(u"gridLayout_monthView")
        self.gridLayout_monthView.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)

        self.gridLayout_2.addLayout(self.gridLayout_monthView, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_month, "")
        self.tab_year = QWidget()
        self.tab_year.setObjectName(u"tab_year")
        self.gridLayout_6 = QGridLayout(self.tab_year)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_3 = QLabel(self.tab_year)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_year, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.gridWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 865, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To be developed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_day), QCoreApplication.translate("MainWindow", u"Day", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"To be developed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_week), QCoreApplication.translate("MainWindow", u"Week", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_month), QCoreApplication.translate("MainWindow", u"Month", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"To be developed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_year), QCoreApplication.translate("MainWindow", u"Year", None))
    # retranslateUi

