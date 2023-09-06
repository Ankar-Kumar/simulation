import numpy as np
import pygame
pygame.init()
pygame.display.set_caption('chemical reactors  ')
screen_size = (650, 650)
screen = pygame.display.set_mode(screen_size)





k1=0.008
k2=0.002
a=[]
b=[]
c=[]
a.append(100)
b.append(50)
c.append(0)
t=0.1
N=50
time=[0.0]
for i in range(N):
    tmp_a=a[-1]
    tmp_b=b[-1]
    tmp_c=c[-1]
    tmp_t=time[-1]
    a.append(tmp_a+(k2*tmp_c- k1*tmp_a*tmp_b)*t)
    b.append(tmp_b+(k2*tmp_c- k1*tmp_a*tmp_b)*t)
    c.append(tmp_c+(2*k1*tmp_a*tmp_b- 2*k2*tmp_c)*t)
    time.append(tmp_t+t)
    # print(tmp_t,"   ",tmp_a,"  ",tmp_b,"   ",tmp_c)
for i in range(N+1):
        # print('%.2f' %t[i], '\t%.2f' %a[i], '\t%.2f' %b[i], '\t%.2f' %c[i])
        print(round(time[i], 2), '\t', round(a[i], 2), '\t', round(b[i], 2), '\t', round(c[i], 2))