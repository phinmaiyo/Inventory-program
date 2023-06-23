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

    elif (userInput == 2):                                             # adds new student
        newstud = input("Please Enter the student name : ").lower()
        stud_age = int(input("Please Enter student age : "))
        stud_GPA = int(input("Please Enter student GPA : "))
        stud_hobby = input("Please Enter student hobby : ")
        if newstud in dictstd:
            print(f"\n This student {newstud} already in inventory")
        else:
            dictstd[newstud] = {"Age": stud_age, "GPA": stud_GPA, "Hobby": stud_hobby}
            print(f"\n This student {newstud} added successfully")

    elif (userInput == 3):                                              # finds a specific student in the inventory
        srcStud = input("Please enter the student name to search: ").lower()
        if srcStud in dictstd:
            print(f"\n Student Record Found {srcStud}{dictstd[srcStud]}") 
        else:
            print(f"\n Student Record not Found {srcStud}")

    elif (userInput == 4):                                               # removes a students record
        rmStud = input("Please Enter Student Name to Remove: ").lower()
        if rmStud in dictstd:
            prompt = input(f"Are you sure you want to delete {rmStud}'s inventory? yes or no :'").lower()
            if prompt == yes:
                dictstd.pop(rmStud)
                print(f"\n {rmStud} record deleted")
            for student in dictstud:
                print(f"\n {student}")
    else:
        print(f" No Record of student by name {rmStud} Found in inventory")


