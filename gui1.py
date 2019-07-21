# from tkinter import *
from Tkinter import *
import tkFileDialog
from tkFileDialog import askdirectory
from PIL import Image, ImageTk
import sys, os
import math
import pickle
import numpy as np
from smpl.hello_smpl import get_mesh
root = Tk()
from smpl.smpl_webuser.serialization import load_model

from hmr.demo1 import rerenders
m = load_model('smpl/models/basicmodel_m_lbs_10_207_0_v1.0.0.pkl')
root.title('Mesh GUI')
root.geometry('1024x1024')
bottomframe = Frame(root)
leftframe = Frame(root)
leftframe.pack(side= LEFT)
rightframe = Frame(root)
rightframe.pack(side= RIGHT)
bottomframe.pack(side=BOTTOM)
Posex = dict()
Posey = dict()
Posez = dict()
Beta = dict()
im_path =""
params_path = ""
for i in range(1,25):
    Posex[str(i)] = 0
    Posey[str(i)] = 0
    Posez[str(i)] = 0

for i in range(1, 11):
    Beta[str(i)] = 0

class scale:
    def __init__(self,master,text,n):
        frame = Frame(master)
        frame.pack(side=TOP)
        self.v = DoubleVar()
        self.v1 = IntVar()
        self.v2 = StringVar()
        self.v3 = StringVar()
        self.v4 = StringVar()
        self.s = Scale(frame,from_=-3.14159,to=3.14159,orient=HORIZONTAL,resolution=0.0001,length=170,width=4,variable=self.v)
        self.s.grid(row=n+1,column=1)
        self.l = Label(frame,text=text)
        self.l.grid(row=n+1,column=0)
        self.rx = Radiobutton(frame,text='x',value = 1,variable=self.v1)
        self.rx.grid(row=n+1,column=2)
        self.ry = Radiobutton(frame,text='y',value = 2,variable=self.v1)
        self.ry.grid(row=n+1,column=3)
        self.rz = Radiobutton(frame,text='z',value = 3,variable=self.v1)
        self.rz.grid(row=n+1,column=4)
        self.lx = Label(frame,textvariable=self.v2, font='TkFixedFont')
        self.lx.grid(row=n+1,column=6)
        self.ly = Label(frame,textvariable=self.v3)
        self.ly.grid(row=n+1,column=7)
        self.lz = Label(frame,textvariable=self.v4)
        self.lz.grid(row=n+1,column=8)


class scaleS:
    def __init__(self,master,text,n):
        frame = Frame(master)
        frame.pack(side=TOP)
        self.v = DoubleVar()
        self.s = Scale(frame,from_=-3.14159,to=3.14159,orient=HORIZONTAL,resolution=0.0001,length=170,width=4,variable=self.v)
        self.s.grid(row=n,column=2)
        self.l = Label(frame,text=text)
        self.l.grid(row=n,column=1)

class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 650, 650
        self.pack()
        self.file = Button(self, text='Browse', command=self.choose)
        self.choose = Label(self, text="Choose file").pack()
        self.image = ImageTk.PhotoImage(Image.open("b.jpg"))
        self.label = Label(image=self.image)
        

        self.file.pack()
        self.label.pack()

    def choose(self):
        global im_path, params_path
        ifile = tkFileDialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        im_path = ifile.name
        hmr_path = "/home/yudhik/study/RESEARCH/hmr"
        cur_path = os.getcwd()
        os.chdir(hmr_path)
        cmd = "python -m demo1 --img_path " + im_path
        print cmd
        os.system(cmd)
        os.chdir(cur_path)
        self.load_image()
    
    def load_image(self, flag=0):
        global im_path, params_path
        img_path = "/home/yudhik/study/RESEARCH/GUI_project/test_img/" + im_path.split('/')[-1][:-4] + ".png"
        params_path = "/home/yudhik/study/RESEARCH/GUI_project/test_params/" + im_path.split('/')[-1][:-4] + ".pkl"
        print(im_path, img_path, params_path)
        self.image2 = ImageTk.PhotoImage(Image.open(img_path).resize((500, 500)))
        self.label.configure(image=self.image2)
        self.label.image=self.image2
        self.load_params(params_path, flag)

    def load_params(self, path, flag):
        if flag is not 0:
            print(1,poses_dict[0].v2.get())
            self.show_params()
            return
        file = open(path, 'rb')
        data = pickle.load(file)
        pose = data['pose'].reshape(72,)
        shape = data['shape'].reshape(10,)
        print pose.shape
        for i in range(0, 10):
            Beta[str(i+1)] = shape[i]
        for i in range(0, 72):
            if i%3==0:
                Posex[str(i/3+1)] = pose[i]
            elif i%3==1:
                Posey[str(i/3+1)] = pose[i]
            elif i%3==2:
                Posez[str(i/3+1)] = pose[i]
        self.show_params()


    def show_params(self):
        for i in range(0,24):
            poses_dict[i].v2.set(str(Posex[str(i+1)])[:6])
            poses_dict[i].v3.set(str(Posey[str(i+1)])[:6])
            poses_dict[i].v4.set(str(Posez[str(i+1)])[:6])
        #print(poses_dict[0].v2.get())

