#Problem:
#Write Encode and decoder functions for return outputs as like below:
#Input: String, key
#Output: endcoded or decoded string
def encoder(msg,key):
    
    lst = [int(i) for i in key]
    res = []
    temp = []
    lenk = len(key)
    lenm = len(msg)
    if(lenk<=lenm):
        for i in range(lenk):
            temp.append(msg[i]*lst[i])
    
        res = temp+list(msg[i+1:])
        res = ''.join(res)
    
    else:
        for j in range(lenm):
            temp.append(msg[j]*lst[j])
    
        res = temp
        res = ''.join(res)
        
    return res
    
def decoder(msg, key):
    
    empty = ''
    lst = [int(i) for i in key]
    for i in lst:
        tmp = msg[:i]
        empty+=tmp[0]
        msg = msg.replace(tmp, '',1)

    return empty+msg

def main():
    flag = int(input("Enter the flag: "))
    msg  = input("Enter the message: ")
    key  = input("Enter the key: ")
    if(flag == 1):
        result = encoder(msg,key)
        print("Encoded String: ", result)
    elif(flag == 2):
        result = decoder(msg, key)
        print("decoded String: ", result)
    else:
        print("Invalid Input")
    

if __name__ == '__main__':
    main()
    

