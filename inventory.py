import platform
import os

# global variable of an empty dict
global dictstd
dictstd={}

def student_inventory():                      # defines inventory function
    print('''
    Enter 1 : to view inventory
    Enter 2 : to add a new student
    Enter 3 : to search student
    Enter 4 : to delete student
    
    ''')
    

    userInput=int(input("please select an above option: "))            # takes in user option

    if (userInput == 1):                                               # this option prints out all student details
        print("Student Inventory\n ")
        for student,_inventory in dictstd.items():
            print("\n Student Name =>",student)
            for key in _inventory:
                print(key + ":", _inventory[key])

    