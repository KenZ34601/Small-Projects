import numpy as np
from payoff_solver import findstrategy
import gambit
import sys

orig_stdout = sys.stdout

# record results in txt file
f = open('PayoffMatrix_result.txt', 'w')
sys.stdout = f

#1(a)
# parameters for generating payoff matrices
#range of values in the payoff matrix                                                                                           
# -1000 <= a_ij <= 1000 
low = -1000
high = 1000
step = 1
m = 1
for iteration in range(100):
    print('Iteration', m)
    print('generating payoff matrix...')
# generate a random matrix with 
# m is 1 to 100
    rows  = np.random.choice([x+1 for x in range(10)])
# n is 1 to 100
    cols = np.random.choice([x+1 for x in range(10)])
#construct payoff matrix G
    G = np.random.choice([x for x in range(low,high,step)],rows*cols)
    G.resize(rows,cols)
    print(G)

#solve the payoff matrix using gambit

    G_array = G.astype(gambit.Rational)
    G_gambit = gambit.Game.from_arrays(G_array, -G_array)

    solver = gambit.nash.ExternalEnumMixedSolver()
    pq = solver.solve(G_gambit)
    p_gambit = np.array(pq[0][G_gambit.players[0]])
    q_gambit = np.array(pq[0][G_gambit.players[1]])
    v_gambit = pq[0].payoff(G_gambit.players[0])
#solve the payoff matrix using my code
    p, q, v = findstrategy(G)
    print('QZ code result: ')
    print(p)
    print(q)
    print(v)
    print('Gambit result: ')
    print(p_gambit)
    print(q_gambit)
    print(v_gambit)
    print('Does it match the Gambit results')
    print(np.max(p-p_gambit) < 1e-4 and np.max(q-q_gambit) < 1e-4 and v-v_gambit < 1e-4) 

    m+=1


#1(b)
g1 =  np.array([[1,2,3,4,5], [3,4,5,6,7]])
print(g1)
p1,q1,v1 = findstrategy(g1)
print('Play I strategy is', p1)
print('Play II strategy is', q1)
print('Value of the Game is', v1)
g2 = np.array([[1,-2,3,-4], [0,1,-2,3], [0,0,1,-2], [0,0,0,1]])
print(g2)
p2,q2,v2 = findstrategy(g2)
print('Play I strategy is', p2)
print('Play II strategy is', q2)
print('Value of the Game is', v2)
g3 = np.array([[1,2,-1], [2,-1,4], [-1,4,-3]])
print(g3)
p3,q3,v3 = findstrategy(g3)
print('Play I strategy is', p3)
print('Play II strategy is', q3)
print('Value of the Game is', v3)

g4 = np.array([[0,2,1], [-2,0,-4], [-1,4,0]])
print(g4)
p4,q4,v4 = findstrategy(g4)
print('Play I strategy is', p4)
print('Play II strategy is', q4)
print('Value of the Game is', v4)

g5 = np.array([[10,0,7,0], [0,6,4,0], [0,0,3,3]])
print(g5)
p5,q5,v5 = findstrategy(g5)
print('Play I strategy is', p5)
print('Play II strategy is', q5)
print('Value of the Game is', v5)

sys.stdout = orig_stdout
f.close()
