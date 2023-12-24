def sherlockAndAnagrams(s):
    # Write your code here
    s1 = ''
    s  = list(s)
    ans = 0
    for i in range(len(s)):
        temp = s[:i]
        s1 = "".join(temp)   
        temp = s[i:]
        s2 = "".join(temp)
        i,j = 0, 0
        d = {}
        for item in s1:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        count = len(d)  
        k = len(s1)
        n = len(s2)
        while j < n and len(s2) >= len(s1):
            if s2[j] in d:
                d[s2[j]] -= 1
                if d[s2[j]] == 0:
                    count -= 1
            if j-i+1 < k:
                j += 1
            elif j-i+1 == k:
                if count == 0:
                    ans += 1
                if s2[i] in d:
                    d[s2[i]] += 1
                    if d[s2[i]] == 1:
                        count += 1
                i += 1
                j += 1
    return ans

s = 'mom'
ans = sherlockAndAnagrams(s)
print(ans)