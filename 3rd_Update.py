from tkinter import *
from tkinter import messagebox
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#----------------
import mysql.connector
#------------------
import matplotlib.pyplot as plt
import numpy as np
#---------------------

mydb=mysql.connector.connect(host="localhost",user="root",passwd="abhi",database="tictaktoe")
mycursor=mydb.cursor()

global temp
temp=0
t=0
global still_running
still_running=True
root= Tk()

root.geometry("400x160")
root.maxsize(400,160)
root.minsize(400,160)
root.title("Tic-Tak-Toe")

board=["-","-","-",
		"-","-","-"
		,"-","-","-"]

#                                    game counter section------AND DISPLAY--------start
master_count=open("C:/Python27/count.txt",'r')
#master_count.write("1")
game_counter=master_count.read()
master_count.close()
dog=int(game_counter)
#print(type(dog))
dog+=1
#print(dog)
master_count=open("C:/Python27/count.txt",'w')
ccc=str(dog)
master_count.write(ccc)
master_count.close()

var1=StringVar()
label=Label(root,textvariable=var1,fg="red")
var1.set(ccc+"th time played the game.")
label.pack(side=TOP)


#                                    game counter section --------------END




def change1():
	global temp
	temp+=1
	if temp%2==0:
		board[0]='O'
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=30,y=20)
		check()

	else:
		board[0]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=30,y=20)
		check()


def change2():
	global temp
	temp+=1
	if temp%2==0:
		board[1]='O'
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=75,y=20)
		check()
	else:
		board[1]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=75,y=20)
		check()

def change3():
	global temp
	temp+=1
	if temp%2==0:
		board[2]='O'	
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=120,y=20)
		check()
	else:
		board[2]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=120,y=20)
		check()

def change4():
	global temp
	temp+=1
	if temp%2==0:
		board[3]='O'	
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=30,y=60)
		check()
	else:
		board[3]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=30,y=60)
		check()

def change5():
	global temp
	temp+=1
	if temp%2==0:
		board[4]='O'	
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=75,y=60)
		check()
	else:
		board[4]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=75,y=60)
		check()

def change6():
	global b6
	global temp
	temp+=1
	if temp%2==0:
		board[5]='O'	
		b6=Button(text="O",fg="red2",width=5,height=2)
		b6.place(x=120,y=60)
		check()
	else:
		board[5]='X'
		b6=Button(text="X",fg="green4",width=5,height=2)
		b6.place(x=120,y=60)
		check()

def change7():
	global temp
	temp+=1
	if temp%2==0:	
		board[6]='O'
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=30,y=100)
		check()
	else:
		board[6]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=30,y=100)
		check()

def change8():
	global temp
	temp+=1
	if temp%2==0:	
		board[7]='O'
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=75,y=100)
		check()
	else:
		board[7]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=75,y=100)
		check()

def change9():
	global temp
	temp+=1
	if temp%2==0:	
		board[8]='O'
		b=Button(text="O",fg="red2",width=5,height=2)
		b.place(x=120,y=100)
		check()
	else:
		board[8]='X'
		b=Button(text="X",fg="green4",width=5,height=2)
		b.place(x=120,y=100)
		check()


#first row
b1=Button(text="1",command=change1,width=5,height=2,bg="grey")
b1.place(x=30,y=20)

b=Button(text="2",command=change2,width=5,height=2,bg="grey")
b.place(x=75,y=20)

b=Button(text="3",command=change3,width=5,height=2,bg="grey")
b.place(x=120,y=20)


#2nd row
b=Button(text="4",command=change4,width=5,height=2,bg="grey")
b.place(x=30,y=60)

b=Button(text="5",command=change5,width=5,height=2,bg="grey")
b.place(x=75,y=60)

b=Button(text="6",command=change6,width=5,height=2,bg="grey")
b.place(x=120,y=60)


#3rd row
b=Button(text="7",command=change7,width=5,height=2,bg="grey")
b.place(x=30,y=100)

b=Button(text="8",command=change8,width=5,height=2,bg="grey")
b.place(x=75,y=100)

