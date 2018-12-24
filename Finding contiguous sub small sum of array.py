from sys import maxsize
lst = [3, 4, -2, -3, -1, 7, -5]

smallsum = maxsize
final_smallsum = maxsize

for i in range(len(lst)):
  
  if(smallsum > 0):

    smallsum = lst[i]
    
  else:
    
    smallsum += lst[i]
    
  final_smallsum = min(smallsum, final_smallsum)


print("final_smallsum: ", final_smallsum)
