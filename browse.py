# from tkinter import *
# from tkinter import filedialog
# from PIL import Image, ImageTk

# root = Tk()
# root.title('Mesh GUI')
# root.geometry('1024x1024')
# rightframe = Frame(root)
# rightframe.pack(side= RIGHT)
# img1 = ImageTk.PhotoImage(Image.open('a.png').resize((400, 400)))
# label1 = Label(rightframe,image=img1)
# label1.pack()
# def browsefunc():
#     filename = filedialog.askopenfilename()

#     img1 = ImageTk.PhotoImage(Image.open(filename).resize((400, 400)))
#     label1 = Label(rightframe,image=img1)
#     label1.pack()

# browsebutton = Button(root, text="Browse", command=browsefunc)
# browsebutton.pack()

# root.mainloop()

from Tkinter import *
import tkFileDialog
from tkFileDialog import askdirectory
from PIL import  Image, ImageTk
import sys, os
# sys.path.append('/home/yudhik/study/RESEARCH/hmr')
class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 650, 650
        master.minsize(width=w, height=h)
        master.maxsize(width=w, height=h)
        self.pack()

        self.file = Button(self, text='Browse', command=self.choose)
        self.choose = Label(self, text="Choose file").pack()
        self.image = ImageTk.PhotoImage(Image.open("b.jpg"))
        self.label = Label(image=self.image)


        self.file.pack()
        self.label.pack()

    def choose(self):
        ifile = tkFileDialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        path = ifile.name
        hmr_path = "/home/yudhik/study/RESEARCH/hmr"
        cur_path = os.getcwd()
        os.chdir(hmr_path)
        print os.listdir('.')
        cmd = "python -m demo1 --img_path " + path
        print cmd
        os.system(cmd)
        os.chdir(cur_path)
        img_path = "/home/yudhik/study/RESEARCH/GUI_project/test_img/" + path.split('/')[-1][:-4] + ".png"
        self.image2 = ImageTk.PhotoImage(Image.open(img_path))
        self.label.configure(image=self.image2)
        self.label.image=self.image2


root = Tk()
app = GUI(master=root)
app.mainloop()
root.destroy()