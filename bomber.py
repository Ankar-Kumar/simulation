import numpy as np
import math
import matplotlib.pyplot as plt
data=[]
with open('bomb.txt', 'r') as f:
    lines = []
    for line in f:
        line=line.strip().split()
        tmp=[int(val) for val in line]
        data.append(tmp)
        # print(x,"  ",y)
# print(data)
xb=[x[0] for x in data]
yb=[x[1] for x in data]
# print(xb)
xf=[0]
yf=[50]

vf=20
t=0
i=0
mn=10
mx=100
while True:
    t+=1
    dist = math.sqrt((data[i][0]-xf[-1])**2+(data[i][1]-yf[-1])**2)
    pygame.draw.circle(screen, (50, 50, 250), (bx[-1], by[-1]), 2)
    pygame.draw.circle(screen, (200, 50, 200), (fx[-1], fy[-1]), 2)

    if (dist <= mn):
        flag = True
        print('Bomber caught at step: ' + str(t))
        break
    elif (dist >= mx):
        flag = False
        print('Bomber escaped at step: ' + str(t))
        break
    else:
        cosA, sinA = (data[i][0]-xf[-1])/dist, (data[i][1]-yf[-1])/dist
        xf.append(xf[-1]+vf*cosA)
        yf.append(yf[-1]+vf*sinA)
        x, y = np.random.randint(-500, 500, 2)
        xf.append(x)
        yf.append(y)
        i+=1
plt.scatter(xf,yf)
plt.scatter(xb,yb)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Bomber vs Fighter\nBomber ' + ('caught' if flag == True else 'escaped') + ' at step: ' + str(t)) 
plt.legend(['Fighter', 'Bomber'])
plt.show()