st = "rhdt:246"
ind = 0
for i in range(len(st)):
    if st[i] == ':':
        ind = i
        break
temp = "".join(list(st)[ind+1 : ])
temp_rev = list(st)[:ind]
print(temp)
print(temp_rev)

num = 0
for i in temp:
    num += int(i)**2

if num % 2 == 0:
    x = temp_rev.pop(0)
    temp_rev.append(x)
    st = "".join(temp_rev)
else:
    x = temp_rev.pop()
    y = temp_rev.pop()
    st = x + y + "".join(temp_rev)
print(st)
    
# -------------------------------------------------

ex = "9@a42&516"
# o/p = 492561
print("492561")
nums = [0,1,2,3,4,5,6,7,8,9]
small = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
symbols = ['@','#','*','$','&']
capital = []
count = 0
for i in ex:
    if i in small or i in nums:
        pass
    else:
        count += 1

odds = []
even = []
for i in ex:
    if i not in symbols and i not in small:
        if int(i) % 2 == 0:
            even.append(int(i))
        else:
            odds.append(int(i))
ans = []
if count % 2 == 0:
    i = 0
    j = 0
    while i < len(even) and j < len(odds):
        ans.append(even[i])
        ans.append(odds[j])
        i+=1
        j += 1
    while i < len(even):
        ans.append(i)
    while j < len(odds):
        ans.append(odds[j])
print(ans)

# ----------------------------------
mat = [[0,7,6],
       [9,0,1],
       [4,3,0]]

for i in mat:
    data = 15 - sum(i)
    for j in range(len(mat)):
        if i[j] == 0:
            i[j] = data
print(mat)
mt = [[0,1,1],
      [1,0,1],
      [1,1,0]]


