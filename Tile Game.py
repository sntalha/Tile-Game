from tkinter import *
import random

# Creating Window
main=Tk()
main.title("Tile Match")
main.geometry("460x570")

# Creating matches
nums=[1,1,2,2,3,3,4,4,5,5,6,6]
# Shuffling matches
random.shuffle(nums)

# Defining variables
count=0
ans_list=[]
ans_dict={}
win=0

# Function for win
def winner():
    l1.config(text="Congratulations! You WON!!!")
    rb = Button(main,text="Reset Game?",bg="Black",fg="White",font=("Georgina,10"),relief="groove",command=reset)
    rb.pack(pady=10)
    qb=Button(main,text="Quit Game",bg="Black",fg="White",font=("Georgina,10"),relief="groove",command=main.quit)
    qb.pack(pady=20)

# Reset Function
def reset():
    global win,nums
    win=0
    nums=[1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(nums)
    l1.config(text="")
    blist=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11]
    for i in blist:
        i.config(text=' ',state="normal",relief="groove")

# Function for buttons
def shuffle(b,n):
    global count,ans_list,ans_dict,win
    if b["text"]==' ' and count<2:
        b["text"]=nums[n]
        ans_list.append(n)
        ans_dict[b]=nums[n]
        count+=1
    if len(ans_list) == 2:
        if nums[ans_list[0]]==nums[ans_list[1]]:
            l1.config(text="MATCH")
            for key in ans_dict:
                key["state"]="disabled"
                key["relief"]="sunken"
            count=0
            ans_list=[]
            ans_dict={}
            win+=1
            if win==6:
                winner()
        else:
            l1.config(text="Failed")
            count=0
            ans_list=[]
            for key in ans_dict:
                key["text"]=' '
            ans_dict={}

# Creating frame
f1=Frame(main,bg="Black")
f1.pack(pady=10)

# Creating buttons
b0=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b0,0),relief="groove")
b1=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b1,1),relief="groove")
b2=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b2,2),relief="groove")
b3=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b3,3),relief="groove")
b4=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b4,4),relief="groove")
b5=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b5,5),relief="groove")
b6=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b6,6),relief="groove")
b7=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b7,7),relief="groove")
b8=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b8,8),relief="groove")
b9=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b9,9),relief="groove")
b10=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b10,10),relief="groove")
b11=Button(f1,text=' ',bg="Red",font=("Georgia",20),height=3,width=6,command=lambda: shuffle(b11,11),relief="groove")

# Gridding Buttons
b0.grid(row=0,column=0)
b1.grid(row=0,column=1)
b2.grid(row=0,column=2)
b3.grid(row=0,column=3)
b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)
b7.grid(row=1,column=3)
b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
b10.grid(row=2,column=2)
b11.grid(row=2,column=3)

l1=Label(main,text="",font=("Georgia",20))
l1.pack(pady=20)

main.mainloop()


