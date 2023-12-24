t = int(input())
while t :
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    x, y = map(int, input().split())
 
    if b == d or b == y or d == y:
        if b == d and b > y:
            # print('0')
            print(abs(c-a))
        elif d == y and d > b:
            # print('0')
            print(abs(x-c))
        elif b == y and b > d:
            # print('0')
            print(abs(x-a))
        else:
            print(0)
    else:
        print(0)
    t -= 1
    

    
