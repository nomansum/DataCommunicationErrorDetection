###EVEN PARITY Q2



def genCodeword(even):
    x=0
    if even==False:
        x=1
        
        
    
    dataword = input('Enter The Dataword\n')
    
    parityBit = (dataword.count('1') + x) % 2
    
    print(f"Parity Bit is : {parityBit}\n")
    
    codeword = dataword + str(parityBit)
    
    print(f"The Generated Codeword is : {codeword}\n")


def validateCodeword(even):
    
    x=0
    if even==False:
        x=1
    
    codeword = input("Enter The Codeword\n")
    
    parityBit = int(codeword[-1])
    
    dataword = codeword[:-1]
    
    print(f"The Dataword Extracted Is : {dataword}\n")
    
    actualParity = ( dataword.count('1') + x ) % 2
    
    if actualParity == parityBit:
        
        print("The Codeword Is Perfectly Generated\n")
        
    else:
        print("Codeword Corrupted\n")
    


n = int(input("Enter the number of dataword & codeword to be generated & validated\n"))
print('1. Generate Codeword using Even parity-bit\n')
print('2. Generate Codeword using Odd parity-bit\n')

option = int(input("choose option\n"))

even = False
    
    
if option == 1:
    even = True
    

for i in range(n):
   

    
    print('1. Generate Codeword using parity-bit')
    print('2. Check the codeword for parity-bit')
    choice = int(input('Choose a type: '))
    if choice==1:
        
        genCodeword(even)
    else:
        
        validateCodeword(even)
    
    
    


