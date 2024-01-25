import numpy as np

from collections import defaultdict 

file_path = "cpm.txt"
 
predecessor ={defaultdict(list)}
succesor =defaultdict(list) 
index = []
MX = 1005
arr = np.zeros((MX, 2), dtype=int)  # arr[mx][2] initialize all with 0
cost = np.zeros((MX, 5), dtype=int)

## taking input and store the values into array

i=1
for lines in open(file_path):
     words = lines.rstrip('\n').split(',')
    #  print(words)
     idx= int(words[0]) ## when we declare an extra index value then needed 
     arr[i][1] = words[1] # activity name
     
     cost[i][0] = int(words[2])

     tmp_word= words[3]
     index.append(idx)   

     if(len(tmp_word)!=0):
        predecessors = tmp_word.split(';')  # how you take input 
      #   print(i,predecessors)
        for item in predecessors:
            item = int(item)
            # print(i,item)
            # print (str(idx) + " predecessor: " + str(item))
            predecessor[idx].append(item)  # for forword pass needed
            succesor[item].append(idx)  # for backward pass needed
     i=i+1
## end of taking input

### check the value of graph if needed 
# for idx in index:
#    print(idx,'>')
#    for val in succesor[idx]:
#        print(val,end='   ')
#    #  print (idx, predecessor[idx])
     



maxEF = 0

for idx in index:
    if (len(predecessor[idx]) == 0):
        cost[idx][1]=0
        cost[idx][2]=cost[idx][0]  ## earliest finish a duration time store krbo
    else :
        maxTime = 0
        for item in predecessor[idx]:# sob gula activity max EF time check korbo            
                maxTime = max(maxTime,cost[item][2])
        cost[idx][1]=maxTime
        cost[idx][2]=maxTime+cost[idx][0]

     
    maxEF = max(maxEF, cost[idx][2]) # finish line e gia abar MAX EF time check kore store korbo



length = len(index)
for i in range(length):
    print(i)
    idx = index[length-i-1]
    if (len(succesor[idx]) == 0):  ## when there is no successor 
        cost[idx][4]=maxEF   ## latest finish a max value store krbo
        cost[idx][3]=maxEF-cost[idx][0]
    else :
        minTime = 99999
        for item in succesor[idx]:           
                minTime =min( minTime, cost[item][3])
        cost[idx][4]=minTime
        cost[idx][3]=minTime-cost[idx][0]   
      

result = []
print()
print("check the value of cost array")
for i in index:
     print()
    
     # earliest_start -> earliest_finish -> latest_start -> latest_finish
     for j in range(1,5):
      print(cost[i][j],end='   ')
     if cost[i][1] == cost[i][3] and cost[i][2] == cost[i][4]:
        # result.append(arr[i][1]) # when we have not extra column for activity name
         result.append(i)    ## when index and activity order are same

print()
print()

print("critical path ")
for i in range(len(result)-1):    
    print(result[i] , " -> ", end="")

print(result[len(result)-1])


