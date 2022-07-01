import csv
import Sinbol
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

object_isSnap=True

class Application(tk.Frame):

    def __init__(self,master=None):

        super().__init__(master)
        self.master.title("電子連動 進路作成")
        self.master.geometry("1500x900+200+50")
        self.master.resizable(width=False, height=False)
        self.pack()

        self.Route_view=tk.Canvas(master,background="black",height=900,width=1500)
        self.Route_view.pack(side=tk.LEFT)

        self.isSnap=True
        self.mode=""
        self.grid_modo=True
        self.mouseX,self.mouseY=0,0
        self.track_name=""
        self.track_x,self.track_y=[],[]
        self.point_var=tk.StringVar()
        Sinbol.Canvas_object.canvas=self.Route_view

        self.point_label=tk.Label(self.Route_view,textvariable=self.point_var,bg="white",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"))
        self.back_line=tk.Button(self.Route_view,text="Track",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=lambda:self.new_track("None"))
        self.load_line=tk.Button(self.Route_view,text="Load",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white")
        self.clear_list=tk.Button(self.Route_view,text="Clear",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white")
        self.open_menu=tk.Button(self.Route_view,text="Menu",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white")
        self.line_mode=tk.Button(self.Route_view,text="Grid",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=lambda:self.base_line("None"))
        self.open_menu.place(x=1160,y=840)
        self.back_line.place(x=1400,y=840)
        self.load_line.place(x=1320,y=840)
        self.line_mode.place(x=130,y=840)
        self.clear_list.place(x=1240,y=840)
        self.point_label.place(x=20,y=840,width=100,height=37)

        self.Route_view.bind("<Motion>",self.get_mouse) 
        self.Route_view.bind('<Control-t>',self.new_track,"+")
        self.Route_view.bind('<Control-b>',self.base_line,"+")

        self.Route_view.focus_set()

        Sinbol.Track_01("1RAT",550,550,300,True,True,True)
        Sinbol.Track_02("21T",[220,520,240,520,300,560,320,560])
        Sinbol.Sinbol_02(750,450,"None")

    def new_track(self,event):

        self.entry_box(event,"軌道回路名 入力","軌道回路 名称")

    def entry_box(self,event,name,meg):

        self.dialog=tk.Toplevel(self)
        self.dialog.title(name)
        self.dialog.geometry("300x50+750+450")
        self.dialog.resizable(width=False, height=False)                                                            
        self.dialog.grab_set()
        self.dialog.focus_set()
        self.dialog.transient(self.master)
        self.entry_box=ttk.Entry(self.dialog,width=30)
        entry_label=ttk.Label(self.dialog,text=meg)
        self.entry_box.place(x=((len(meg)-1)*15+5),y=15)
        entry_label.place(x=10,y=15)
        self.entry_box.bind('<Return>',self.track_add)
        self.entry_box.focus_get()

    def track_add(self,event):

        track=self.entry_box.get()
        if track=="":
            return
        self.mode="make track"
        self.dialog.destroy()

    def switch_isSnap(self):

        pass
    
    def get_mouse(self,event):
        
        self.mouseX,self.mouseY=event.x,event.y
        self.point_var.set("x:"+str(int(event.x/20)).zfill(2)+" y:"+str(int(event.y/20)).zfill(2))
    
    def base_line(self,event):

        i,height_dig,width_dig=0,50,100
        if self.grid_modo==True:
            while i<1500:
                self.Route_view.create_line(i+width_dig,0,i+width_dig,900,tags="base_line",fill="white")
                i=i+width_dig
            i=0
            while i<900:
                self.Route_view.create_line(0,i+height_dig,1500,i+height_dig,tags="base_line",fill="white")
                i=i+height_dig
        else :
            self.Route_view.delete("base_line")
        self.grid_modo=not self.grid_modo



if __name__=="__main__":

    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()