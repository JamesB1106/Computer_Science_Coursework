#import and initialise
import tkinter as tk
from tkinter import ttk
import Logintkwindowv1 as login
import Signuptkwindowv1 as signUp
root = tk.Tk()
#dimensions and attributes
window_height = 500
window_width = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
centre_x = int(screen_width/2 - window_width/2)
centre_y = int(screen_height/2 - window_height/2)
root.geometry('750x500+50+50')
root.title('Login or Signup')
root.iconbitmap('padlock.ico')
root.resizable(False,False)
#main code    
ttk.Button(root, text="Login", command = lambda: login.loginScreen()).pack()
ttk.Button(root, text="Sign up", command = lambda: signUp.signUpScreen()).pack()
root.mainloop()
