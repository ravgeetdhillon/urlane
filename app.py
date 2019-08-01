#library files
import numpy as np
from tkinter import *
import tkinter as tk
import cv2

def refresh():
    global n
    n+=1

#main function
n=1
while n<=5:
#process the image -> matrix-> file
    img_name='case'+str(n)+'.png'
    img=cv2.imread(img_name,0)
    image_height=np.size(img,0)
    image_width=np.size(img,1)
    cols=5
    rows=20
    cell_height=image_height//rows
    cell_width=image_width//cols
    i,j=0,0
    file=open('data.txt','w+')
    while(i<rows):
        while(j<cols):
            if img[(cell_height*i)+(cell_height//2),(cell_width*j)+(cell_width//2)]<50:
                file.write('1')
            else:
                file.write('0')
            j+=1
        file.write('\n')    
        j=0
        i+=1
    file.close()

#calculate the cars in each lane
    file=open('data.txt','r+')
    total_queue=len(file.readline())-1
    situation=[]
    for i in range(total_queue):
        situation.append(0)
    file.seek(0,0)
    count=0
    while True:
        while count<total_queue:
            car=file.read(1)
            if car=='1':
                situation[count]+=1
            elif car=='0':
                pass
            count+=1
        r=file.readline()
        if r=='':
            break
        count=0
    file.close()

#calculate the lane number with the least cars
    index=0
    i=0
    least=situation[0]
    while(i<total_queue-1):
        if least>situation[i+1]:
            least=situation[i+1]
            index=i+1
        i+=1
    queue_no=index+1

#front end display
    app=Tk()
    app.title('URLANE - Super RackX')
    f=Frame(app,width=250,height=285)
    f.grid(row=0,column=0,sticky="NW")

    queuelabel=Label(f,text="URLANE",fg="#f49842",font='100')
    queuelabel.place(x=125,y=20,anchor="center")

    queuelabel=Label(f,text="LANE 1   :")
    queuelabel.place(x=60,y=55,anchor="center")


    queuelabel=Label(f,text="LANE 2   :")
    queuelabel.place(x=60,y=80,anchor="center")


    queuelabel=Label(f,text="LANE 3   :")
    queuelabel.place(x=60,y=105,anchor="center")


    queuelabel=Label(f,text="LANE 4   :")
    queuelabel.place(x=60,y=130,anchor="center")

    queuelabel=Label(f,text="LANE 5   :")
    queuelabel.place(x=60,y=155,anchor="center")

    carlabel=Label(f,text=str(situation[0])+' car/s')
    carlabel.place(x=130,y=55,anchor="center")


    carlabel=Label(f,text=str(situation[1])+' car/s')
    carlabel.place(x=130,y=80,anchor="center")


    carlabel=Label(f,text=str(situation[2])+' car/s')
    carlabel.place(x=130,y=105,anchor="center")


    carlabel=Label(f,text=str(situation[3])+' car/s')
    carlabel.place(x=130,y=130,anchor="center")

    carlabel=Label(f,text=str(situation[4])+' car/s')
    carlabel.place(x=130,y=155,anchor="center")

    resultlabel=Label(f,text="ENTER LANE NUMBER   :")
    resultlabel.place(x=108,y=200,anchor="center")

    resultlabel=Label(f,text=queue_no)
    resultlabel.place(x=220,y=200,anchor="center")

    b=Button(app, text="Refresh",command=app.destroy,bg="#47e028",borderwidth="0",highlightbackground="#a8abaf")
    b.place(x=75,y=250,anchor="center",width="80")

    b=Button(app, text="Exit",command=quit,bg="#fc2d2d",borderwidth="0",highlightbackground="#a8abaf")
    b.place(x=175,y=250,anchor="center",width="80")

    
    app.mainloop()
    n+=1
    if n>5:
        n=1
