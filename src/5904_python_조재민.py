import sys
Index = int(sys.stdin.readline())
seq = 0
length = 3

while Index > length : 
    seq += 1
    length = length*2 + seq + 3

def recursion(seq, len, index):
    if(seq == 0):
        return 'm' if (index == 1) else 'o'

    len = (len-3-seq) // 2
    seq -= 1
        
    if (index <= len):
        return recursion(seq, len, index)
    elif (index == len + 1):
        return 'm'
    elif (index > len + seq + 4):
        return recursion(seq, len, index-len-seq-4)
    else:
        return 'o'
    

print(recursion(seq, length, Index))
