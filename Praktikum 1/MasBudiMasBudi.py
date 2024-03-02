n = int(input())

def masBudi():
    toping = ["coklat", "stroberi", "keju"]
    for i in range(1, n+1):
        t = toping[(i-1) // (n//3)]
        print("Budi menaburkan topping %s di atas kue ke-%d" % (t, i))

masBudi()
