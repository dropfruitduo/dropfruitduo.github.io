lister=[3,225,1,225,6,6,1100,1,238,225,104,0,1101,90,60,224,1001,224,-150,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1,57,83,224,1001,224,-99,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1102,92,88,225,101,41,187,224,1001,224,-82,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,7,20,225,1101,82,64,225,1002,183,42,224,101,-1554,224,224,4,224,102,8,223,223,1001,224,1,224,1,224,223,223,1102,70,30,224,101,-2100,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,2,87,214,224,1001,224,-2460,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,102,36,180,224,1001,224,-1368,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1102,50,38,225,1102,37,14,225,1101,41,20,225,1001,217,7,224,101,-25,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,7,30,225,1102,18,16,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,359,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,108,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1008,677,677,224,1002,223,2,223,1005,224,449,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,464,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,479,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,509,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,1008,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,599,1001,223,1,223,108,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]


def check_mode(item):
  modes=[0,0]
  if len(item)>2:
    modes[1]=int(item[-3])
    if len(item)>3:
      modes[0]=int(item[-4])
  return modes

def run_instruct(i,z,liste):
  code=liste[i]
  code=str(code)
  modes = check_mode(code)
  item=int(code[-1])
  if item == 1:
    pos3=liste[i+3]
    if modes[1]==1:
      pos1=i+1
    else:
      pos1=liste[i+1]
    if modes[0]==1:
      pos2=i+2
    else:
      pos2=liste[i+2]
    y=liste[pos1]+liste[pos2]
    liste[pos3]=y

    return i+4,z
  if item==2:
    pos3=liste[i+3]
    if modes[1]==1:
      pos1=i+1
    else:
      pos1=liste[i+1]
    if modes[0]==1:
      pos2=i+2
    else:
      pos2=liste[i+2]

    y=liste[pos1]*liste[pos2]
    liste[pos3]=y
    return i+4,z
  if item==3:
    pos=liste[i+1]
    liste[pos]=z
    return i+2,z
  if item==4:
    if modes[1]==1:
      z=liste[i+1]
    else:
      pos=liste[i+1]
      z=liste[pos]
    return i+2,z
  if item==5:
    if modes[1]==1:
      pos1=i+1
    else:
      pos1=liste[i+1]
    if modes[0]==1:
      pos2=i+2
    else:
      pos2=liste[i+2]
    if liste[pos1]!=0:
      return liste[pos2],z
    else:
      return i+3,z

  if item==6:
    if modes[1]==1:
      pos1=i+1
    else:
      pos1=liste[i+1]
    if modes[0]==1:
      pos2=i+2
    else:
      pos2=liste[i+2]
    if liste[pos1]==0:
      return liste[pos2],z
    else:
      return i+3,z
  if item==7:
    pos3=liste[i+3]
    if modes[1]==0:
      pos1=liste[i+1]
    else:
      pos1=i+1
    if modes[0]==0:
      pos2=liste[i+2]
    else:
      pos2=i+2
    if liste[pos1]<liste[pos2]:
      liste[pos3]=1
    else:
      liste[pos3]=0
    return i+4,z
  if item==8:
    pos3=liste[i+3]
    if modes[1]==0:
      pos1=liste[i+1]
    else:
      pos1=i+1
    if modes[0]==0:
      pos2=liste[i+2]
    else:
      pos2=i+2
    if liste[pos1]==liste[pos2]:
      liste[pos3]=1
    else:
      liste[pos3]=0  
    return i+4,z

def intcomputer(inp, instructions):
  place=0
  z=inp
  while place < len(instructions):
    if str(instructions[place])[-1]=='9':
      break
    place,z = run_instruct(place,z, instructions)
  return z


print(intcomputer(5, lister))