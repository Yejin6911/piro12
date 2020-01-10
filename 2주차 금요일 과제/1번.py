def find(n):
    result = 0
    for i in range(n):
        sum = i
        for x in str(i):
            sum += int(x)
        if(sum==n):
            result = i
            break
    return result

N = int(input())
print(find(N))
