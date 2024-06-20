import random as r
import tkinter as tk

root=tk.Tk()

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1000

SCREEN_HEIGHT = root.winfo_screenheight()
SCREEN_WIDTH = root.winfo_screenwidth()

SCREEN_CENTRE = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

class NewClient():
    #constructor
    def __init__(self,fname="",sname="",username="",pword="",question="",answer=""):
        self.fname = fname
        self.sname = sname
        self.username = username
        self.pword = pword
        self.question = question
        self.answer = answer
        self.saveClient()
    #modifiers
    def newFname(self):
        self.fname = input('Enter your first name')
        self.newSname()
    def newSname(self):
        self.sname = input('Enter your surname')
        self.newUsername()
    def newUsername(self):
        self.username = str(self.sname) + str(self.fname[0]) + str(r.randint(0,10))
        print("Your username is: " + str(self.username))
        self.newPword()
    def newPword(self):
        thepword = input('Enter your new password')
        verify = input('Re enter your password')
        if verify == thepword:
            self.pword = thepword
        else:
            print("Passwords do not match, start again!")
            self.newPword()            
        self.newQuestion()
    def newQuestion(self):
        self.question = input('Enter your new security question')
        self.newAnswer()
    def newAnswer(self):
        self.answer = input('Enter the answer to your security question')
    #Accessors
    def getFname(self):
        return  self.fname
    def getSname(self):
        return  self.sname
    def getUsername(self):
        return  self.username
    def getPword(self):
        return  self.pword
    def getQuestion(self):
        return  self.question
    def getAnswer(self):
        return  self.answer
    #Comparisons
    def __eq__(self, arg):
        return self.fname == arg.getfname() and self.sname == arg.getsname()
    def __lt__(self, arg):
        if self.sname == arg.getsname():
            return self.fname < arg.getfname()
        else:
            return self.sname < arg.getsname
    def __gt__(self, arg):
        if self.sname == arg.getsname():
            return self.fname > arg.getfname()
        else:
            return self.sname > arg.getsname
    #save 
    def saveClient(self):
        with open("dbClient.txt", "w") as my_db:
            my_db.write(f'{self.fname},{self.sname},{self.username},{self.pword},{self.question},{self.answer}+\n')
client = NewClient()
client.newFname()
client.saveClient()


