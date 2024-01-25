import numpy as np
import matplotlib.pyplot as plt


k1=0.05
k2=0.05
a=[]
b=[]
c=[]
a.append(1)
b.append(0.5)
c.append(0)
N=100.0
t=(N-0.0)/(500.0)
# print(t)


time=[0.0]
i=0.0
legend=False
while i <= N:
    tmp_a=a[-1]
    tmp_b=b[-1]
    tmp_c=c[-1]
    tmp_t=time[-1]
    
    a.append(tmp_a+(k2*tmp_c- k1*tmp_a*tmp_b)*t)
    b.append(tmp_b+(k2*tmp_c- k1*tmp_a*tmp_b)*t)
    c.append(tmp_c+(2*k1*tmp_a*tmp_b- 2*k2*tmp_c)*t)
    time.append(tmp_t+t)
    i+=t
    plt.plot(time, a, 'b', label='A')
    plt.plot(time, b, 'r', label='B')
    plt.plot(time, c, 'g', label='C')
    plt.xlim([0,100])
    if legend==False:
        legend=True
        plt.legend()
    # Pause briefly to show the updated plot
    plt.pause(0.01)

plt.show()
















