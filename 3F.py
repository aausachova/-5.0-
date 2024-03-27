wordsset = set(input().split())
strings = input().split()
for s in strings: 
    prefix = ''
    for j in range(len(s)):
        prefix += s[j]
        if prefix in wordsset:
            print(prefix, end= ' ')
            break
    else:
        print(s, end=' ')
      
