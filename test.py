from graph import Graph
from random_solver import RandomSolver
from deterministic_solver import DetermininsticSolver
import sys

def compute_accurace(a,b):
	# print(a)
	# print(b)
	v = 0
	s = 0
	for i in range(0,len(a)):
		if(a[i] > 0):
			v = v + 1
			s = s + abs(b[i]-a[i])/a[i]
			#print(i,a[i],b[i],s,v)
	return (1-s/v)*100


g = Graph()
g.read_from_mat(sys.argv[1])

ds = DetermininsticSolver(g)
ds.solve()

print("n = " + str(g.vertices))
print("for deterministic")
print("time = "+ str(ds.time))
print("-------------")

rs = RandomSolver(g,0.1)

for eps in [0.1,0.05,0.001]:
	rs.change_eps(eps)
	rs.solve()
	a = compute_accurace(ds.solution, rs.solution)
	print("for eps = "+ str(eps))
	print("time = "+str(rs.time))
	print("accuracy = "+ str(a))
	print("-------------")