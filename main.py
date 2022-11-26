# XDG_SESSION_TYPE=x11

# pyqt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication

#MVP
from view.ui import UI

from model.record import Record
from model.budget_manager import BudgetManager
from controller.controller import Controller

# system
import sys


class App(QApplication):
    def __init__(self, *args):
        super().__init__(list(args))
        
        # view
        self.ui = UI()
        
        # model and controller
        self.create_model()
        self.create_controller()
        
        # init app
        self.ui.init_app()
    
    def create_model(self):
        self.record = Record()
        self.budget_manager = BudgetManager()
        
    def create_controller(self):
        self.controller = Controller(view=self.ui, model=self.budget_manager)
        

def start():
    app = App(sys.argv)
    app.setApplicationName("Family budget manager")
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    start()