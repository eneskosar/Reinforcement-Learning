
import matplotlib.pyplot as plt

mu = 0.95
beta = 0.8

states = ["B", "G"]
actions = [0, 1]

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

PI_S = {
    "G": 0,
    "B": 0
}

policy_history = {
    "G": [0],
    "B": [0]
}


def cost(x,u):
    if int(x == "G") & u == 1:
        return mu*u-1
    else:
        return mu*u

StateValues = {s: 0 for s in states}


for i in range(4):
    value_history = {
        "G": [],
        "B": []
    }
    while True:
        oldStateValues = StateValues.copy()
        delta = 0
        for s in states:

            action = PI_S[s]
            probGood = transitionKernel[f"['{s}',{action},'G']"]
            probBad = transitionKernel[f"['{s}',{action},'B']"]

            costt = cost(s, PI_S[s])
            EV = probGood * StateValues["G"] + probBad * StateValues["B"]

            StateValues[s] = costt + beta * EV
            #print("***********")
            #print(StateValues)
            # calculate maximum difference in value
            delta = max(delta, abs(StateValues[s] - oldStateValues[s]))

            value_history[s].append(StateValues[s])
        # check for convergence, if values converged then return V
        if delta < 0.00001:
            break
    print(value_history["G"])
    print(value_history["B"])
    plt.plot(value_history["G"],  label="Value of state Good")
    plt.ylabel('State value')
    plt.xlabel('Number of iterations')
    plt.plot(value_history["B"], label="Value of state Bad")
    plt.legend(loc="center")
    plt.show()

    for s in states:
        cost0 = cost(s, 0)
        probGood0 = transitionKernel[f"['{s}',0,'G']"]
        probBad0 = transitionKernel[f"['{s}',0,'B']"]
        EV0 = probGood0 * StateValues["G"] + probBad0 * StateValues["B"]

        cost1 = cost(s, 1)
        probGood1 = transitionKernel[f"['{s}',1,'G']"]
        probBad1 = transitionKernel[f"['{s}',1,'B']"]
        EV1 = probGood1 * StateValues["G"] + probBad1 * StateValues["B"]

        a0reward = cost0 + beta * EV0
        a1reward = cost1 + beta * EV1
        if a0reward < a1reward:
            PI_S[s] = 0
        else:
            PI_S[s] = 1

        policy_history[s].append(PI_S[s])


print(PI_S)
print(policy_history["G"])
print(policy_history["B"])



plt.plot(policy_history["G"] , 's', label = "Policy in state Good")
plt.ylabel('Action value')
plt.xlabel('Number of iterations')
plt.plot(policy_history["B"], '^', label = "Policy in state Bad")
plt.legend(loc="center")
plt.show()
















