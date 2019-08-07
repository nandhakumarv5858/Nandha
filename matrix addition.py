a =[[1,2,3],
   [3,4,3],
   [4,3,2]]
   
b =[[5,6,4],
   [4,8,6],
   [5,9,2]]
   
result =[[0,0,0],
		[0,0,0],
		[0,0,0]]
for i in range (len (a)):
	for j in range (len (a[0])):
		result[i][j] = a [i][j] + b [i][j]
for f in result:	
	print(f)	
		
