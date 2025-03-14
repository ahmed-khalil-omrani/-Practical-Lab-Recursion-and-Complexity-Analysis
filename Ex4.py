from numpy import array

def pascale(n,p):
    if(n==p)or(p==0):#base case
        return 1
    return(pascale(n-1,p-1)+pascale(n-1,p))#apply of formulla
#O(2^n)
def pascaleTringle(n):#to print te pascale triangle
    for i in range(n):#to go from 0 to n to callculate and print all the lines of the trinagle
        for j in range(0,i+1):#to go from 0 to n to print all the line of from the first value to last
            print(pascale(i,j),"",end="")
        print()#return to the line between two rows

#O(n^2)

#-----------------------------------------------iterative approach------------------------------------------
def printRes(m,n):
    for i in range(n):
        for j in range(i+1):
            print(m[i][j],"",end="")

        print()#new line    
#O(n)

def pascaleTriangleItr(n):
    m=array([[0]*n]*n)#initialise the matrix for the values
    for i in range(n):#to go from 0 to n to callculate all the lines of the trinagle
        for j in range(i+1):#to go from 0 to n 
            if(i==j)or(j==0):#to take the 1 values of the calcule
                m[i][j]=1
            else:
                if(i>0):
                    m[i][j]=m[i-1][j-1]+m[i-1][j]#to clacule the values of the lines
    printRes(m,n)#to print result in formul way
    
#O(n)





n=int(input("give n"))#to read n
pascaleTringle(n)
pascaleTriangleItr(n)
