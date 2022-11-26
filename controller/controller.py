class Controller:
    def __init__(self, view=None, model=None):
        self.view = view
        self.model = model
                
    def add_record(self, record):
        self.model.add_record(record)
        
    def change_record(self, record):
        self.model.change_record(record)
        
    def delete_record(self, record):
        self.model.delete_record(record)
        
    def show_recode(self, record):
        self.model.show_record(record)
        
    def login(self, username, password):
        return self.model.login(username, password)
    
    def change_account(self, account):
        self.model.change_account(account)
        
    def delete_account(self):
        self.account.delete()
        
    def leave_accout(self):
        self.account.leave()