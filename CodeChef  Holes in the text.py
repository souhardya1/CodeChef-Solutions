t=int(input())
one=['A','O','P','R','D']

for i in range(t):
    n=input().strip().upper()
    c=0
    for i in range(len(n)):
        if n[i]=='B':
            c=c+2
        if n[i] in one:
            c=c+1
    print(c)
            
    