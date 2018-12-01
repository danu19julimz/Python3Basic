x = input('masukkan bintangnya: ')
x = int(x)
s = x
p = x-1
l=1
z=0
for i in range(0,x):
	print('')
	for j in range(0,s):
		print('*',end='')
	for k in range(0,l):
		if k==0 or i==p:	
			print('#',end='')
		elif k!=0:
			print('_',end='')
	for m in range(0,z):
		print('#',end='')	
	s-=1
	i+=1
	l+=1
	z+=1
print('\r')
	


