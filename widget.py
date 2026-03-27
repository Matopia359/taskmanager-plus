from PySide6.QtWidgets import QWidget
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)