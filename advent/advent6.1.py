aux = ''
z=','.join(iter(input, aux))
map1=z.split(',')

map2=[]
for x in map1:
  y=x.index(')')
  a=x[0:y]
  b=x[y+1:]
  map2.append((a,b))

map2.reverse()

total=0
for planet in map2:
  line=0
  y=planet[1]
  i=0
  while i<len(map2):
    z=map2[i]
    if y == z[1]:
      line+=1
      y=z[0]
      i=0
    else:
      i+=1
  total+=line

print(total)
