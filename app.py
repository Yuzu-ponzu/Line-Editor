import os
import csv
import Sinbol
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

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
        self.isMode=""
        self.grid_modo=True
        self.mouseX,self.mouseY=0,0
        self.track_name=""
        self.object_count=0
        self.object_list=[]
        self.signal_window_isrun=False
        self.track_x,self.track_y=[],[]
        self.point_var=tk.StringVar()
        Sinbol.Canvas_object.canvas=self.Route_view

        self.point_label=tk.Label(self.Route_view,textvariable=self.point_var,bg="white",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"))
        self.make_line=tk.Button(self.Route_view,text="Track",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=lambda:self.new_track("None"))
        self.load_button=tk.Button(self.Route_view,text="Load",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=lambda:self.open_loadDate("None"))
        self.save_button=tk.Button(self.Route_view,text="Save",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white")
        self.open_menu=tk.Button(self.Route_view,text="Menu",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white")
        self.turnout_win=tk.Button(self.Route_view,text="Turnout",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=lambda:self.TurnOut_setup("None"))
        self.signal_menu=tk.Button(self.Route_view,text="Signal",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=self.open_sigSetup)
        self.line_mode=tk.Button(self.Route_view,text="Grid",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),bg="white",command=lambda:self.base_line("None"))

        self.load_button.place(x=1410,y=840)
        self.save_button.place(x=1335,y=840)
        self.open_menu.place(x=1255,y=840)
        self.make_line.place(x=1175,y=840)
        self.signal_menu.place(x=1090,y=840)
        self.turnout_win.place(x=985,y=840)
        self.line_mode.place(x=140,y=840)
        self.point_label.place(x=20,y=840,width=100,height=37)
        
        self.Route_view.bind("<Motion>",self.get_mouse)
        self.Route_view.bind("<Return>",self.make_track,"+")
        self.Route_view.bind("<Button-1>",self.add_track,"+")
        self.Route_view.bind('<Control-t>',self.new_track,"+")
        self.Route_view.bind('<Control-b>',self.base_line,"+")
        self.Route_view.bind('<Control-t>',self.TurnOut_setup,"+")
        self.Route_view.bind('<Control-q>',self.open_sigSetup,"+")

        self.Route_view.focus_set()

        Sinbol.Track("1RAT",550,550,300,True,True,True,True,35,True)
        Sinbol.Track("1RBT",550,600,300,True,True,True,False,0,True)
        Sinbol.Track("1RCT",550,650,300,True,False,True,False,0,True)
        Sinbol.Track("1RDT",550,700,300,False,True,True,False,0,True)
        #Sinbol.Free_track("21T",[220,520,240,520,300,560,320,560])
        Sinbol.Sinbol_02(750,450,"None")

    def open_sigSetup(self):

        if  self.signal_window_isrun==False:
            self.signal_menu_win=tk.Toplevel(self.master)
            self.app=Signal_window(self.signal_menu_win)
            self.signal_window_isrun=True

    def open_loadDate(self,event):

        fTyp=[("json", "*.json")]
        iDir=os.path.abspath(os.path.dirname(__file__))
        file_dialog=tk.filedialog.askopenfilename(title="連動図データを開く",filetypes=fTyp, initialdir=iDir)
        print(type(file_dialog))

    def new_track(self,event):

        self.entry_box(event,"軌道回路名 入力","軌道回路 名称")
    
    def add_track(self,event):

        if self.isMode=="add track point":
            self.track_x.append(int(event.x/5)*5)
            self.track_y.append(int(event.y/5)*5)
            track_len=len(self.track_x)
            if track_len>=1:
                self.Route_view.create_line(self.track_x[track_len-2],self.track_y[track_len-2],self.track_x[track_len-1],self.track_y[track_len-1],width=2,fill="white",tag="new_track")
    
    def make_track(self,event):

        self.isMode=""
        self.Route_view.delete("new_track")
        self.make_line.config(background="white")
        if len(self.track_x)>=1:
            Sinbol.Free_track(self.track_name,self.track_x,self.track_y)
        self.track_name,self.track_x,self.track_y="",[],[]

    def entry_box(self,event,name,meg):

        self.dialog=tk.Toplevel(self)
        self.dialog.title(name)
        self.dialog.geometry("300x50+750+450")
        self.dialog.resizable(width=False, height=False)                                                            
        self.dialog.transient(self.master)
        self.entry_box=ttk.Entry(self.dialog,width=30)
        entry_label=ttk.Label(self.dialog,text=meg)
        self.entry_box.place(x=((len(meg)-1)*15+5),y=15)
        entry_label.place(x=10,y=15)
        self.entry_box.bind('<Return>',self.track_add)
        self.dialog.grab_set()
        self.dialog.focus_set()
        self.entry_box.focus_get()

    def signal_maker(self,main_signal,sub_signal,light,inset,indect,locking):

        pass

    def locking_menu(self):

        pass
    
    #Signal window ここまで/ここからTurnOut window

    def TurnOut_setup(self,event):

        self.turnout_menu=tk.Toplevel(self)
        self.turnout_menu.title("分岐器　新規作成")
        self.turnout_menu.geometry("200x220+850+450")
        self.turnout_menu.resizable(width=False, height=False)                                                            
        self.turnout_menu.transient(self.master)
        self.turnout_menu.grab_set()
        self.turnout_menu.focus_set()

        menu_frame=tk.Frame(self.turnout_menu,height=200,width=220)
        info_label,label_object,y=["分岐器種類"," 動作方法 ","分岐器番号"," 番号標準 "," 転轍標識 "],[],10

        for i in range(len(info_label)):
            label_object.append(tk.Label(menu_frame,text=info_label[i],background="white"))
            label_object[i].place(x=10,y=y)
            y+=30
        menu_frame.pack()

    def track_add(self,event):

        track=self.entry_box.get()
        if track=="":
            return
        self.isMode="add track point"
        self.make_line.config(background="green")
        self.dialog.destroy()

    def switch_isSnap(self):

        pass
    
    def get_mouse(self,event):
        
        self.mouseX,self.mouseY=event.x,event.y
        self.point_var.set("x:"+str(int(event.x/20)).zfill(2)+" y:"+str(int(event.y/20)).zfill(2))

    def make_signal(self):

        pass
    
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

class Signal_window(tk.Frame):

    def __init__(self,master):

        super().__init__(master)
        self.pack()
        self.master.title("信号機 新規作成")
        self.master.geometry("200x250+850+450")
        self.master.resizable(width=False, height=False)                                                            
        #self.master.transient(self.master)
        self.master.grab_set()
        self.master.focus_set()
        self.master.protocol("WM_DELETE_WINDOW",self.close_menu)

        info_label,label_object,y=["信号種類","現示種類","設置形態","付属設備","誘導設置","連動条件","信号番号"],[],10
        signal_list=["場内信号機","出発信号機","入換信号機","入換標識","入信 入標共用"]
        signal_types=["R,G","R,Y","R,YY,Y","R,Y,G","R,YY,Y,G","R,Y,YG,G","--設定不能--"]
        signal_inset=["柱上(単独)","柱上(付属)","懸垂式","地上直置き","信号機本体のみ"]
        signal_attached=["入換信号機","入換標識","入信 入標共用","入信(誘導付属)","設置しない"]
        signal_indect=["設置する","設置しない"]
        signal_number=["表示する","表示しない"]
        signal_locking=["設定する","設定しない"]
        menu_frame=tk.Frame(self.master,height=250,width=200)
        self.parts_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_list)
        self.parts_pudown.current(0)
        self.inset_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_inset)
        self.inset_pudown.current(0)
        self.parts_pudown.bind('<<ComboboxSelected>>',self.signal_typeset)
        self.types_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_types)
        self.types_pudown.current(3)
        self.attached_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_attached)
        self.attached_pudown.current(4)
        self.indect_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_indect)
        self.indect_pudown.current(1)
        self.locking_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_locking)
        self.locking_pudown.current(1)
        self.number_pudown=ttk.Combobox(menu_frame,state="readonly",values=signal_number)
        self.number_pudown.current(0)
        self.inset_pudown.place(x=80,y=70,width=110)
        self.types_pudown.place(x=80,y=40,width=110)
        self.parts_pudown.place(x=80,y=10,width=110)
        self.indect_pudown.place(x=80,y=130,width=110)
        self.locking_pudown.place(x=80,y=160,width=110)
        self.attached_pudown.place(x=80,y=100,width=110)
        self.number_pudown.place(x=80,y=190,width=110)
        signal_add=ttk.Button(menu_frame,text="OK",command=self.signal_getconfig)
        signal_add.place(x=70,y=220)
        for i in range(len(info_label)):
            label_object.append(tk.Label(menu_frame,text=info_label[i],background="white"))
            label_object[i].place(x=10,y=y)
            y+=30
        menu_frame.pack()

    def signal_getconfig(self):

        inset=self.inset_pudown.get()               #設置方法
        light=self.types_pudown.get()               #場内,出発信号機の灯火
        indect=self.indect_pudown.get()             #誘導信号機の設置有無
        locking=self.locking_pudown.get()           #連動条件の設定
        main_signal=self.parts_pudown.get()         #主信号機の種類
        umber_flg=self.number_pudown.get()          #番号表示の有無
        sub_signal=self.attached_pudown.get()       #従属信号機の種類
        self.close_menu()
        if locking=="設定しない":
            pass
        else :
            app.make_signal()
        print(inset,light,indect,locking,main_signal,sub_signal)

    def signal_typeset(self,event):

        type=self.parts_pudown.get()
        if not(type=="場内信号機" or type=="出発信号機"):
            self.types_pudown.set("--設定不能--")
            self.types_pudown.config(state="disabled")
            self.attached_pudown.set("--設定不能--")
            self.attached_pudown.config(state="disabled")
            if type=="入換標識":
                self.indect_pudown.set("--設定不能--")
                self.indect_pudown.config(state="disabled")
            else :
                self.indect_pudown.config(state="readonly")
                self.indect_pudown["values"]=["設置する","設置しない"]
                self.indect_pudown.current(1)
        else:
            self.types_pudown.config(state="readonly")
            self.types_pudown["values"]=["R,G","R,Y","R,YY,Y","R,Y,G","R,YY,Y,G","R,Y,YG,G","--設定不能--"]
            self.types_pudown.current(3)
            self.attached_pudown.config(state="readonly")
            self.attached_pudown["values"]=["入換信号機","入換標識","入信 入標共用","入信(誘導付属)","設置しない"]
            self.attached_pudown.current(4)
            self.indect_pudown.config(state="readonly")
            self.indect_pudown["values"]=["設置する","設置しない"]
            self.indect_pudown.current(1)

    def close_menu(self):

        self.master.destroy()
        print(app.signal_window_isrun)
        app.signal_window_isrun=False
        print(app.signal_window_isrun)

def main():

    root=tk.Tk()
    global app
    app=Application(master=root)
    app.mainloop()

if __name__=="__main__":

    main()