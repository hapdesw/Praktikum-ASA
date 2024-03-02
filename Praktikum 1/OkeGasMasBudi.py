n = int(input())
k = eval(input())

def okeGas():
    tabungan = 0
    setengah = False
    for i in range(len(k)):
        tabungan += k[i]
        if (not setengah and tabungan >= n//2 and tabungan < n) :
            print("Sedikit lagi! Tabungan kamu udah setengahnya dalam waktu %d hari." % (i+1))
            setengah = True
        elif (tabungan >= n):
            print("Keren! Tabungan kamu cukup dalam waktu %d hari." % (i+1))
            break

okeGas()