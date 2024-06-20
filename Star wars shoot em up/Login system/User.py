class Player():
    def __init__(self, username = "", password = "", secQ = "", secA = "", score = 0,level = 0):

        self.username = username
        self.password = password
        self.secQ = secQ
        self.secA = secA
        self.score = score
        self.level = level
#accessors
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_secQ(self):
        return self.secQ
    def get_secA(self):
        return self.secA
    def get_score(self):
        return self.score
    def get_level(self):
        return self.level
#modifiers
    def set_username(self,newUsername):
        self.username = newUsername
    def set_password(self,newPassword):
        self.password = newPassword
    def set_question(self,newQ):
        self.secQ = newQ
    def set_answer(self,newA):
        self.secA = newA
    def set_score(self,newScore):
        self.score = newScore
    def set_level(self,newLevel):
        self.level = newLevel
#To read client details
    def readUser(self,file):
        x = ['']
        with open(file, "r") as my_db:
            lines = my_db.readlines()
            for line in lines:
                x.append(line)
        return x
    def saveUser(self,file,fname,sname,uname,pword,secQ,secA,score):
        x = self.readUser(file)
        toAppend = f'{fname},{sname},{uname},{pword},{secQ},{secA},{score}'
        x.append(toAppend)
        with open(file, "w") as my_db:
            for item in x:
                my_db.write(item)
                
    def __str__(self):
        return (self.username + " " +  self.password + " " +  self.secQ + " " + self.secA + " " + self.score + " " + self.level)
    # Overwrite greater than function 
    def __gt__(self, arg):
        if arg.get_score() > self.score:
            return True
        else:
            return False
    def __lt__(self, arg):
        if arg.get_score() < self.score:
            return True
        else:
            return False
    def __eq__(self, arg):
        if arg.get_score() == self.score:
            return True
        else:
            return False
        
