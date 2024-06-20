class Stack():

    def __init__(self):
    # initialise the class
        self.theStack = []
        self.counter = -1
    def push(self, item, file):
    #function to push(append) an item to the stack
        self.counter += 1
        self.theStack.append(item)
        

    def pop(self):
    #function to return a reversal of the stack
        if self.counter == -1:
            pass
        else:
            self.counter -= 1
            return self.theStack[(self.counter+1)]

class fileChanger():
    def __init__(self, file = ""):
        self.file = file       

    def encryptAfile(self,file):
        #creates an instance of stack
        stack = Stack()
        with open (file,"r") as f:
        # opens the file to read and reads in lines and characters
            lines = f.readlines()
            for line in lines:
        # converts characters to ascii, takes away 10 and then converts back to character
                for i in line:
                    char = ord(i)-10
        # stop getting non character values
                    if char == 22:
                        char = 125
                    if char != 22 and char < 33:
                        numb = 33 - char
                        char = 126 - numb
                    stack.push(chr(char), file)
        string = stack.theStack
        self.saveFile(string, file)

    def decryptAfile(self, file):
        stack = Stack()
        with open (file,"r") as f:
            lines = f.readlines()
            for line in lines:
                for i in line:
                    char = ord(i)+10
                    if char == 135:
                        char = 32
                    elif char !=135 and char > 126:
                        numb = 126 - char
                        char = 33 - numb 
                    stack.push(chr(char), file)
        string = stack.theStack
        self.saveFile(string, file)

    def saveFile(self,data,file):
        stack = Stack()
        string = "".join(str(f) for f in data)              
        with open (file,"w") as ff:
            ff.write(string)
            ff.close()        
fileChanger = fileChanger()
#fileChanger.encryptAfile('Hellos.txt')
fileChanger.decryptAfile('Hellos.txt')
