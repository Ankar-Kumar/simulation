import sys
import numpy as np
MX = 1005
arr = np.zeros((MX, 4), dtype=int)  # arr[mx][4] initialize all with 0
cost = np.zeros((MX, 5), dtype=int)
node_t = np.zeros((MX, 4), dtype=int)

sys.stdin = open("pert.txt", "r")

n, m = map(int, input().split())
for i in range(1, n + 1): # 1<=n
	arr[i][0], arr[i][1], cost[i][0], arr[i][2] = map(int, input().split())
	

# cost
# 0 
# 1  2
# 3  4
# forward pass calculation

for i in range(1, n + 1):
	cost[i][1] = node_t[arr[i][1]][1]  # est(k) = ent(s(k))
	cost[i][2] = cost[i][1] + cost[i][0]  # eft(k) = est(k) + t(k)
	node_t[arr[i][2]][1] = max(node_t[arr[i][2]][1], cost[i][2])  # ent(n) = max(lft(all activities terminating on node k))

# backward pass calculation
for i in range(1,m + 1): #  1<=m
	node_t[i][2] = 100 # mx value initilize

# node_t[:, 2] = 100

node_t[m][2] = node_t[m][1] # last 1st position value(time) is copied to the 2nd position

for i in range(n, 0, -1):
	cost[i][4] = node_t[arr[i][2]][2]  # lft(k) = lnt(k)
	cost[i][3] = cost[i][4] - cost[i][0]  # lst(k) = lft(k) - t(k)
	node_t[arr[i][1]][2] = min(node_t[arr[i][1]][2], cost[i][3])  # lnt(n) = min(lst(all activities terminating on node k))

for i in range(1, n + 1):
	if cost[i][1] == cost[i][3] and cost[i][2] == cost[i][4]:
		print(i, end=" > ")


