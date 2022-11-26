from model.user import User
from view.pyqtiu.ClangeAccountWindow import Ui_ChangeAccountScreenUI
from PyQt5.QtWidgets import QMainWindow


class ChangeAccountScreen(QMainWindow):
    user = User()
    
    def __init__(self):
        super(ChangeAccountScreen, self).__init__()
        self.ui = Ui_ChangeAccountScreenUI(self)
    
    def open_user_screen(self, user):
        self.user_screen.open(user)