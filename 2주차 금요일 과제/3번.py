vps = []

def is_vps(vps):
    for x in vps:
        l_count=0
        r_count=0
        for y in x:
            if y=='(':
                l_count+=1
            elif y==')':
                r_count+=1
        if l_count==r_count:
            print('YES')
        else:
            print('NO')
        
x = int(input())
for  i in range(x):
    vps.append(input())
    
is_vps(vps)
