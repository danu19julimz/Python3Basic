x = input('masukkan x nya:')
x = int(x)
z=x
a=''
b=''
p=x-1
for i in range(1,x+1):
	if i==1:	
		for j in range(1,x+1):
			a+=str(i)
			i+=1
		print(a)		
	elif i==x:
		for k in range(1,x+1):
			b+=str(z)
			z-=1
		print(b)
	else:
		
		print(str(i)+(' '*(x-2))+str(p))
		p-=1
