def tailRecFact(n):
    if(n==1):
        return 1
    return n*tailRecFact(n-1)
#O(n)

def headRecFact(n):
    if(n>1):
        return n*headRecFact(n-1)
    return 1
#O(n)


n=int(input("give a number"))
print(tailRecFact(n))
print(headRecFact(n))

#the tail version compare with 1 before doing any thing that optmize the space complexty