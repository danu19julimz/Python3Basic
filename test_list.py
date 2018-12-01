y = input('jumlah nama peserta: ')
y = int(y)

names=[]
for i in range(0,y):
	name=input('input nama peserta: ')
	names.append(name)

print('peserta sebanyak {}, {}'.format(y, names))

for name in names:
	print(names.index(name))
	print(name)

change_index = input('pilih index nama yang akan dirubah')
updated_name = input('masukkan nama: ')

index = int(change_index)
names[index] = updated_name

print('index ke %s berhasil diupdate menjadi %s' % (index, updated_name))

print(names)
