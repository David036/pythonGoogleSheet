import gspread

gc = gspread.service_account()
sheet = gc.open("UsersTests")

wks = sheet.worksheet("Sheet1")