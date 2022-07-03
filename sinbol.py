#ドラッグオブジェクト　上位クラス
#from pyxel import width
#

class Canvas_object:

    canvas=None

    def drag_start(self,event):

        self.x,self.y=event.x,event.y
        #self.load_csv(event)

    def dragging(self,event):

        x1,y1=(int(event.x/10)*10),(int(event.y/10)*10)
        for i in range(len(self.parts_list)):
            Canvas_object.canvas.lift(self.name+self.parts_list[i])
            Canvas_object.canvas.move(self.name+self.parts_list[i],x1-self.x,y1-self.y)
        self.x,self.y=x1,y1 
        #self.load_csv(event)                     

    def event_bind(self,name,parts_list,x,y,flg):

        self.name,self.parts_list,self.x,self.y,self.flg=name,parts_list,x,y,flg
        for i in range(0,len(self.parts_list)):
            Canvas_object.canvas.tag_bind(self.name+self.parts_list[i],"<Button-1>",self.drag_start)
            Canvas_object.canvas.tag_bind(self.name+self.parts_list[i],"<Button1-Motion>",self.dragging)
            if self.flg==True:
                Canvas_object.canvas.tag_bind(self.name+self.parts_list[i],"<Double-1>",self.switch_draw)

#着点有/発点両方向
class Track(Canvas_object):

    def __init__(self,name,x,y,length,left,right,button,track,text_mid,section):

        self.name,self.x,self.y,self.left,self.right,self.parts,self.section=name,x,y,left,right,["A"],section
        self.EndPointOffset,self.Track_length,self.size,self.button,self.track,self.text_mid=50,length,20,button,track,text_mid
        Canvas_object.canvas.create_line(self.x,self.y,self.x+self.Track_length,self.y,fill="white",width=2,tags=self.name+"A")
        if self.section==True:
            self.parts.append("G")
            self.parts.append("H")
            Canvas_object.canvas.create_line(self.x,self.y-5,self.x,self.y+5,fill="white",width=2,tags=self.name+"G")
            Canvas_object.canvas.create_line(self.x+self.Track_length,self.y-5,self.x+self.Track_length,self.y+5,fill="white",width=2,tags=self.name+"H")
        if self.track==False:
            if self.left==True:
                Canvas_object.canvas.create_polygon(
                    self.x+self.EndPointOffset,self.y,
                    self.x+self.EndPointOffset+self.size,self.y+int(self.size/2),
                    self.x+self.EndPointOffset+self.size,self.y-int(self.size/2),
                    width=2,outline="white",fill="black",tags=self.name+"B"
                    )
                self.parts.append("B")
            if self.right==True:
                Canvas_object.canvas.create_polygon(
                    self.x+self.Track_length-self.EndPointOffset+self.size,self.y,
                    self.x+self.Track_length-self.EndPointOffset,self.y+int(self.size/2),
                    self.x+self.Track_length-self.EndPointOffset,self.y-int(self.size/2),
                    width=2,outline="white",fill="black",tags=self.name+"C"
                    )
                self.parts.append("C")
            if self.button!=False and self.track==False:
                Canvas_object.canvas.create_oval(
                    self.x+int(self.Track_length/2)-int(self.size/2),self.y-int(self.size/2),
                    self.x+int(self.Track_length/2)+int(self.size/2),self.y+int(self.size/2),
                    width=2,outline="white",tags=self.name+"D",fill="black"
                )
                self.parts.append("D")
        else:
            self.parts.append("E")
            self.parts.append("F")
            Canvas_object.canvas.create_rectangle(self.x+int(self.Track_length/2)-self.text_mid,self.y-5,self.x+int(self.Track_length/2)+self.text_mid,self.y+5,fill="black",tags=self.name+"E")
            Canvas_object.canvas.create_text(self.x+int(self.Track_length/2),self.y,text="("+self.name+")",fill="white",font=("HG丸ｺﾞｼｯｸM-PRO",14,"bold"),tags=self.name+"F")
        Canvas_object.event_bind(self,self.name,self.parts,self.x,self.y,False)

#着点有/発点片方向
class Track_02(Canvas_object):

    def __init__(self,name,line):

        self.name,self.line=name,line
        Canvas_object.canvas.create_line(self.line,fill="white",width=2,tags=self.name+"A")
        #Canvas_object.event_bind(self,self.name,["A"],self.x,self.y,False)