l2 = Label(root,text='Shape Params')
l2.pack()
b1 = scaleS(root,'1',1)
b2 = scaleS(root,'2',2)
b3 = scaleS(root,'3',3)
b4 = scaleS(root,'4',4)
b5 = scaleS(root,'5',5)
b6 = scaleS(root,'6',6)
b7 = scaleS(root,'7',7)
b8 = scaleS(root,'8',8)
b9 = scaleS(root,'9',9)
b10 = scaleS(root,'10',10)
l = Label(leftframe,text='Pose Params')
l.pack()
beta_dict = []

beta_dict.append(b1)
beta_dict.append(b2)
beta_dict.append(b3)
beta_dict.append(b4)
beta_dict.append(b5)
beta_dict.append(b6)
beta_dict.append(b7)
beta_dict.append(b8)
beta_dict.append(b9)
beta_dict.append(b10)

s1 = scale(leftframe,'1',1)
s2 = scale(leftframe,'2',2)
s3 = scale(leftframe,'3',3)
s4 = scale(leftframe,'4',4)
s5 = scale(leftframe,'5',5)
s6 = scale(leftframe,'6',6)
s7 = scale(leftframe,'7',7)
s8 = scale(leftframe,'8',8)
s9 = scale(leftframe,'9',9)
s10 = scale(leftframe,'10',10)
s11 = scale(leftframe,'11',11)
s12 = scale(leftframe,'12',12)
s13 = scale(leftframe,'13',13)
s14 = scale(leftframe,'14',14)
s15 = scale(leftframe,'15',15)
s16 = scale(leftframe,'16',16)
s17 = scale(leftframe,'17',17)
s18 = scale(leftframe,'18',18)
s19 = scale(leftframe,'19',19)
s20 = scale(leftframe,'20',20)
s21 = scale(leftframe,'21',21)
s22 = scale(leftframe,'22',22)
s23 = scale(leftframe,'23',23)
s24 = scale(leftframe,'24',24)
poses_dict = []

poses_dict.append(s1)
poses_dict.append(s2)
poses_dict.append(s3)
poses_dict.append(s4)
poses_dict.append(s5)
poses_dict.append(s6)
poses_dict.append(s7)
poses_dict.append(s8)
poses_dict.append(s9)
poses_dict.append(s10)
poses_dict.append(s11)
poses_dict.append(s12)
poses_dict.append(s13)
poses_dict.append(s14)
poses_dict.append(s15)
poses_dict.append(s16)
poses_dict.append(s17)
poses_dict.append(s18)
poses_dict.append(s19)
poses_dict.append(s20)
poses_dict.append(s21)
poses_dict.append(s22)
poses_dict.append(s23)
poses_dict.append(s24)

# print poses_dict

app = GUI(rightframe)

def getVal():
    global params_path
    for i in range(0, 24):

        if poses_dict[i].v1.get() == 1:
            Posex[str(i+1)] = poses_dict[i].v.get()
        elif poses_dict[i].v1.get() == 2:
            Posey[str(i+1)] = poses_dict[i].v.get()
        elif poses_dict[i].v1.get() == 3:
            Posez[str(i+1)] = poses_dict[i].v.get()
        
    for i in range(0, 10):
        Beta[str(i+1)] = beta_dict[i].v.get()
   
    pose = []
    beta = []
    for i in range(0, 24):
        pose.append(Posex[str(i+1)])
        pose.append(Posey[str(i+1)])
        pose.append(Posez[str(i+1)])
    for i in range(0, 10):
        beta.append(Beta[str(i+1)])
    #print(pose, beta)
    
    #print(params_path)
    verts = get_mesh(m, np.array(pose), np.array(beta))
    file = open(params_path, 'rb')
    data = pickle.load(file)
    proc_param = data['proc_param']
    cam = data['cam']
    joints = data['joints']
    
        
    rerenders(im_path, proc_param, joints, verts, cam)
    img_path = "/home/yudhik/study/RESEARCH/GUI_project/test_img/" + im_path.split('/')[-1][:-4] + ".png"
    app.load_image(flag=1)

    
button2 = Button(bottomframe,text = 'Refresh',fg = 'red',command=getVal)
button2.pack()
img2 = ImageTk.PhotoImage(Image.open('b.jpg').resize((244, 244)))
label2 = Label(rightframe,image=img2)
label2.pack()
root.mainloop()

