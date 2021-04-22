'''Implement FA for the Regular Expression:
(0 + 1)*1(0+1)*1(0+1)*1(0+1)* .
Print the transition table and for input string ,
show whether it is valid or invalid.'''
def checklanguage(exp):
	for i in exp:
		if(i not in Lang):
			return False
	return True


def checkfinalstate(checkstate):
	if(checkstate[3]):
		return True
	return False


def printstate(exp):
	s=0
	print("\t\tSTATE TABLE")
	print("------------------------------")
	print("|Current-State"+"\t"+"| Element\t")
	print("------------------------------")
	for i in exp:
		if(i=='1'):
			s+=1
		print("|\t"+str(states[s])+"\t\t\t|\t"+i+"\t|")
	print("------------------------------")

# number of input for checking
tc = int(input())
states = ['q0','q1','q2','q3']
Lang = ['1','0']
flg = False

while tc:
	checkstate = [False]*4
	exp = list(input())
	print()
	print("------------------------------")
	print("Expression:"+''.join([str(elem) for elem in exp]))
	print("------------------------------")
	
	lan = checklanguage(exp)
	if(lan):
		c1 = exp.count('1')
		if(c1 == 0):
			checkstate[0]= True
		elif(c1 == 1):
			checkstate[1]= True
		elif(c1 == 2):
			checkstate[2]= True
		else:
			checkstate[3]= True
		
		printstate(exp)
		fstate = checkfinalstate(checkstate)
		print(''.join([str(elem) for elem in exp]),end=" ")
		print("is",end=" ")
		if(fstate):
			print("Valid Expression")
		else:
			print("Invalid Expression")

	else:
		print("Invalid Language")
	print("------------------------------")
	tc-=1
