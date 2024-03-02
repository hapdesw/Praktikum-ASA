n = int(input())

def petualanganJanggar():
    hitung = 0
    for i in range(1, n+1):
        if (i % 2 != 0):
            print("Janggar telah memetik buah ke-%d" % i)
            hitung += 1
        else:
            print("Janggar tidak memetik buah ke-%d" % i)
    print("Jumlah buah yang dipetik Janggar = %d" % hitung)

petualanganJanggar()