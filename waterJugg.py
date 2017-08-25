import math
answer=[]
def gcd(x,y):
	if y==0:
		return x
	return gcd(y,x%y)	

def isSolnAvailable(capacity1,capacity2,finalCapacity):
	a=(int)(gcd(capacity1,capacity2)/finalCapacity)
	print(a)
	if a!=0:
		return True
	return False

def pour(capacity1,capacity2,finalCapacity):
	currCapacity1=capacity1
	currCapacity2=0
	answer.append([currCapacity1,currCapacity2])
	stepCount=0
	while currCapacity1!=finalCapacity or currCapacity2!=finalCapacity:
		temp=min(currCapacity1,capacity2-currCapacity2)
		currCapacity1-=temp
		currCapacity2+=temp
		answer.append([currCapacity1,currCapacity2])
		stepCount+=1

		if currCapacity1==finalCapacity or currCapacity2==finalCapacity:
			break
		if currCapacity1==0:
			currCapacity1=capacity1
			answer.append([currCapacity1,currCapacity2])
			stepCount+=1

		if currCapacity2==capacity2:
			currCapacity2=0
			answer.append([currCapacity1,currCapacity2])
			stepCount+=1
	return stepCount


m=input("Capacity of Jug 1 ? : ")
n=input("Capacity of Jug 2 ? :")
# print("Enter final capacity if known else 0")
# mF=input("Final Capacity of Jug 1 ?")
# nF=input("Final Capacity of Jug 2 ?")
d=input("Final capacity to be measured ? : ")

'''
Diophantime equation mx+ny=d
m is capacity 1
n is capacity 2
d is capacity to be measured

'''
if isSolnAvailable(m,n,d):
	print("Solution Available\n")
else: 
	print("Solution Not Available\n")

pour(m,n,d)
print(answer)
answer=[]
pour(n,m,d)
print(answer)