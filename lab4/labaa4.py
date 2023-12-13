from scipy.optimize import linprog
#1
obj = [-180, -200]


lhs_ineq = [[ 5,  4],
            [10,  20]]

rhs_ineq = [[80,
           200]]
bnd = [(0, float("inf")),  # Bounds of x
        (0, float("inf"))]  # Bounds of y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq
              , bounds=bnd,
              method="revised simplex")

print(opt)
#https://realpython.com/linear-programming-python/
#2
from scipy.optimize import linprog

obj2 = [1, 1, 1, 1, 1, 1, 1]

lhs_ineq2 = [[-1, 0, -1, -1, 0, 0, 0],
            [0, -1, -1, 0, 0, 0, -1],
            [-1, 0, 0, 0, -1, -1, 0],
            [0, -1, 0, 0, -1, 0, -1]]

rhs_ineq2 = [-1,
            -1,
            -1,
            -1]

bnd2 = [(0, 1),
       (0, 1),
       (0, 1),
       (0, 1),
       (0, 1),
       (0, 1),
       (0, 1)]

opt2 = linprog(c=obj2, A_ub=lhs_ineq2, b_ub=rhs_ineq2, bounds=bnd2, method="revised simplex")
x1,x2,x3,x4,x5,x6,x7=opt2.x
print(opt2)