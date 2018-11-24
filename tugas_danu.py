x = input('masukkan bintang pertama: ')

x = int(x)
s = x
for i in range(0,x):
	for j in range(0,s):	
		print(".",end="")
	s = s-1
	for k in range(0,i+1):
		print("#",end="")
	for l in range(0,i+1):
		print("#",end="")
	print("\r")

