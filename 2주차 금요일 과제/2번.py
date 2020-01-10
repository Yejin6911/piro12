x = int(input())
total=[]
count = 0
def make_1(x,count):
    if x==1:
        total.append(count)
    else:
        if x%3==0:
            make_1(int(x/3),count+1)
        if x%2==0:
            make_1(int(x/2),count+1)
        make_1(x-1,count+1)

def min_count(total):
    return min(total)
    
make_1(x,count)
print(min_count(total))
