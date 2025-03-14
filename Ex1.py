def inputCoins(coins):
    while(True):#loop for to enter any number of coins
        x=int(input("give me a coin"))
        coins.append(x)#add the coin to the list
        c=input("there are other coin y/n")#ask for complete compuling or exit
        while(c!="y" and c!="n"):#ensure that user enter yess for comleting and no to exit
            c=input("there are other coin y/n")
        if(c=="n"):
            return

def computeCoins(coins,amount):
    if(amount==0):#Base Case
        return 
    elif(coins[0]<=amount):
        print(coins[0],"+",end="")#print without new line
        return computeCoins(coins,amount-coins[0])
    coins.pop(0)#elemenate the first coin because it is begere then the rest ofammount
    return computeCoins(coins,amount)
#O(n)



coins=[]#initialize the list of coins
coins=inputCoins(coins)#fill the list
coins=[1,5,10,25,50,100]
amount=int(input("give the ammount"))#read the ammount
coins.sort(reverse=True)
res=computeCoins(coins,amount)
#the recursion is not the best approach because it take more space complexity and don't minmaise the time complexity