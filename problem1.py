def Product(leftsideList,rightsideList):
    prod = 1
    leftsideList.extend(rightsideList)
    for i,j in enumerate(leftsideList):
        prod *=j
    return prod

def Calc(inList):
    l2=[]
    for i in range(len(inList)):
        lList = inList[0:i]
        rList = inList[i+1:]
        l2.append(Product(lList,rList))
    return l2

if __name__=='__main__':
    res = Calc([1,3,5,2,7,4])
    print(res)
    
