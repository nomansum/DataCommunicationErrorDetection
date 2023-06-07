def binary_sum(numbers):
    result = 0
    for i in numbers:
        result += i
    binary_result = bin(result)[2:]  # Convert integer to binary string (remove '0b' prefix)
    return binary_result


def checksumGenerator(numbers,bitLength,fl):
    
    result = binary_sum(numbers)
        
    result1 = result[-bitLength:]  
        
    while(len(result)> bitLength ):
        
        result1 = result[-bitLength:]     
        
        result = result[:-bitLength]
        
        result = int(result,2) + int(result1,2) 
    
        result = bin(result)[2:]  
        
    
    
    result1 = result;
    
    if( len(result) <bitLength ):
        
        result = ''.join('0' for i in range(bitLength-len(result)))
        
        result+=result1       
    
    wrapSum = result
    
    if fl:
        return wrapSum
    
    print(f"Wrapped Sum is {result}\n") 
    
    
    result = int(result,2)
        
    checkSum = ~result & int('1'*bitLength,2)
    
    
    print(f"CheckSum Is : {checkSum}")
    
    return wrapSum

def validateChecksum(numbers,checksum,bitLength):
    numbers.append(checksum)
    
    wrapSumOnReceiverEnd = checksumGenerator(numbers,bitLength,True)
    
    print(f"Wrapped Sum on Receiver side is {wrapSumOnReceiverEnd}\n") 
    
    result = int(wrapSumOnReceiverEnd,2)
        
    validator = ~result & int('1'*bitLength,2)
    
    if validator == 0:
        print("Checksum technique has no loss\n")
    
    else:
        print("Checksum Has Error\n")
    
    
    
    
    
    
    

    
    
    
    
    
n =int(input("Enter the bit length\n"))

m =int(input("enter how many numbers ?\n"))

numbers = []

for i in range(m):
    
    val = int(input(f"Enter the {i+1} th number\n"))
    
    numbers.append(val)

checksumGenerator(numbers,n,False)
validateChecksum(numbers,9,n)

