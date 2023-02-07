class String:
    def __init__(self, inp):
        self.inp = inp
    def read(self):
        print("Your name is " + self.inp)
inputt = String(input())
inputt.read()