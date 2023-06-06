

def CRC_Generator(dataword,divisor):
    
    
    remainderLength = len(divisor) - 1
    
    dividend = dataword + ''.join('0' for i in range(remainderLength))
    
    print(f"Dataword is :{dataword}\n  divisor is : {divisor}\n  divident is : {dividend}\n")

    remainder = dividend[:remainderLength]
    
    for i in range(remainderLength,len(dividend)):
        
        remainder += dividend[i];
        
        if remainder[0] != '0':
            
            updatedRemainder = ''
            
            for x,y in zip(remainder,divisor):
                
                updatedRemainder += str(int(x!=y))
                
            remainder = updatedRemainder    
        remainder = remainder[1:]
        
        
    codeword = dataword + remainder
    
    print(f"The codeword is :{codeword}\n The Remainder is : {remainder}\n")

def validateCRC(codeword,divisor):
    
    remainderLength = len(divisor) - 1
    
    dividend = codeword;
    
    validator = ''.join('0' for i in range(remainderLength))
    
    remainder = dividend[:remainderLength]
    
    for i in range(remainderLength,len(dividend)):
        
        remainder += dividend[i];
        
        if remainder[0] != '0':
            
            updatedRemainder = ''
            
            for x,y in zip(remainder,divisor):
                
                updatedRemainder += str(int(x!=y))
                
            remainder = updatedRemainder    
        remainder = remainder[1:]
        
    if remainder == validator:
        print("No corrupt data were found CRC generated successfully\n")
    else:
        print("Codeword is corrupted\n")
        
        
while(True):
    
    print('1. Generate Codeword using CRC\n')
    print('2. Check the codeword for CRC\n')
    print('3. Exit\n')
    choice = int(input('Choose a type: \n'))
    
    
    if choice==3:
        break;
    
    else:
        data = input("Enter The Data\n")
        divisor = input("Enter The Divisor\n")
        
        if choice == 1:
            CRC_Generator(data,divisor)
        else:
            validateCRC(data,divisor)
    
    

    
