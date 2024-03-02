n = int(input())

def tamanBermain(n):
    for i in range(1, n+1):
        if (i % 3 == 0 or i % 5 == 0):
            if (i % 3 == 0 and i % 5 == 0):
                print("SleepyJoe")
            elif (i % 3 == 0):
                print("Sleepy")
            elif (i % 5 == 0):
                print("Joe")
        else:
            print(i)

tamanBermain(n)