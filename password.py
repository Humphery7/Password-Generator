import random
import string

class Passwrd:
    letters = string.ascii_letters
    figs = string.digits

    # create attributes user chooses length of password, default = 8
    def __init__(self, length=8):
        self.length = length

    def form(self):
        if self.length >= 6:
            # join function joins elements from a sequence and returns a combine string
            words= ''.join(random.choice(self.letters) for i in range(self.length // 2))
            figures = ''.join(random.choice(self.figs) for i in range((self.length - (self.length // 2))))
            return words[2:]+figures[2:]+ words[0:2]+figures[0:2]
        else:
            print("minimum password length is 8")
            exit()

user = Passwrd(9)
users = user.form()
print(users)
