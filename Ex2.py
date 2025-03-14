def recVirusSpread(N,P):
    if(N>0):#while Number of hours > 0 the recurseve function still call
        return P+recVirusSpread(N-1,P*2)#we increase the hours and multiolie by two the number of PC and the number of PC ifected in that hour
    return P#if N=0 we return the number of effected PC
#O(n)    
    
    
def iterVirusSpread(N,P):
    for i in range(0,N):
        P=P*2+1
    return P
#O(n)



N=int(input("give the number of hours"))
P=int(input("give the number of  infected computers"))
print(recVirusSpread(N,P))
print(iterVirusSpread(N,P))

#the recurseve function is more complicated