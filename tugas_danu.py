x = input('masukkan bintang pertama: ')
x = int(x)
j=x

for i in range(1,x+1):
	print(('_'*j)+('#'*i))
	j-=1

