import pandas as pd
import gspread

gc = gspread.service_account()
sheet = gc.open("UsersTests")

wks = sheet.worksheet("Sheet1")

class Person:
    def __init__(self,name,lastName,age,height,weight):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.height = height
        self.weight = weight

def my_function():
    name = input("Enter your First Name:")
    lastName = input("Enter your Last Name:")
    age = int(input("Enter your age:"))
    height = int(input("Enter your height:"))
    weight = int(input("Enter your weight:"))
    wks.append_row([name,lastName,age,height,weight])

while 1:
    my_function()