from random import randrange, choice, random

mu = 0.5
beta = 0.8
alfa = 0.1

states = ["B", "G"]
actions = [0, 1]

Q_table ={

    "G0" : 0,
    "G1" : 0,
    "B0" : 0,
    "B1" : 0

}

transitionKernel = {
# current state, action , next state, probability
    "['G',1,'G']": 0.3,
    "['G',1,'B']": 0.7,

    "['G',0,'G']": 0.8,
    "['G',0,'B']": 0.2,

    "['B',1,'G']": 0.5,
    "['B',1,'B']": 0.5,

    "['B',0,'G']": 0.95,
    "['B',0,'B']": 0.05
}

def cost(x,u):
    if int(x == "G") & u == 1:
        return mu*u-1
    else:
        return mu*u


for i in range(2000):
    s = choice(states)
    a = choice(actions)
    r = random()
    print(r)

    if (r < transitionKernel[f"['{s}',{a},'G']"] ):
        s_next = 'G'
    else:
        s_next = 'B'

    q0 = Q_table[f"{s_next}0"]
    q1 = Q_table[f"{s_next}1"]
    opt_a = 0
    if(q0<q1):
        min_Q = q0
        opt_a = 0
    else:
        min_Q = q1
        opt_a = 1

    Q_table[f"{s}{a}"] = Q_table[f"{s}{a}"] + alfa*(cost(s,a) + beta*min_Q - Q_table[f"{s}{a}"] )

    print("**************************")
    print(Q_table)

print("**************************")
print(Q_table)

