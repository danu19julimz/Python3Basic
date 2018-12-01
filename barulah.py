x = input('masukkan nilai= ')
x = int(x)
p=x-1
for i in range(0,x):
	print(' ')
	for j in range(0,i+1):
		if i==2:
			print('')
		print('*',end=' ')
	i+=1	
print('\r')