#
class Free_track(Canvas_object):

    def __init__(self,name,track_x,track_y):

        self.name,self.track_x,self.track_y=name,track_x,track_y
        for i in range(1,len(self.track_x)):
            print(self.track_x[i],self.track_y[i])
            Canvas_object.canvas.create_line(self.track_x[i-1],self.track_y[i-1],self.track_x[i],self.track_y[i],width=2,fill="white",tags=self.name+"A")
        Canvas_object.event_bind(self,self.name,["A"],self.track_x[0],self.track_y[0],False)

class Sinbol_01(Canvas_object):

    def __init__(self,x,y,name):

        self.x,self.y,self.name,oval_size,grund_size,heght,self.aspect=x,y,"Sinbol-01-"+name,15,10,10,True
        Canvas_object.canvas.create_oval(
            self.x+heght,self.y-int(oval_size/2),self.x+heght+oval_size,self.y+int(oval_size/2),fill="black",outline="white",width=2,tags=self.name+"A"    
        )
        Canvas_object.canvas.create_line(
            self.x,self.y+int(grund_size/2),self.x,self.y-int(grund_size/2),fill="white",width=2,tags=self.name+"B"
        )
        Canvas_object.canvas.create_line(
            self.x,self.y,self.x+heght+oval_size,self.y,fill="white",width=2,tags=self.name+"C"    
        )
        Canvas_object.canvas.create_line(
            self.x+heght+int(oval_size/2)+1,self.y+int(oval_size/2),self.x+heght+int(oval_size/2)+1,self.y-int(oval_size/2),fill="white",width=2,tags=self.name+"D"    
        )
        Canvas_object.event_bind(self,self.name,["A","B","C","D"],self.x,self.y,True)

    def switch_draw(self,event):

        self.aspect,oval_size,grund_size,heght=not self.aspect,15,10,10
        if self.aspect==True:
            Canvas_object.canvas.coords(self.name+"A",self.x+heght,self.y-int(oval_size/2),self.x+heght+oval_size,self.y+int(oval_size/2))
            Canvas_object.canvas.coords(self.name+"B",self.x,self.y+int(grund_size/2),self.x,self.y-int(grund_size/2))
            Canvas_object.canvas.coords(self.name+"C",self.x,self.y,self.x+heght+oval_size,self.y)
            Canvas_object.canvas.coords(self.name+"D",self.x+heght+int(oval_size/2)+1,self.y+int(oval_size/2),self.x+heght+int(oval_size/2)+1,self.y-int(oval_size/2))
        else:
            Canvas_object.canvas.coords(self.name+"A",self.x-heght,self.y+int(oval_size/2),self.x-heght-oval_size,self.y-int(oval_size/2))
            Canvas_object.canvas.coords(self.name+"B",self.x,self.y-int(grund_size/2),self.x,self.y+int(grund_size/2))
            Canvas_object.canvas.coords(self.name+"C",self.x,self.y,self.x-heght-oval_size,self.y)
            Canvas_object.canvas.coords(self.name+"D",self.x-heght-int(oval_size/2),self.y-int(oval_size/2),self.x-heght-int(oval_size/2),self.y+int(oval_size/2))

