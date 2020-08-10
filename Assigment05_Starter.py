# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot, 1.2030, Created started script
# Hitakshi, 08.08.2020, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for strData in objFile:
    temp_list = strData.strip().split(",")
    dicRow = {"task": temp_list[0], "priority": temp_list[1]}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item. 
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Your current data is  ")
        print("Task | Priority")
        for item in lstTable:
            print(item["task"] + "|" + item["priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input("Please enter your task : ")
        while True:
            strPriority = input("Pick priority from the following: \"High\",\"Medium\" and \"Low :  ")
            if (strPriority.lower() == "high") | (strPriority.lower() == "medium") | (strPriority.lower() == "low"):
                break

        tempChoice = {"task": strTask, "priority": strPriority}
        lstTable.append(tempChoice)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        print("\nYour current data is  \n")
        print("\nTask | Priority")
        for item in lstTable:
            print(item["task"] + "|" + item["priority"])
        strDelete = input("\nPlease enter task you want to remove:  ")
        counter = 0
        initialTableLen = len(lstTable)
        for item in lstTable:
            if item["task"].lower() == strDelete.lower():
                lstTable.remove(item)
                print("Your task is removed.\n")
            else:
                counter = counter + 1
        if counter == initialTableLen:
            print("Task not found!!")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["task"] + "," + row["priority"] + "\n")
        objFile.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("You chose to exit.")
        break  # and Exit the program
