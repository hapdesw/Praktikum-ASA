
inputKata = str(input())
panjangKata = int(input())

def tugasSekolah(inputKata, panjangKata):
    ulangHuruf = (inputKata * (panjangKata // len(inputKata) + 1)) [:panjangKata]
    print(ulangHuruf)
    hitungVokal = 0
    for i in ulangHuruf:
        if (i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o'):
            hitungVokal += 1
    print (hitungVokal)
tugasSekolah(inputKata, panjangKata)