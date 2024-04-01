nama = str(input('Masukan Nama : '))
umur = int(input('Masukan Umur : '))
pekerjaan = str(input('Masukan Pekerjaan : '))
gaji = int(input('Masukan Gaji : Rp.'))
anak = int(input('Mempunyai Anak : '))
syarat = pekerjaan not in ['ASN','Polis','Pengusaha','TNI','Manager'] and gaji < 2000000 and anak < 5

if syarat:
    print('Layak Mendapatkan Bantuan')
else:
    print('Tidak Layak Mendapatkan Bantuan')

print(nama,umur,pekerjaan,gaji,anak,syarat)