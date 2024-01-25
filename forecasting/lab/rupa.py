import numpy as np
from collections import defaultdict

f_path = "rupa.txt"
act_f = defaultdict(list)
act_b = defaultdict(list)

index = []

mx =1005

act = np.zeros((mx,2),dtype=int)
dur = np.zeros((mx,5), dtype=int)

i=1

for line in open(f_path):
        word = line.rstrip('\n').split(',')
        ind = int(word[0])
        act[i][1] = ord(word[0]) - ord('A') + 1 ## changes this line as a A replace to 1
        dur[i][0] = int(word[2])

        tmp = word[3]
        index.append(ind)

        if(len(tmp)!=0):
            predes = tmp.split(';')

            for item in predes:
                item = ord(item)- ord('A') + 1 ## changes this line as a A replace to 1 and so on
                act_f[ind].append(item)
                act_b[item].append(ind)
        i+=1

mxVal = 0
for ind in index:
        if(len(act_f[ind])==0):
            dur[ind][1] = 0
            dur[ind][2] = dur[ind][0]
        else:
            mx_t=0
            for itm in act_f[ind]:
                mx_t = max(mx_t,dur[itm][2])
            dur[ind][1] = mx_t
            dur[ind][2] = mx_t + dur[ind][0]
        mxVal = max(mxVal, dur[ind][2])

    #backward_pass:
for i in range(len(index)):
        ind = index[len(index)-i-1]

        if(len(act_b[ind])==0):
            dur[ind][4] = mxVal
            dur[ind][3] = mxVal-dur[ind][0]
        else:
            mn_t = 9999
            for itm in act_b[ind]:
                mn_t = min(mn_t,dur[itm][3])

            dur[ind][4] = mn_t
            dur[ind][3] = mn_t-dur[ind][0]
   
ans = []
print("ES      EF      LS       LF")
print("------------------------------")
for i in index:
    
    for j in range(1,5):
        print(dur[i][j], end="|        ")
    print()
    if(dur[i][1]==dur[i][3] and dur[i][2]==dur[i][4]):
        ans.append(chr(i + ord('A') - 1)) ## change the values to opossite 
        

print()
for i in range(len(ans)-1):
    print(ans[i],end=" -> ")

print(ans[len(ans)-1])