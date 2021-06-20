from tkinter import *
import math , random
import os
from tkinter import messagebox
class Bill_app:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700")
        self.root.title("RSV HunGry SoluTion")
        bg_colour ="#0c4f53"
        fg_colour ="#747810"
        h_colour = "#BCC6CC"
        #logo = tkinter.PhotoImage(file = "bill_area.jpg")
        title=Label(self.root,text="RSV HunGry SoluTion",bd= 8,relief=FLAT,bg = bg_colour , fg= fg_colour , font=("RIBBON",27,"overstrike","italic"),pady=2).pack(fill= X)
        #*******VARIABLES*********
        #************COSMETICS*********
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gel=IntVar()
        self.lotion=IntVar()
        #***********GROCERY************
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.pulses=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #*********COLD DRINKS**********
        self.maza=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #********Total product price & Tax********
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #*********customer************
        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))

        self.search_bill=StringVar()

        #**********************customer detail frame****************
        F1 = LabelFrame(self.root,bd=10,relief=FLAT,text="Customer Details",font = ("times new roman",15,"bold"),fg=h_colour,bg = bg_colour   )
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl = Label(F1,text ="Customer Name",bg = bg_colour,fg = "white" ,font=("times new roman",18,"bold")).grid(row=0,column= 0 , padx=20 , pady=5)
        cname_txt = Entry(F1,width=18,textvariable=self.c_name, font = "arial 15", bd =3 , relief= SOLID).grid(row=0,column = 1,pady=5,padx=10)
        
        cphn_lbl = Label(F1,text ="Phone No.",bg = bg_colour,fg = "white" ,font=("times new roman",18,"bold")).grid(row=0,column=2 , padx=20 , pady=5)
        cphn_txt = Entry(F1,width=18,textvariable=self.c_phone,font = "arial 15", bd =3 , relief= SOLID).grid(row=0,column = 3,pady=5,padx=10)

        c_bill_lbl = Label(F1,text ="Bill Number",bg = bg_colour,fg = "white" ,font=("times new roman",18,"bold")).grid(row=0,column= 4 , padx=20 , pady=5)
        c_bill_txt = Entry(F1,width=18,textvariable=self.search_bill,font = "arial 15", bd =3, relief = SOLID).grid(row=0,column = 5,pady=5,padx=10)

        bill_btn = Button(F1,text="Search",command=self.find_bill,width=8,bd=7,font="chewy 12 bold").grid(row=0,column = 6,padx=10,pady= 10)

        
        #******************Cosmetics Frame*********************
        F2=LabelFrame(self.root,bd=10,relief=FLAT,text="Cosmetics",font = ("times new roman",15,"bold"),fg=h_colour,bg = bg_colour   )
        F2.place(x=0,y=180,width=325,height=380)

        bath_lbl= Label(F2,text="Bath soap",font=("times new roman",16,"bold"),bg=bg_colour,fg= fg_colour).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=8,textvariable=self.soap,font=("times new roman",16,"bold"),bd=2,relief = SOLID).grid(row=0,column=1,padx=10,pady=10)

        face_cream_lbl= Label(F2,text="face cream",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=8,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl= Label(F2,text="face wash",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=8,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=2,column=1,padx=10,pady=10)

        hair_s_lbl= Label(F2,text="Hair Spray",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=8,textvariable=self.spray,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=3,column=1,padx=10,pady=10)

        hair_g_lbl= Label(F2,text="Hair Gel",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_g_txt=Entry(F2,width=8,textvariable=self.gel,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=4,column=1,padx=10,pady=10)


        body_lbl= Label(F2,text="Body Lotion",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_s_txt=Entry(F2,width=8,textvariable=self.lotion,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=5,column=1,padx=10,pady=10)

        #******************Drink's*********************
        F4=LabelFrame(self.root,bd=10,relief=FLAT,text="Drink_s",font = ("times new roman",15,"bold"),fg=h_colour,bg = bg_colour   )
        F4.place(x=300,y=180,width=325,height=380)

        d1_lbl= Label(F4,text="MAZA",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        d1_txt=Entry(F4,width=8,textvariable=self.maza,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=0,column=1,padx=10,pady=10)

        d2_lbl= Label(F4,text="COKE",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        d2_txt=Entry(F4,width=8,textvariable=self.coke,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=1,column=1,padx=10,pady=10)

        d3_lbl= Label(F4,text="FROOTI",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        d3_txt=Entry(F4,width=8,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=2,column=1,padx=10,pady=10)

        d4_lbl= Label(F4,text="THUMBs Up",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d4_txt=Entry(F4,width=8,textvariable=self.thumbsup,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=3,column=1,padx=10,pady=10)

        d5_lbl= Label(F4,text="LIMCA",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        d5_txt=Entry(F4,width=8,textvariable=self.limca,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=4,column=1,padx=10,pady=10)

        d6_lbl= Label(F4,text="SPRITE",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        d6_txt=Entry(F4,width=8,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=5,column=1,padx=10,pady=10)

        #******************Grocery Frame*********************
        F3=LabelFrame(self.root,bd=20,relief=FLAT,text="Grocery",font = ("times new roman",15,"bold"),fg=h_colour,bg = bg_colour   )
        F3.place(x=600,y=180,width=325,height=380)

        g1_lbl= Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=8,textvariable=self.rice,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl= Label(F3,text="Food Oil",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=8,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl= Label(F3,text="pulses",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=8,textvariable=self.pulses,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl= Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=8,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl= Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=8,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl= Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_colour,fg=fg_colour).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=8,textvariable=self.tea,font=("times new roman",16,"bold"),bd=2,relief=SOLID).grid(row=5,column=1,padx=10,pady=10)

        #**************Bill Area************
        F5=Frame(self.root,bd=2,relief=SOLID)
        F5.place(x=950,y=180,width=360,height=380)
        bill_title=Label(F5,text="BILL AREA",font="chewy 15 bold",bd =2,relief=SOLID).pack(fill=X)
        scrol_y=Scrollbar(F5,orient = VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill = BOTH,expand = 1)
        
        #************Button frame***************
        F6 =LabelFrame(self.root,bd=4,relief=SOLID,text="BILL MENU",font = ("times new roman",15,"bold"),fg=h_colour,bg = bg_colour)
        F6.place(x=0,y=560,relwidth=1,height=140)
        m1_lbl = Label(F6,text="TOTAL COSMETIC PRICE",bg=bg_colour,fg = "white" , font =("tomes new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=13,textvariable=self.cosmetic_price,font="arial 10 bold",bd = 3,relief=SOLID).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl = Label(F6,text="TOTAL GROCERY PRICE",bg=bg_colour,fg = "white" , font =("tomes new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=13,textvariable=self.grocery_price,font="arial 10 bold",bd = 3,relief=SOLID).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl = Label(F6,text="TOTAL DRINK_S PRICE",bg=bg_colour,fg = "white" , font =("tomes new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=13,textvariable=self.cold_drink_price,font=("arial 10 bold"),bd = 3,relief=SOLID).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl = Label(F6,text="COSMETIC Tax",bg=bg_colour,fg = "white" , font =("tomes new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=13,textvariable=self.cosmetic_tax,font="arial 10 bold",bd = 3,relief=SOLID).grid(row=0,column=3,padx=10,pady=1)

        c2_lbl = Label(F6,text="GROCERY Tax",bg=bg_colour,fg = "white" , font =("tomes new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=13,textvariable=self.grocery_tax,font="arial 10 bold",bd = 3,relief=SOLID).grid(row=1,column=3,padx=10,pady=1)

        c3_lbl = Label(F6,text="DRINK_S Tax",bg=bg_colour,fg = "white" , font =("tomes new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=13,textvariable=self.cold_drink_tax,font=("arial 10 bold"),bd = 3,relief=SOLID).grid(row=2,column=3,padx=10,pady=1)

        #*********button fraame***********

        btn_F=Frame(F6,bd=3,relief=GROOVE)
        btn_F.place(x=740,width=585,height=90)

        total_btn = Button(btn_F,text="TOTAL",command=self.total ,bg=bg_colour,fg="white",pady=6,width=11,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        GBILL_btn = Button(btn_F,text="GENRATE BILL",command=self.bill_area,bg=bg_colour,fg="white",pady=6,width=11,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        CLEAR_btn = Button(btn_F,text="CLEAR",command=self.clear_data,bg=bg_colour,fg="white",pady=6,width=11,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        EXIT_btn = Button(btn_F,text="EXIT",command=self.exit_app,bg=bg_colour,fg="white",pady=6,width=11,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
        self.c_s_p= self.soap.get()*40
        self.c_fc_p= self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gel.get()*140
        self.c_bl_p=self.lotion.get()*180
        self.total_cosmetic_price=float(
                                    self.c_bl_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hg_p+
                                    self.c_hs_p+
                                    self.c_s_p
                                  ) 
        self.cosmetic_price.set("Rs.  "+str(self.total_cosmetic_price))
        self.c_tax =round((self.total_cosmetic_price * 0.05),2)
        self.cosmetic_tax.set( "Rs.  " +str(self.c_tax))

        self.D_m_p = self.maza.get()*40
        self.D_c_p = self.coke.get()*120
        self.D_s_p = self.sprite.get()*60
        self.D_f_p = self.frooti.get()*180
        self.D_t_p = self.thumbsup.get()*140
        self.D_l_p = self.limca.get()*180

        


        self.total_drink_price=float(
                                self.D_c_p+
                                self.D_f_p+
                                self.D_l_p+
                                self.D_s_p+
                                self.D_t_p+
                                self.D_m_p
                                  ) 
        self.cold_drink_price.set("Rs.  "+str(self.total_drink_price) )
        self.d_tax=round((self.total_drink_price* 0.05),2)
        self.cold_drink_tax.set( "Rs.  " +str(self.d_tax))

        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.pulses.get()*60
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180

        self.total_grocery_price=float(
                                      self.g_r_p+
                                      self.g_f_p+
                                      self.g_d_p+
                                      self.g_w_p+
                                      self.g_s_p+
                                      self.g_t_p                          
                                  ) 
        self.grocery_price.set( "Rs.  "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price * 0.05),2)
        self.grocery_tax.set( "Rs.  " +str(self.g_tax))

        self.total_bill=float(  self.total_cosmetic_price + self.c_tax + 
                                self.total_drink_price + self.d_tax +
                                self.total_grocery_price + self.g_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"              .....RSV.....\n        .....THANKS FOR COMMING.....")
        self.txtarea.insert(END,f"\n BILL NO.            : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name       : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Customer Phone no.  : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n ---------------------------------------")
        self.txtarea.insert(END,f"\n Product\t  |\tQTY.\t|\tPrice")
        self.txtarea.insert(END,f"\n ---------------------------------------")


    def bill_area(self):
        if self.c_name.get=="" or self.c_phone.get()=="" :
            messagebox.showerror("Error ","CUSTOMER DETAILS ARE MUST")
        # elif self.c_phone.get() != int(len(10)):
        #     messagebox.showerror("ENTER CORRECT MOBILE NUMBER")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0" :
            messagebox.showerror("NO PRODUCTED PURCHASE")
        

        else:
            self.welcome_bill()
            #*************cosmetics***********
            if self.soap.get() != 0:
                self.txtarea.insert(END,f"\n BATH SOAP\t\t{self.soap.get()}\t\t{self.c_s_p}")
            if self.face_cream.get() != 0:
                self.txtarea.insert(END,f"\n FACE CREAM\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
            if self.face_wash.get() != 0:
                self.txtarea.insert(END,f"\n FACE WASH\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            if self.spray.get() != 0:
                self.txtarea.insert(END,f"\n HAIR SPRAY\t\t{self.spray.get()}\t\t{self.c_hs_p}")
            if self.gel.get() != 0:
                self.txtarea.insert(END,f"\n HAIR GEL\t\t{self.gel.get()}\t\t{self.c_hg_p}")
            if self.lotion.get() != 0:
                self.txtarea.insert(END,f"\n BODY LOTION\t\t{self.lotion.get()}\t\t{self.c_bl_p}")

            #**********drinks*************
            if self.maza.get() != 0:
                self.txtarea.insert(END,f"\n MAZA\t\t{self.maza.get()}\t\t{self.D_m_p}")
            if self.coke.get() != 0:
                self.txtarea.insert(END,f"\n COKE\t\t{self.coke.get()}\t\t{self.D_c_p}")
            if self.frooti.get() != 0:
                self.txtarea.insert(END,f"\n FROOTI\t\t{self.frooti.get()}\t\t{self.D_f_p}")
            if self.thumbsup.get() != 0:
                self.txtarea.insert(END,f"\n THUMBS UP\t\t{self.thumbsup.get()}\t\t{self.D_t_p}")
            if self.limca.get() != 0:
                self.txtarea.insert(END,f"\n LIMCA\t\t{self.limca.get()}\t\t{self.D_l_p}")
            if self.sprite.get() != 0:
                self.txtarea.insert(END,f"\n SPRITE\t\t{self.sprite.get()}\t\t{self.D_s_p}")

            #***********grocery*********
            if self.rice.get() != 0:
                self.txtarea.insert(END,f"\n RICE\t\t{self.rice.get()}\t\t{self.g_r_p}")
            if self.pulses.get() != 0:
                self.txtarea.insert(END,f"\n PULSES\t\t{self.pulses.get()}\t\t{self.g_d_p}")
            if self.food_oil.get() != 0:
                self.txtarea.insert(END,f"\n FOOD OIL\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
            if self.wheat.get() != 0:
                self.txtarea.insert(END,f"\n WHEAT\t\t{self.wheat.get()}\t\t{self.g_w_p}")
            if self.sugar.get() != 0:
                self.txtarea.insert(END,f"\n SUGAR\t\t{self.sugar.get()}\t\t{self.g_s_p}")
            if self.tea.get() != 0:
                self.txtarea.insert(END,f"\n TEA\t\t{self.tea.get()}\t\t{self.g_t_p}")

            
            self.txtarea.insert(END,f"\n----------------------------------------")
            if self.cosmetic_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t       {self.cosmetic_tax.get()}")
            if self.cold_drink_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Cold drinks Tax     {self.cold_drink_tax.get()}")
            if self.grocery_tax.get()!="0.0":
                self.txtarea.insert(END,f"\n Grocery Tax         {self.grocery_tax.get()}")
            
            self.txtarea.insert(END,f"\n----------------------------------------")

            self.txtarea.insert(END,f"\n TOTAL AMOUNT        Rs.  { str(self.total_bill)}")

            self.txtarea.insert(END,f"\n----------------------------------------")
            self.save_bill()


        
    def save_bill(self):
        op = messagebox.askyesno("Save BILL ", "Do you want to save the bill ?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} saved successfully")
        else :
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("D:/BILL_App/Bills"):
            if i.split('.')[0]==self.search_bill.get():
                save_path = 'D:/BILL_App/Bills'
                name_of_file =str(i)
                completeName = os.path.join(save_path, name_of_file)         
                f1 = open(completeName, "r")
                self.txtarea.delete('1.0',END)
                for d in f1 :
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present == "no":
            messagebox.showerror("ERROR","Invalid Bill Number")
            print(i)

    def clear_data(self):
        op = messagebox.askyesno("CLEAR","DO YOU WANT TO CLEAR ?")
        if op>0:
            # self.root.destroy()

            #**********cosmetic******
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gel.set(0)
            self.lotion.set(0)
            #***********GROCERY************
            self.rice.set(0)
            self.food_oil.set(0)
            self.pulses.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #*********COLD DRINKS**********
            self.maza.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            #********Total product price & Tax********
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")

            #*********customer************
            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill(self)
    
    def exit_app(self):
        op = messagebox.askyesno("EXIT","DO YOU WANT TO EXIT ?")
        if op>0:
            self.root.destroy()

root=Tk()
Obj = Bill_app(root)
root.mainloop()
