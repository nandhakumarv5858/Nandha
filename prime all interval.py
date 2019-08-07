small_no=int(input("Enter your  small number\n"))
big_no=int(input("Enter your big number"))
for prime in range(small_no,big_no +1):
	if prime >1:
		for i in range(prime):
			if (prime % 2)==0:
				break
		else:
			print(prime)
