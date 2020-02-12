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

mapyou=[]
mapsanta=[]
you='YOU'
santa='SAN'
cross='YCH'

y=map2[1145][1]

i=0
while i<len(map2):
  z=map2[i]
  if y == z[1]:
    mapyou.append(z)
    y=z[0]
    i=0
  else:
    i+=1

y=map2[235][1]

i=0
while i<len(map2):
  z=map2[i]
  if y == z[1]:
    mapsanta.append(z)
    y=z[0]
    i=0
  else:
    i+=1
j=0
while j<len(mapyou):
  if mapyou[j][1]==cross:
    print(j)
    break
  else:
    j+=1
j=0
while j<len(mapsanta):
  if mapsanta[j][1]==cross:
    print(j)
    break
  else:
    j+=1