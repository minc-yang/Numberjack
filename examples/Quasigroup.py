from Numberjack import *

def QG(t,a,b,x): 
    if   t == 3 : return (x[x[a,b],x[b,a]] == a)
    elif t == 4 : return (x[x[b,a],x[a,b]] == a)
    elif t == 5 : return (x[x[x[b,a],b],b] == a)
    elif t == 6 : return (x[x[a,b],b] == x[a,x[a,b]])
    elif t == 7 : return (x[x[b,a],b] == x[a,x[b,a]])

def model_quasigroup(T,N):
    matrix = Matrix(N,N,N)
    model = Model(
        [AllDiff(row) for row in matrix.row], # latin square (rows)
        [AllDiff(col) for col in matrix.col], # latin square (columns)
        
        [matrix[a,a] == a for a in range(N)], # idempotency
        [QG(T,a,b,matrix) for a in range(N) for b in range(N)]
    )
    return (matrix,model)

def solve_quasigroup(param):
    (matrix,model) = model_quasigroup(param['T'], param['N'])
    solver = model.load(param['solver'])
    if solver.solve():
        print matrix.solution()
    else:
        print 'no such quasigroup'
    print 'Nodes:', solver.getNodes(), ' Time:', solver.getTime()

solve_quasigroup(input({'solver':'Mistral', 'N':8, 'T':3}))
