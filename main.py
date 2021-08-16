def discount(result):
	
	if result>=5000:
		sp=result*0.05
		result=result-sp
		print("Your total price=$",result)
	elif result>=8000:
		sp=result*0.06
		result=result-sp
		print("Your total price=$",result)
	elif result>=10000:
		sp=result*0.1
		result=result-sp
		print("Your total price=$",result)
	else:
		print("Your total price=$",result)

		


			

	
length=int(input("Enter the length of the room"))
width=int(input("Enter the width of the room"))
result=length*width*20
discount(result)