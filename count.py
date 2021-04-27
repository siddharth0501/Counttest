def count(n):
    if(n==0 or n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return count(n-3) + count(n-2) + count(n-1)
n=8
print(count(n))
