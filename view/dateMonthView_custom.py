from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from view.dateMonthView import Ui_Form

class CustomDateMonthView(QWidget):
    def __init__(self, parent=None):
        super(CustomDateMonthView, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

    def add_event(self, event_text):
        loader = QUiLoader()
        file = QFile("./eventMonthView.ui")
        file.open(QFile.ReadOnly)
        event_widget = loader.load(file, self)
        file.close()

        # Assuming the QLabel in eventView.ui has the objectName "label_event"
        event_label = event_widget.findChild(QLabel, "label_event")
        event_label.setText(event_text)

        event_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout.addWidget(event_widget)