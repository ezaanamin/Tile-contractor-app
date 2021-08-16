from tkinter import *
from tkinter.ttk import *
def calculator():
	entry1=m1.get()
	entry2=f1.get()
	e=float(entry1)*3.2808
	b=float(entry2)*3.2808
	q=e*b
	c=e*b*20
	t=round(q,0)
	a=round(c,0)
	result=Label(root,text='Total area in feets:',font=("Arial Black",10))
	resul1=Label(root,text=t,font=("Arial Black",10))
	result.grid(row=5,column=0)
	resul1.grid(row=5,column=1)
	r=0
	if a>=5000:
		p=a*0.05
		r=a-p
	elif a>=8000:
		p=a*0.06
		r=a-p
	elif a>=10000:
		p=a*0.1
		r=a-sp
	else:
		r=a

	po=Label(root,text=r,font=("Arial Black",10))
	po.grid(row=6,column=1)
	Total=Label(root,text='Total price',font=("Arial Black",10))
	Total.grid(row=6,column=0)	

root=Tk()
root.geometry("500x500")
root.configure(bg="#210070")
root.title("Tile contractor app")
meter=Label(root,text='Length in m',font=("Arial Black",10))
Tile=Label(root,text="Tile contractor calculator",font=("Arial Black",20))
Tile.grid(row=0,column=1)
meter.grid(row=1,column=0)
meter=Label(root,text='Width in m',font=("Arial Black",10))
meter.grid(row=2,column=0)
m1=Entry(root,width=30)
m1.grid(row=1,column=1)
f1=Entry(root,width=30)
f1.grid(row=2,column=1)
g=Entry(root)
g=Button(root,text='Calculate',command=lambda :calculator()).grid(row=3,column=1)


root.mainloop()



	
		

	
	
	
	  
	 


	




