g=[]
for x in range(254032,789860,1):
  t=0
  x=str(x)
  for i in range(0,5,1):
    if x[i]<=x[i+1]:
      t+=1
  if t==5:
    g.append(x)



f=[]
for x in g:
  i=0
  x=str(x)
  y=[0,0,0,0,0,0]
  while i<5:
    if x[i]==x[i+1]:
      y[i]=1
      if i<4 and x[i+1]==x[i+2]:
        y[i]=0
        if i<3 and x[i+2]==x[i+3]:
          if i<2 and x[i+3]==x[i+4]:
            if i<1 and x[i+4]==x[i+5]:
              i+=1
            i+=1
          i+=1
        i+=1

    i+=1
  for r in range(0,len(y),1):
    if y[r]==1:
      f.append(x)
      break

print(len(f))