b=Button(text="9",command=change9,width=5,height=2,bg="grey")
b.place(x=120,y=100)

#data Analysis and graph+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def showdata():
		mycursor.execute("select count(*) from data")
		counter=mycursor.fetchall()

		mycursor.execute("select * from data")
		result=mycursor.fetchall()
		sss=str(result)
		#print(sss)
		#print(type(sss))
		global abhi
		abhi=Toplevel()
		abhi.geometry("200x500")
		res=list(reversed(result))
		for i in range(int(counter[0][0])):
			for j in range(2):
				var=StringVar()
				label=Label(abhi,textvariable=var,relief=RAISED,padx=15)
				#str=list(result[i])
				#x=str.split()
				#print(result[i][j])
				var.set(res[i][j])
				label.grid(row=i,column=j)

def delete():
	mycursor.execute("delete from data")
	mydb.commit()
	sumx=0
	sumo=0
	sumtie=0
	x_counter=0
	o_counter=0
	tie_counter=0
	
	
def statistic():
	mycursor.execute("select count(*) from data where win='X won'")
	sumx=mycursor.fetchall()
	mycursor.execute("select count(*) from data where win='O won'")
	sumo=mycursor.fetchall()
	mycursor.execute("select count(*) from data where win='Tie'")
	sumtie=mycursor.fetchall()
	labels='X won','O won','Tie'
	size=[sumx[0][0],sumo[0][0],sumtie[0][0]]
	
	m=max(size)
	if m==sumx[0][0]:
		explode=[0.05,0,0]
	if m==sumo[0][0]:
		explode=[0,0.1,0]
	if m==sumtie[0][0]:
		explode=[0,0,0.1]

	y=['x won','O won','Tie',]
	plt.subplot(2,1,1)
	plt.bar(y,size,align='center',alpha=0.5)
	plt.ylabel('Times won')
	#plt.pie(y)
	plt.title('Statistic')
	plt.subplot(2,1,2)
	#plt.title('Pie Graph')
	plt.pie(size,labels=labels,shadow=True,autopct='%1.1f%%',explode=explode)

	plt.show()
	#print(x_counter,o_counter,tie_counter)

def email():
	mycursor.execute("select * from data")
	content=mycursor.fetchall()
	attachment=open("C:/Python27/test11.txt",'w')
	for i in content:
		for j in i:
			attachment.write(j+" ")
		attachment.write("\n")
	##f=open("C:/Python27/test11.txt",'r')
	#print(f.read())
	##msg = MIMEText(f.read())
	attachment.close()


	##msg['Subject'] = 'The contents of %s' % textfile
	##msg['From'] = me
	##msg['To'] = you


	#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
	import smtplib 
	from email.mime.multipart import MIMEMultipart 
	from email.mime.text import MIMEText 
	from email.mime.base import MIMEBase 
	from email import encoders 

	fromaddr = "sahabhisek11@gmail.com"
	toaddr = e.get()

	# instance of MIMEMultipart 
	msg = MIMEMultipart() 

	# storing the senders email address 
	msg['From'] = fromaddr 

	# storing the receivers email address 
	msg['To'] = toaddr 

	# storing the subject 
	msg['Subject'] = "History of game"

	# string to store the body of the mail 
	body = "just checking"

	# attach the body with the msg instance 
	msg.attach(MIMEText(body, 'plain')) 

	# open the file to be sent 
	filename = "test11.txt"
	attachment = open("C:/Python27/test11.txt", "r") 

	# instance of MIMEBase and named as p 
	p = MIMEBase('application', 'octet-stream') 

	# To change the payload into encoded form 
	p.set_payload((attachment).read()) 

	# encode into base64 
	encoders.encode_base64(p) 

	p.add_header('Content-Disposition', "attachment; filename = %s\n" % filename) 

	# attach the instance 'p' to instance 'msg' 
	msg.attach(p) 

	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

	# start TLS for security 
	s.starttls() 

	# Authentication 
	s.login(fromaddr, "TYPE YOUR GMAIL PASSWORD HERE") 

	# Converts the Multipart msg into a string 
	text = msg.as_string() 

	# sending the mail 
	s.sendmail(fromaddr, toaddr, text) 

	# terminating the session 
	s.quit() 
	
	#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	#s = smtplib.SMTP('smtp.gamil.com',587)
	#s.sendmail(me, [you], msg.as_string())
	#s.quit()


	
	#sender="sahabhisek11@gmail.com"
	#rec="abhisek301298@gmail.com"
	#passwd="abhisekSAH@11"
	#msg="heeeeeeeeeee hooooooooo"

	#server = smtplib.SMTP('smtp.gmail.com',587)
	#server.starttls()
	#server.login(sender,passwd)
	#print("successful")
	#server.sendmail(sender,rec,msg)
	#print("done")
