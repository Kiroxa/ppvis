from model.user import User


class BudgetManager:
    user = User()
    
    def login(self, username, password):
        return self.user.login(username, password)
    
    def change_account(self, changes):
        self.user.change_account(changes)
        
    def leave_account(self):
        self.user.leave_account()
        
    def delete_account(self):
        self.user.delete_account()
