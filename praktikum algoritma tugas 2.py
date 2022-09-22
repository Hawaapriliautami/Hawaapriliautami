b = float(input('masukkan Panjang: '))
c = float(input('masukkan Lebar: '))
d = input('pilih satuan(meter/inci: ')

if (d == 'meter') :
    h = b * c
elif (d == 'inci') :
    h = b * c * 39.37
    
print ('\npanjang ruangan = ', b)
print ('Lebar ruangan = ', c)
print ('Luas ruangan = ',h,d)

    