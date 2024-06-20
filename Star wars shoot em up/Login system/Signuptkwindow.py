#import and initialise
import tkinter as tk
from tkinter import ttk
import random as r
import User 
class signUp():
    Player = User.Player()
    #Constructors
    def __init__(self, root = 'root', fname = "", sname = "", uname = "", pword = "", pwordChecker = "", secQ = "", secA = "", score = 0):
        self.fname = fname
        self.sname = sname
        self.uname = uname
        self.pword = pword
        self.pwordChecker = pwordChecker
        self.secQ = secQ
        self.secA = secA
        self.score = score
        self.root = tk.Tk()
        self.newUserWindow(self.root)
    #Build the tk window
    def newUserWindow(self, root):
        root.geometry('750x500+50+50')
        root.title('Sign-up')
        root.attributes('-topmost',1)
        root.iconbitmap('padlock.ico')
        self.newUserDetails(root)
        root.mainloop()
    #Take in the user details
    def newUserDetails(self, root):
        ttk.Label(root, text = "Enter your first name").pack()
        fname = ttk.Entry(root)
        fname.pack()
        
        ttk.Label(root, text = 'Enter your Surname').pack()
        sname = ttk.Entry(root)
        sname.pack()
        ttk.Label(root, text = 'Enter your Password').pack()
        pword = ttk.Entry(root, show = '*')
        pword.pack()
        ttk.Label(root, text = 'Enter your Password again').pack()
        pwordChecker = ttk.Entry(root, show = '*')
        pwordChecker.pack()
        
        ttk.Label(root, text = 'Enter your Security Question').pack()
        secQ = ttk.Entry(root)
        secQ.pack()
        
        ttk.Label(root, text = 'Enter the answer to your security question').pack()
        secA = ttk.Entry(root, show = '*')
        secA.pack()
        # set user details as their vairiables
        ttk.Button(root,text = 'Check password',command = lambda: self.pwordCheck(root,fname.get(),sname.get(),pword.get(),pwordChecker.get(),secQ.get(),secA.get())).pack()
        root.mainloop()
    # Check passwords match
    def pwordCheck(self,root, fname,sname,pword,pwordChecker,secQ,secA,score):
        if pword != pwordChecker:
            ttk.Label(root, text = 'Passwords do not match').pack()
        else:
            sname = str(sname)
            uname = str(fname) + sname[0] + "0" + str(r.randint(0,9))
            ttk.Label(root, text = ('Passwords Match, your username is: '+ str(uname))).pack()
            ttk.Button(root, text = 'Enter Details', command = lambda: Player.saveUser('dbClient.txt',fname,sname,uname,pword,secQ,secA,score)).pack()
            root.mainloop()
