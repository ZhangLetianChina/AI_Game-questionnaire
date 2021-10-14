
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random
import xlrd
import tkinter.messagebox
import pandas

Question_Excel = xlrd.open_workbook("Question list V1.xlsx")

#all the data collected
Questions_List = []
Left_Instruction_List = []
Mid_Instruction_List = []
Right_Instruction_List = []


Question_Table = Question_Excel.sheets()[0]
max_year = Question_Table.nrows

for i in range(1,Question_Table.nrows):
    k = Question_Table.row_values(i)
    Questions_List.append(k[0])
    Left_Instruction_List.append(k[1])
    Mid_Instruction_List.append(k[2])
    Right_Instruction_List.append(k[3])


window = tk.Tk()
window.title("Future Company")
window.geometry("1000x600")
window.resizable(False,False)
amount_money = 0

#bd is the boarder width
cv = tk.Canvas(window,height = 600, width = 1000, bd = 0, highlightthickness=0)

#Add background image
im_path = "./background.jpg"
imge = Image.open(im_path).resize((1000,700))

background = ImageTk.PhotoImage(imge)
cv.create_image(500,300, image = background)
cv.pack()
choice = []
Question_Number = 0

Question_Instruction = Questions_List[Question_Number]
Year_Instruction = "您目前处于第2020年"
Money_Insruction = "您的金币数量为：0"
Left_Instruction = Left_Instruction_List[Question_Number]
Mid_Instruction = Mid_Instruction_List[Question_Number]
Right_Instruction = Right_Instruction_List[Question_Number]


def Left1_Choose():
    global Question_Number
    choice.append(1)
    global amount_money
    amount_money += int(500*(random.random())-150)
    global Question_Instruction, Year_Instruction, Money_Insruction, Left_Instruction, Mid_Instruction, Right_Instruction

    Question_Number += 1


    Question_Presentation["text"]=Questions_List[Question_Number]
    Year_Presentation["text"]="您目前处于第" + str(2020 + Question_Number) + "年"
    Money_Presentation["text"]="您的金币数量为：" + str(amount_money)
    Left_Instruction_Presentation["text"]=Left_Instruction_List[Question_Number]
    Right_Instruction_Presentation["text"]=Mid_Instruction_List[Question_Number]
    Mid_Instruction_Presentation["text"]=Right_Instruction_List[Question_Number]

    print(Left_Instruction_List[Question_Number])



Question_Presentation = tk.Label(text = Questions_List[Question_Number],wraplength = 180,font=("Purisa",25),fg="black", bg="white")
Question_Presentation.pack()
cv.create_window(500,100,width = 250, height = 120, window = Question_Presentation)

Year_Presentation = tk.Label(text = "您目前处于第2020年",wraplength = 150,font=("Purisa",25),fg="black", bg="white")
Year_Presentation.pack()
cv.create_window(800,50,width = 150, height = 20, window = Year_Presentation)

Money_Presentation = tk.Label(text = "您的金币数量为：0",wraplength = 150,font=("Purisa",25),fg="black", bg="white")
Money_Presentation.pack()
cv.create_window(800,150,width = 150, height = 20, window = Money_Presentation)

Left_Instruction_Presentation = tk.Label(text = Left_Instruction_List[Question_Number], wraplength = 1000,font=("Purisa",25),fg="green", bg="white")
Left_Instruction_Presentation.pack()
cv.create_window(100,370,width = 300, height = 100, window = Left_Instruction_Presentation)

Mid_Instruction_Presentation = tk.Label(text = Mid_Instruction_List[Question_Number], wraplength = 100,font=("Purisa",25),fg="gray", bg="white")
Mid_Instruction_Presentation.pack()
cv.create_window(490,370,width = 300, height = 100, window = Mid_Instruction_Presentation)

Right_Instruction_Presentation = tk.Label(text = Right_Instruction_List[Question_Number], wraplength = 100,font=("Purisa",25),fg="Purple", bg="white")
Right_Instruction_Presentation.pack()
cv.create_window(900,370,width = 300, height = 100, window = Right_Instruction_Presentation)




green_photo_path = "./Green.png"
gray_photo_path = "./Gray.png"
purple_photo_path = "./Purple.png"


#change the command
Left1_img = Image.open(green_photo_path).resize((100,100))
Left1_dis = ImageTk.PhotoImage(Left1_img)
Left1_Button = tk.Button(image=Left1_dis, command = Left1_Choose)
Left1_Button.pack()
cv.create_window(100,450,width = 100, height = 100, window = Left1_Button)

Left2_img = Image.open(green_photo_path).resize((80,80))
Left2_dis = ImageTk.PhotoImage(Left2_img)
Left2_Button = tk.Button(image=Left2_dis, command = Left1_Choose)
Left2_Button.pack()
cv.create_window(250,450,width = 80, height = 80, window = Left2_Button)

Left3_img = Image.open(green_photo_path).resize((60,60))
Left3_dis = ImageTk.PhotoImage(Left3_img)
Left3_Button = tk.Button(image=Left3_dis, command = Left1_Choose)
Left3_Button.pack()
cv.create_window(380,450,width = 60, height = 60, window = Left3_Button)

Mid_img = Image.open(gray_photo_path).resize((40,40))
Mid_dis = ImageTk.PhotoImage(Mid_img)
Mid_Button = tk.Button(image=Mid_dis, command = Left1_Choose)
Mid_Button.pack()
cv.create_window(490,450,width = 40, height = 40, window = Mid_Button)

Right3_img = Image.open(purple_photo_path).resize((60,60))
Right3_dis = ImageTk.PhotoImage(Right3_img)
Right3_Button = tk.Button(image=Right3_dis, command = Left1_Choose)
Right3_Button.pack()
cv.create_window(600,450,width = 60, height = 60, window = Right3_Button)

Right2_img = Image.open(purple_photo_path).resize((80,80))
Right2_dis = ImageTk.PhotoImage(Right2_img)
Right2_Button = tk.Button(image=Right2_dis, command = Left1_Choose)
Right2_Button.pack()
cv.create_window(750,450,width = 80, height = 80, window = Right2_Button)

Right1_img = Image.open(purple_photo_path).resize((100,100))
Right1_dis = ImageTk.PhotoImage(Right1_img)
Right1_Button = tk.Button(image=Right1_dis, command = Left1_Choose)
Right1_Button.pack()
cv.create_window(900,450,width = 100, height = 100, window = Right1_Button)


#Add the canvas into the main window
window.mainloop()
#print(Question_Number)


