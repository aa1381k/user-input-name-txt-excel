from xlwt import Workbook
from threading import Thread
import datetime
import os 
# create excel file
xlsx_file = Workbook()
sheet = xlsx_file.add_sheet("sheet1")
#delete file
if os.path.exists("user input.txt"):
    os.remove("user input.txt")

if os.path.exists("user input.xls"):
    os.remove("user input.xls")
#time function
def time():
    now = datetime.datetime.today()
    return now
#write txt file
class txt_files(Thread):
    def run(self):
        txt_file = open("user input.txt","a")
        txt_file.write((user_input+"\n"+str(time())+"\n"))
#write excel file
class xlsx_files(Thread):
    def run(self):
        sheet.write(i,0,user_input)
        sheet.write(i,1,str(time()))
#user input name       
for i in range(2):
    user_input = input("enter your name: ")
    txt_files2 = txt_files()
    xlsx_files2 = xlsx_files()
    txt_files2.start()
    xlsx_files2.start()
xlsx_file.save("user input.xls")