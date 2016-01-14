import random

with open('list.md','r') as source:
  data = [ (random.random(), line) for line in source ]
data.sort()
with open('list_randomized.md','w') as target:
  for _, line in data:
    target.write( line )
