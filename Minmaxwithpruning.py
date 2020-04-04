import random
import select

r=0

def minimax(n,m):
	global r
	if m==1:
		state=0
		if n==1:
			return 0
		if n==2: 
			return 1
		for i in range(n-1,0,-1):
			if i<n-3:
				break
			state=minimax(i,0)
			if state==1:
				r=(n-i)
				break
		return state
	else:
		state=1
		if n==1:
			return 1
		if n==2:
			return 0
		for i in range(n-1,0,-1):
			if i<n-3:
				break
			state=minimax(i,1)
			if state==0:
				break
		return state

print("1. Type 1 for playing against AI\n2. Type 2 for AI vs AI")
x=int(input())
print("Enter no. of sticks")
stick=int(input())
if x==1:
	choice=int(random.choice([0,1]))
	if choice==1:
		print("Your turn")
	else:
		print("AI's chance")
	turn=choice
	while 1:
		print("Number of sticks left: ",stick)
		if turn==1:
			print("select the number of sticks(from 1 to3):")
			while 1:
				v=int(input())
				if v>=1 and v<=3:
					stick=stick-v
					break
				print("enter a value from 1 to 3:")
			turn=0
		else:
			r=0
			minimax(stick,1)
			if r!=0:
				stick=stick-r
				print("AI picked ",r," sticks")
			else:
				print("AI picked 1 stick")
				stick=stick-1
			turn=1
		if stick==1:
			if turn==1:
				print("AI won")
			else:
				print("You won")
			break
else:
	choice=int(random.choice([0,1]))
	turn=int(choice)
	while 1:
		print("Number of sticks left: ",stick)
		if turn==0:
			minimax(stick,1)
			stick=stick-r
			print("AI",turn+1," picked ",r," sticks")
			turn=1
		else:
			minimax(stick,1)
			stick=stick-r
			print("AI",turn+1," picked ",r," sticks")
			turn=0
		if stick==1:
			if turn==1:
				print("AI1 won")
			else:
				print("AI2 won")
			break
