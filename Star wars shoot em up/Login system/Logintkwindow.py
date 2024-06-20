import tkinter as tk
from tkinter import ttk
import Signuptkwindow as _signup
from User import Player
class login():
    #Constructors
    def __init__(self, root = "root", usname = "", paword = ""):
        self.root = tk.Tk()
        self.usname = usname
        self.paword = paword
        self.getPlayers("dbClient.txt", usname, paword)
    #methods
    def getPlayers(self, file, usname, paword):
        with open (file, 'r+') as file:
            playerList = []
            lines = file.readlines()
            for line in lines:
                newPlayer = Player()
                temp1 = line.rstrip() # gets rid of eol characters
                if len(temp1) > 0:
                    temp = temp1.rsplit(",")
                    newPlayer.set_username(temp[2])
                    newPlayer.set_password(temp[3])
                    newPlayer.set_question(temp[4])
                    newPlayer.set_answer(temp[5])
                    newPlayer.set_score(temp[6])
                    newPlayer.set_level(temp[7])
                    playerList.append(newPlayer)
                # add score and level when link with game
            for p in playerList:
                print(p)
        file.close()
        self.sortList(playerList, usname, paword)
    def sortList(self,playerList, usname, paword):
        for n in range(len(playerList)):
            item = playerList[n]
            i = n-1
            while i>=0 and item < playerList[i]:
                playerList[i+1] = playerList[i]
                i -= 1
            playerList[i+1] = item
        for p in playerList:
            print(p)
        self.newLoginWindow(self.root, usname, paword, playerList)
    def newLoginWindow(self,root, usname, paword, playerList):
        root.geometry("750x500+50+50")
        root.title("Login")
        root.iconbitmap("padlock.ico")
        self.loginScreen(root, usname, paword, playerList)
    def loginScreen(self, root, usname, paword,playerList):
        ttk.Label(root, text = "Enter your username").pack()
        username = ttk.Entry(root)
        username.pack()
        ttk.Label(root, text = "Enter your password").pack()
        password = ttk.Entry(root, show = "*")
        password.pack()
        ttk.Button(root, text = "Login", command= lambda: self.checkUsname(username.get(), playerList)).pack()
    def checkUsname(self, usname, playerList):
        if self.search(usname, playerList) == True:
            print ("Username found")
        else:
            print ("Username not found")
    def search(self,item,playerList):
        found = False
        first = 0
        last = len(playerList)
        while first <= last and found == False:
            mid = (first + last)//2
            if item == playerList[mid]:
                found = True
            elif item > playerList[mid]:
                first = mid + 1
            else:
                last = mid - 1
        return found
login()

