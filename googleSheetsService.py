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