#車両停止位置
class Sinbol_02(Canvas_object):

    def __init__(self,x,y,name):

        self.x,self.y,self.name,rect_size,grund_size,heght,self.aspect=x,y,"Sinbol-02"+name,12,10,10,True
        Canvas_object.canvas.create_line(
            self.x,self.y+int(grund_size/2),self.x,self.y-int(grund_size/2),fill="white",width=2,tags=self.name+"A"
        )
        Canvas_object.canvas.create_rectangle(
            self.x+heght,self.y-int(rect_size/2),self.x+heght+rect_size,self.y+int(rect_size/2),outline="white",fill="black",width=2,tags=self.name+"B"
        )
        Canvas_object.canvas.create_line(
            self.x,self.y,self.x+heght+rect_size,self.y,fill="white",width=2,tags=self.name+"C"    
        )
        Canvas_object.canvas.create_line(
            self.x+heght+int(rect_size/2),self.y+int(rect_size/2),self.x+heght+int(rect_size/2),self.y-int(rect_size/2),fill="white",width=2,tags=self.name+"D"    
        )
        Canvas_object.event_bind(self,self.name,["A","B","C","D"],self.x,self.y,True)

    def switch_draw(self,event):

        rect_size,grund_size,heght=12,10,10
        self.aspect=not self.aspect
        if self.aspect==True:
            Canvas_object.canvas.coords(self.name+"A",self.x,self.y+int(grund_size/2),self.x,self.y-int(grund_size/2))
            Canvas_object.canvas.coords(self.name+"B",self.x+heght,self.y-int(rect_size/2),self.x+heght+rect_size,self.y+int(rect_size/2))
            Canvas_object.canvas.coords(self.name+"C",self.x,self.y,self.x+heght+rect_size,self.y)
            Canvas_object.canvas.coords(self.name+"D",self.x+heght+int(rect_size/2),self.y+int(rect_size/2),self.x+heght+int(rect_size/2),self.y-int(rect_size/2))
        else:
            Canvas_object.canvas.coords(self.name+"A",self.x,self.y+int(grund_size/2),self.x,self.y-int(grund_size/2))
            Canvas_object.canvas.coords(self.name+"B",self.x-heght,self.y+int(rect_size/2),self.x-heght-rect_size,self.y-int(rect_size/2))
            Canvas_object.canvas.coords(self.name+"C",self.x,self.y,self.x-heght-rect_size,self.y)
            Canvas_object.canvas.coords(self.name+"D",self.x-heght-int(rect_size/2),self.y-int(rect_size/2),self.x-heght-int(rect_size/2),self.y+int(rect_size/2))

#車止標識
class Sinbol_03(Canvas_object):

    def __init__(self,x,y,name):

        self.x,self.y,self.name,rect_size=x,y,"Sinbol-03"+name,20
        Canvas_object.canvas.create_rectangle(
            self.x,self.y,self.x+rect_size,self.y+rect_size,outline="white",fill="black",width=2,tags=self.name+"A"
        )
        Canvas_object.canvas.create_line(
            self.x,self.y,self.x+rect_size,self.y+rect_size,fill="white",width=2,tags=self.name+"B"    
        )
        Canvas_object.canvas.create_line(
            self.x,self.y+rect_size,self.x+rect_size,self.y,fill="white",width=2,tags=self.name+"C"    
        )
        Canvas_object.event_bind(self,self.name,["A","B","C"],self.x,self.y,False)

#車両接触限界標識
class Sinbol_04(Canvas_object):

    def __init__(self,x,y,name):

        self.x,self.y,self.name,size=x,y,"Sinbol-04"+name,8
        Canvas_object.canvas.create_line(
            self.x,self.y,self.x+size,self.y+size,fill="white",width=2,tags=self.name+"A"    
        )
        Canvas_object.canvas.create_line(
            self.x,self.y+size,self.x+size,self.y,fill="white",width=2,tags=self.name+"B"    
        )
        Canvas_object.event_bind(self,self.name,["A","B"],self.x,self.y,False)
 
#信号扱所
class Sinbol_05(Canvas_object):

    def __init__(self,x,y,name):

        self.x,self.y,self.name,heght,width=x,y,"Sinbol-05"+name,35,60
        Canvas_object.canvas.create_rectangle(
            self.x,self.y,self.x+width,self.y+heght,outline="white",fill="black",width=2,tags=self.name+"A"
        )
        Canvas_object.canvas.create_rectangle(
            self.x+5,self.y+5,self.x+width-5,self.y+int(heght/3),outline="white",fill="white",width=2,tags=self.name+"A"
        )
        Canvas_object.canvas.create_oval(
            self.x+int(width/2)-5,self.y+20,self.x+int(width/2)+5,self.y+30,fill="white",width=2,tags=self.name+"C"    
        )
        Canvas_object.event_bind(self,self.name,["A","B","C"],self.x,self.y,False)

#軌道回路区分
class Sinbol_06(Canvas_object):

    def __init__(self,x,y,name):

        self.x,self.y,self.name,size=x,y,"Sinbol-06"+name,15
        Canvas_object.canvas.create_line(
            self.x,self.y,self.x,self.y+size,fill="white",width=2,tags=self.name+"A"    
        )
        Canvas_object.canvas.create_line(
            self.x+5,self.y,self.x+5,self.y+size,fill="white",width=2,tags=self.name+"B"    
        )
        Canvas_object.event_bind(self,self.name,["A","B"],self.x,self.y,False)