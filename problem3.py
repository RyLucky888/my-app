import random
def randN(N):
    temp=[]
    def genRandInt():
        i=random.randint(1,N)
        if i not in temp:
            temp.append(i)
            return i
        if len(emp) >=N:
            temp.clear()
    return genRandInt()

if __name__ == '__main__':
    r = randN(5)
    r()
        
    
