




def getCodewords():
    
    codewords = []

    print("Enter the number of codeword\n")

    n = int(input())

    for i in range(n):
        codeword = input()
        codewords.append(codeword)
    
    print("Entered Codewords\n")
    
    for i in range(n):
        print(codewords[i])
        
        
    return codewords


def getMinHamDist(codewords):
    
    HamDist = []
    
    
    for i in range(len(codewords)):
        for j in range(i+1,len(codewords)):
            
            
            mismatchCount = 0
            
            for k,l in zip(codewords[i],codewords[j]):
                mismatchCount += (k!=l)
                
            HamDist.append(mismatchCount)
    
    return HamDist


codewords = getCodewords();

HamDist = getMinHamDist(codewords)

print(f"Minimum Hamming Distance Between The Codewords : {min(HamDist)}")


    
    

    
    
    
    
    
