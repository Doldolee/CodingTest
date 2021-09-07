###1###
n = int(input())
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ["L","R","U","D"]

x = 1
y = 1

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i] :
      nx=x+dx[i]
      ny=y+dy[i]
      
  if nx<1 or ny <1 or nx > n or ny > n:
    continue
  x,y=nx,ny
print(x, y)
 
###2###
N = int(input())

hour=0
min=0
sec=0
count=0

for h in range(N+1):
  for m in range(60):
    for s in range(60):
      if "3" in str(h) + str(m) + str(s):
        count +=1

print(count)

###3###
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord("a")) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0

for step in steps:
  next_row = row + step[0]
  next_col = column + step[1]
  if next_row <1 or next_row >8 or next_col < 1 or next_col>8:
    continue
  else:
    result +=1
print(result)