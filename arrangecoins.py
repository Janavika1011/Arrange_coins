def Arrange_coins(n):
    i=1
    while n>=i:
        n-=i
        i+=1
    return i-1
n = int(input("Enter : "))
print(Arrange_coins(n))