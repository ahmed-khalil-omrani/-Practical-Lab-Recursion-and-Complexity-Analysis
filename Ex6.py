def receiver(n):
    print("receiver: I will speak",n,"times")
    call(n-1)

def caller(n):
    print("caller: I will speak",n,"times")
    receiver(n-1)
def call(n):
    if(n<0):
        return
    caller(n)

#O(n)







n=int(input("give the number of sentences"))
call(n)