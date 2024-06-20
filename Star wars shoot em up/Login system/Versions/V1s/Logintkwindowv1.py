def loginScreen():
    #import and initialise
    import tkinter as tk
    from tkinter import ttk
    root = tk.Tk()
    username =tk.StringVar()
    password =tk.StringVar()
    def loginWindow(root):
        #dimensions and attributes
        window_height = 500
        window_width = 750
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        centre_x = int(screen_width/2 - window_width/2)
        centre_y = int(screen_height/2 - window_height/2)
        root.geometry('750x500+50+50')
        root.title('Login')
        root.attributes('-topmost',1)
        root.iconbitmap('padlock.ico')
        root.resizable(False,False)
        ttk.Label(root, text = 'Enter your username').grid()
        ttk.Entry(root, textvariable=username).grid()
        ttk.Label(root, text = 'Enter your password').grid()
        ttk.Entry(root, textvariable=password, show = '*').grid()
        ttk.Button(root, text = 'Login', command= lambda: loginCheck(root)).grid()
        root.mainloop()
    def loginCheck(root):
        # Checks username and password against database
        with open("dbClient.txt", "r") as my_db:
            for line in my_db:
                pass
    loginWindow(root)
