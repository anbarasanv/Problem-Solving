lst = [3, -4, 2, -3, -1, 7, -5]

maxsum = 0
final_maxsum = 0

for i in range(len(lst)):
  maxsum +=lst[i]
  if(maxsum < 0):
    maxsum = 0
    lastIndex = 0
    firstIndex = i+1
  elif(maxsum > final_maxsum):
    final_maxsum = maxsum
    l = i
  

print("final_maxsum: ", final_maxsum)
print("first_Index: ", firstIndex," Last_Index: " ,lastIndex)
