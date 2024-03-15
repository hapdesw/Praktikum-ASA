x = int(input())
y = [int(i) for i in input().split()]

def subArrayMaks():
    maks = float('-inf')
    start = 0
    end = 0
    for i in range(len(y)):
        hitung = 0
        for j in range(i, len(y)):
            hitung += y[j]
            if (hitung > maks):
                maks = hitung
                start = i
                end = j
    print(f"Subarray dengan jumlah maksimum: {y[start:end+1]} dengan jumlah maksimum {maks}")

subArrayMaks(x, y)
