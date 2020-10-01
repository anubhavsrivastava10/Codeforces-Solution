import itertools
g = [[[] for _ in range(5)] for _ in range(5)]
for i in range(5):
	gi = [int(gij) for gij in input().split(" ")]
	for j in range(5):
		gij = gi[j]
		g[i][j] = gij
p = itertools.permutations([1,2,3,4,5])
ans = -1
for x in p:
	pi = list(x)
	pi = [pi-1 for pi in pi]
	tmp = 0
	tmp += g[pi[0]][pi[1]]
	tmp += g[pi[1]][pi[0]]
 
	tmp += g[pi[1]][pi[2]]
	tmp += g[pi[2]][pi[1]]
	
	tmp += g[pi[2]][pi[3]]
	tmp += g[pi[3]][pi[2]]
	
	tmp += g[pi[2]][pi[3]]
	tmp += g[pi[3]][pi[2]]
 
	tmp += g[pi[3]][pi[4]]
	tmp += g[pi[4]][pi[3]]	
 
	tmp += g[pi[3]][pi[4]]
	tmp += g[pi[4]][pi[3]]
	if tmp > ans:
		ans = tmp
 
print(ans)