from Tkinter import *
import tkMessageBox
global temp
temp=0
t=0
global still_running
still_running=True
root= Tk()

root.geometry("200x500")
root.maxsize(200,200)
root.minsize(200,200)
root.title("Tic-Tak-Toe")

board=["-","-","-",
		"-","-","-"
		,"-","-","-"]



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
	global t
	if t==10:
		#print("The game is tie\n\n")
		tkMessageBox.showinfo("Tic-Tak-Toe","The game is tie\nThank You!!!")
	else:
		if temp%2==0:
			#print("O won\n\n")
			tkMessageBox.showinfo("Tic-Tak-Toe","O Won the game\nThank You!!!")
		else:
			#print("X won\n\n")
			tkMessageBox.showinfo("Tic-Tak-Toe","X Won the game\nThank You!!!")

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
		root.destroy()


root.mainloop()

