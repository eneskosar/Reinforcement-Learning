
from scipy.optimize import linprog

mu = 0.1
obj = [0, (mu-1), 0, mu]

equalities_left = [
    [0.2,0.7,-0.95,-0.5],
    [1,1,1,1]
]

equalities_right = [
    0,
    1
]

bnd = [ (0, 1),  # Bounds of x1
        (0, 1),
        (0, 1),
        (0, 1),
       ]

opt = linprog(c=obj,
              A_eq=equalities_left, b_eq=equalities_right,
              bounds=bnd, method="revised simplex")

print(opt)

print(0.57575*(mu-1))