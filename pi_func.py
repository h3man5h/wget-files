import math
import random

shots = 10000
value = 20
output=[]

for i in range(0, value):
    incircle = 0
    for i in range(0, shots):
        random1 = random.uniform(-1.0, 1.0)
        random2 = random.uniform(-1.0, 1.0)
        if( ( random1*random1 + random2*random2 ) < 1 ):
          incircle += 1

    y=(4.0 * incircle/shots)
    output.append((incircle,shots,y))
print(output)
