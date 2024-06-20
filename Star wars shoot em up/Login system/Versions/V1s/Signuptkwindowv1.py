def signUpScreen():
    #import and initialise
    import tkinter as tk
    from tkinter import ttk
    import random as r
    root = tk.Tk()
    firstname = tk.StringVar()
    surname = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()
    pwordCheck = tk.StringVar()
    securityQ = tk.StringVar()
    securityA = tk.StringVar()
    def signUpWindow(root):
        #dimensions and attributes
        window_height = 500
        window_width = 750
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        centre_x = int(screen_width/2 - window_width/2)
        centre_y = int(screen_height/2 - window_height/2)
        root.geometry('750x500+50+50')
        root.title('Sign-up')
        root.attributes('-topmost',1)
        root.iconbitmap('padlock.ico')
        root.resizable(False,False)
        #widgets
        ttk.Label(root, text = 'Enter your First name').pack()
        ttk.Entry(root, textvariable = firstname).pack()
        ttk.Label(root, text = 'Enter your Surname').pack()
        ttk.Entry(root, textvariable=surname).pack()
        ttk.Label(root, text = 'Enter your Password').pack()
        ttk.Entry(root, textvariable = password, show = '*').pack()
        ttk.Label(root, text = 'Enter your Password again').pack()
        ttk.Entry(root, textvariable = pwordCheck, show = '*').pack()
        ttk.Label(root, text = 'Enter your Security Question').pack()
        ttk.Entry(root, textvariable = securityQ).pack()
        ttk.Label(root, text = 'Enter the answer to your security question').pack()
        ttk.Entry(root, textvariable = securityA).pack()
        ttk.Button(root,text = 'Check password',command = lambda: pwordCheck(root)).pack()
        def saveDetails(root):
            fname = firstname.get()
            fname = str(fname)
            sname = surname.get()
            sname = str(sname)
            pword = password.get()
            pword = str(pword)
            secureQ = securityQ.get()
            secureQ = str(secureQ)
            secureA = securityA.get()
            secureA = str(secureA)
            username = sname + fname[0] + '0' + str(r.randint(0,9))
            with open("dbClient.txt", "w") as my_db:
                my_db.write(f'{fname},{sname},{username},{pword},{secureQ},{secureA},\n')
        def pwordCheck(root):
            while password != pwordCheck:
                ttk.Label(root, text = 'Passwords do not match').pack()
            else:
                ttk.Button(root, text = 'Enter Details', command = lambda: saveDetails(root)).pack()
                
            ttk.Label(root, text = ('Your username is', username))
    signUpWindow(root)
    root.mainloop()
