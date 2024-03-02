
kalimat = str(input())

def hitungVokal(kalimat):
    count = 0
    for i in kalimat:
        if (i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o' or 
            i == 'A' or i == 'I' or i == 'U' or i == 'E' or i == 'O'):
            count += 1
    print (count)
hitungVokal(kalimat)