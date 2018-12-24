a = "Anbarasan"
a = list("Anbarasan")
j = 1
l = len(a)

for i in range(len(a)):
  a.extend(a[-(i+j)])
  j+=1
a = ''.join(a[l:])

print(a)
    
    
