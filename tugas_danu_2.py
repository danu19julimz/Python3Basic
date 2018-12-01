x = input('masukkan bintang pertama: ')
x = int(x)
j=x
y =x-1
z = x-2
s=1
for i in range(1,x+1):
	if i==1 or i==x:
		print(('_'*j)+('#_'*i))
	else:
		print(('_'*j)+('#')+(' '*s)+('#_'))
		s+=2
	i+=1
	j-=1
	
	
