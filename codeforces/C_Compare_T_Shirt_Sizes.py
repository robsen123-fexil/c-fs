t = int(input())
for i in range(t):
    a, b = input().split()
    if a == b:
        print('=')
        continue
    if a == 'M':
        if 'S' in b:
            print('>')
        else: 
            print('<')
        continue
    if b == 'M':
        if 'S' in a:
            print('<')
        else:  
            print('>')
        continue
    if 'S' in a:
        if 'M' in b or'L' in b:
            print('<')
        else:         
            if len(a) < len(b):
                print('>')
            else:
                print('<')
    elif 'L' in a:
        if 'M' in b or 'S' in b:
            print('>')
        else:    
            if len(a) < len(b):
                print('<')
            else:
                print('>')
