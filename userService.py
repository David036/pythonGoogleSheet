from googleSheetsService import Person as Person, wks as wks

def create_user():
    name = input("Enter your First Name:")
    lastName = input("Enter your Last Name:")
    age = int(input("Enter your age:"))
    height = int(input("Enter your height:"))
    weight = int(input("Enter your weight:"))
    user = Person(name,lastName,age,height,weight)
    wks.append_row([user.name,user.lastName,user.age,user.height,user.weight])