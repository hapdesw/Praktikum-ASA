n = int(input())

def kombinasiPw(n, pw = ''):
    if len(pw) == n:
        if 'bb' not in pw:
            print(pw)
    else:
        kombinasiPw(n, pw + 'a')
        kombinasiPw(n, pw + 'b')

kombinasiPw(n)
