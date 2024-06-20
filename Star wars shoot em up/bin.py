myArray = ["Amanda","Bobbie", "Charlie", "Daniel", "Ezra", "Frankie", "Gerald"]
item = input("What do you want to find")
def binSearch(array, item):
    global midpoint
    upperB = len(array)
    lowerB = 0
    midpoint = (upperB + lowerB) //2
    found = False
    stop = False
    count = 0
    while found == False and stop == False:
        if array[midpoint] == item:
            found = True
        elif array[midpoint] > item:
            upperB = midpoint - 1
            midpoint = (upperB + lowerB) //2
        elif array[midpoint] < item:
            lowerB = midpoint + 1
            midpoint = (upperB + lowerB) //2
        else:
            stop = True
        count += 1
        print("pass number",count)
    if found == True:
        return 'found'
    else:
        return 'not found'
print("The item was",binSearch(myArray,item),"at position", midpoint + 1)
