from Models.LoginModel import LoginDao


class LoginController:
    def __init__(self):
        self.DAO = LoginDao()
    

    def Verification(self,username,password):
        data = self.DAO.Verification(username,password)
        if(data is None):
            return False
        else:
            return True

