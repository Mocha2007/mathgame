import random,time
while 1:
	difficulty=int(input("Welcome to Mocha's Math Game.\nYour score is 2,000 divided by your time to correctly solve 10 random questions.\nEnter a difficulty (1,2,3) to start: "))
	score=0
	begin=time.time()
	while score<10:
		#difficulty
		if difficulty==1:
			puzzle=random.randint(1,4)
		elif difficulty==2:
			puzzle=random.randint(1,6)
		elif difficulty==3:
			puzzle=random.randint(1,11)
		#puzzle choice
		if puzzle==1:
			#addition puzzle level 1
			a=random.randint(0,9)
			b=random.randint(0,9)
			try:
				guess=int(input(str(a)+"+"+str(b)+"=?"))
			except:
				pass
			if guess==a+b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==2:
			#subtraction puzzle level 1
			a=random.randint(0,9)
			b=random.randint(0,9)
			try:
				guess=int(input(str(a)+"-"+str(b)+"=?"))
			except:
				pass
			if guess==a-b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==3:
			#multiplication puzzle level 1
			a=random.randint(1,9)
			b=random.randint(1,9)
			try:
				guess=int(input(str(a)+"*"+str(b)+"=?"))
			except:
				pass
			if guess==a*b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==4:
			#division puzzle level 1
			a=random.randint(1,9)
			b=random.randint(1,9)
			try:
				guess=int(input(str(a*b)+"/"+str(b)+"=?"))
			except:
				pass
			if guess==a:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==5:
			#squares puzzle level 1
			a=random.randint(0,16)
			try:
				guess=int(input(str(a)+"^2=?"))
			except:
				pass
			if guess==a**2:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==6:
			#square root puzzle level 1
			a=random.randint(0,16)
			try:
				guess=int(input("sqrt("+str(a**2)+")=?"))
			except:
				pass
			if guess==a:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==7:
			#linear zero puzzle level 1
			m=random.randint(1,9)
			zero=random.randint(-9,9)
			try:
				guess=int(input(str(m)+"x+"+str(-m*zero)+"=0, solve for x"))
			except:
				pass
			if guess==zero:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==8:
			#addition puzzle level 2
			a=random.randint(0,19)
			b=random.randint(0,19)
			try:
				guess=int(input(str(a)+"+"+str(b)+"=?"))
			except:
				pass
			if guess==a+b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==9:
			#subtraction puzzle level 2
			a=random.randint(0,19)
			b=random.randint(0,19)
			try:
				guess=int(input(str(a)+"-"+str(b)+"=?"))
			except:
				pass
			if guess==a-b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==10:
			#multiplication puzzle level 2
			a=random.randint(10,19)
			b=random.randint(1,19)
			try:
				guess=int(input(str(a)+"*"+str(b)+"=?"))
			except:
				pass
			if guess==a*b:
				score+=1
				print("Correct!")
			else:print("Wrong!")
		elif puzzle==11:
			#division puzzle level 2
			a=random.randint(10,19)
			b=random.randint(1,19)
			try:
				guess=int(input(str(a*b)+"/"+str(b)+"=?"))
			except:
				pass
			if guess==a:
				score+=1
				print("Correct!")
			else:print("Wrong!")
	end=time.time()
	score=str(round(2000/(end-begin)))
	#recording score
	open("math.csv", "a").write("\n"+str(round(end))+","+str(difficulty)+","+score)
	#displaying
	input("Your final score is "+score+".")