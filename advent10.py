def distance(u,v):
  x=abs(u[0]-v[0])
  y=abs(u[1]-v[1])
  return x+y

asteroids=[
'.#..#..#..#...#..#...###....##.#....',
'.#.........#.#....#...........####.#',
'#..##.##.#....#...#.#....#..........',
'......###..#.#...............#.....#',
'......#......#....#..##....##.......',
'....................#..............#',
'..#....##...#.....#..#..........#..#',
'..#.#.....#..#..#..#.#....#.###.##.#',
'.........##.#..#.......#.........#..',
'.##..#..##....#.#...#.#.####.....#..',
'.##....#.#....#.......#......##....#',
'..#...#.#...##......#####..#......#.',
'##..#...#.....#...###..#..........#.',
'......##..#.##..#.....#.......##..#.',
'#..##..#..#.....#.#.####........#.#.',
'#......#..........###...#..#....##..',
'.......#...#....#.##.#..##......#...',
'.............##.......#.#.#..#...##.',
'..#..##...#...............#..#......',
'##....#...#.#....#..#.....##..##....',
'.#...##...........#..#..............',
'.............#....###...#.##....#.#.',
'#..#.#..#...#....#.....#............',
'....#.###....##....##...............',
'....#..........#..#..#.......#.#....',
'#..#....##.....#............#..#....',
'...##.............#...#.....#..###..',
'...#.......#........###.##..#..##.##',
'.#.##.#...##..#.#........#.....#....',
'#......#....#......#....###.#.....#.',
'......#.##......#...#.#.##.##...#...',
'..#...#.#........#....#...........#.',
'......#.##..#..#.....#......##..#...',
'..##.........#......#..##.#.#.......',
'.#....#..#....###..#....##..........',
'..............#....##...#.####...##.']

corsast=[]
for j in range(0,len(asteroids),1):
  xcors = [i for i, x in enumerate(asteroids[j]) if x == '#']
  ycor=j
  for x in xcors:
    corsast.append((x,j))

corsast=[]
for j in range(0,len(asteroids),1):
  xcors = [i for i, x in enumerate(asteroids[j]) if x == '#']
  ycor=j
  for x in xcors:
    corsast.append((x,j))

highestcount=0
print(999999)
size=len(asteroids[0])
for u in corsast:
  ast=u
  count=0
  cors=[]
  for k in range(size):
    for j in range(size):
      cors.append((k,j))
  for k in range(1,2*size):
    circle=[]
    for x in cors:
      if distance(x,ast)==k:
        circle.append(x)
    for y in circle:
      if asteroids[y[1]][y[0]]=='#':
        count+=1
        factor=1
        difx=y[0]-ast[0]
        dify=y[1]-ast[1]
        for s in range(2,size):
          if (difx !=0 or dify !=0) and difx % s==0 and dify % s==0:
            if s>factor:
              factor=s
        difx=difx/factor
        dify=dify/factor
        i=0
        while 0<=y[0]+i*difx<size and 0<=y[1]+i*dify<size:
          point=(y[0]+i*difx,y[1]+i*dify)
          if point in cors:
            cors.remove(point)
          i+=1
  if count>highestcount:
    highestast=ast
    highestcount=count

print(highestast, highestcount)