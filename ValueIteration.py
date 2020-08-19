


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

mu = 0.95
beta = 0.5

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
        for a in actions:
            probGood = transitionKernel[f"['{s}',{a},'G']"]
            probBad = transitionKernel[f"['{s}',{a},'B']"]
            EV = probGood*StateValues["G"] + probBad*StateValues["B"]

            best_EV = min(best_EV, EV)
        StateValues[s] = cost(s,a) + beta*best_EV
        print("***********")
        print(StateValues)
        # calculate maximum difference in value
        delta = max(delta, abs(StateValues[s] - oldStateValues[s]))

    # check for convergence, if values converged then return V
    if delta < 0.001:
        break
print("**************************")
print(StateValues)