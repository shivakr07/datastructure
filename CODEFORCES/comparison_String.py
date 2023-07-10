t = int(input())
while t :
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x = int(input())
        a.append(x)
        y = int(input())
        b.append(y)
    ptr = n-1
    ans = 0
    while ptr >= 0:
        if a[ptr] > b[ptr]:
            ans += a[ptr]
            ptr 
        else:
            ans += a[ptr]
            break
    print(ans)
    
    t -= 1