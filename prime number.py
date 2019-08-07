prime=int(input("Enter your number\n"))
if prime>1:
	for i in range(prime):
		if (prime % 2)==0:
			print(prime,"is not a prime number")
			break
	else:
		print(prime," It is a prime number")