#END--------END-----------END EMAIL PORTION
frame=Frame(root)
frame.place(x=200,y=30)

#bottomframe=Frame(root)
#bottomframe.pack(side= LEFT)

ab=Button(frame,text="Show History",padx=54,bg="thistle2",command=showdata)
ab.pack(side=TOP)

ab=Button(frame,text="Clear History",padx=55,bg="thistle2",command=delete)
ab.pack(side=TOP)

ab=Button(frame,text="Send data to me",padx=50,bg="thistle2",command=email)
ab.pack(side=BOTTOM)
e=Entry(frame,width=30,fg="grey1",bg="OliveDrab1")
e.pack(side=BOTTOM)
ab=Button(frame,text="Statistic graph",padx=51,bg="thistle2",command=statistic)
ab.pack(side=BOTTOM)
#End of graph++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#check winner
def check_winner():
	check_row()
	check_col()
	check_dia()
	check_tie()

#-------------------------row---------

def check_row():
	p=board[0]==board[1]==board[2]!='-'
	q=board[3]==board[4]==board[5]!='-'
	r=board[6]==board[7]==board[8]!='-'
	
	global still_running
	if (p or q or r ):
		still_running=False
		


#------------------------col---------

def check_col():
	p=board[0]==board[3]==board[6]!='-'
	q=board[1]==board[4]==board[7]!='-'
	r=board[2]==board[5]==board[8]!='-'
	global still_running
	if p or q or r :
		still_running=False
#------------------------dia------------

def check_dia():
	p=board[0]==board[4]==board[8]!='-'
	q=board[2]==board[4]==board[6]!='-'
	global still_running
	if p or q :
		still_running=False
#==================print tie

def check_tie():
	global still_running
	global temp
	if '-' not in board:
		if still_running :
			#global still_running
			still_running=False
			global t
			t=10
			#print("The game is Tie")


def print_winner():
	global answer
	global t
	if t==10:
		#print("The game is tie\n\n")
		#insert data into my sql____________________________________________________________
		mycursor.execute("insert into data (win,date) values ('Tie',current_timestamp)")
		mydb.commit()
		mycursor.close()
	
		answer=messagebox.askquestion("Tic-Tak-Toe","The game is tie\nWant to play again??")
		ans()
	else:
		if temp%2==0:
			#print("O won\n\n")
			mycursor.execute("insert into data (win,date) values ('O won',current_timestamp)")
			mydb.commit()
			mycursor.close()
			
			answer=messagebox.askquestion("Tic-Tak-Toe","O Won the game\nWant to play again??")
			ans()
		else:
			#print("X won\n\n")
			mycursor.execute("insert into data (win,date) values ('X won',current_timestamp)")
			mydb.commit()
			mycursor.close()
			
			answer=messagebox.askquestion("Tic-Tak-Toe","X Won the game\nWant to Play again??")
			ans()


#just checking
def display():
	print(board[0]+"|"+board[1]+"|"+board[2])
	print(board[3]+"|"+board[4]+"|"+board[5])
	print(board[6]+"|"+board[7]+"|"+board[8])
	print("\n")



def check():
	#display()
	check_winner()
	if still_running==False:
		print_winner()
		#root.destroy()


def ans():
	if answer=='yes':
		root.destroy()
		os.startfile("C:/Users/HOME/tictaktoe_3rdUpdate.py")
	
	else:
		root.destroy()



root.mainloop()

