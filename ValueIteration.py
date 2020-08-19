


transitionKernel = {
## current state, action , next state, probability
    "['G',1,'G']": 0.3,
    "['G',1,'B']": 0.7,

    "['G',0,'G']": 0.8,
    "['G',0,'B']": 0.2,

    "['B',1,'G']": 0.5,
    "['B',1,'B']": 0.5,

    "['B',0,'G']": 0.95,
    "['B',0,'B']": 0.05
}

mu = 0.5
beta = 0.8

def cost(x,u):
    if int(x == "G") & u == 1:
        return mu*u-1
    else:
        return mu*u


states = ["B", "G"]
actions = [0, 1]

StateValues = {s: 0 for s in states}

while True:
    oldStateValues = StateValues.copy()
    delta = 0
    for s in states:
        best_EV = 999
        best_cost = 999
        best_total_Cost=999
        for a in actions:
            probGood = transitionKernel[f"['{s}',{a},'G']"]
            probBad = transitionKernel[f"['{s}',{a},'B']"]

            if (a == 0):
                EV0 = probGood * StateValues["G"] + probBad * StateValues["B"]
                cost0 = cost(s, a)
                total_cost0 = EV0 + cost0
            if (a == 1):
                EV1 = probGood * StateValues["G"] + probBad * StateValues["B"]
                cost1 = cost(s, a)
                total_cost1 = EV1 + cost1

        if (total_cost1 > total_cost0):
            best_EV = EV0
            best_cost = cost0
        elif (total_cost0 >= total_cost1):
            best_EV = EV1
            best_cost = cost1

        StateValues[s] = best_cost + beta*best_EV
        print("***********")
        print(StateValues)
        # calculate maximum difference in value
        delta = max(delta, abs(StateValues[s] - oldStateValues[s]))

    # check for convergence, if values converged then return V
    if delta < 0.0001:
        break
print("**************************")
print(StateValues)