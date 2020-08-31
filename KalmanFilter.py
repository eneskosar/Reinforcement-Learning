import numpy as np

# x(t+1) = Ax(t) + w(t)
# y(t) = Cx(t)+v(t)

m = [[0,0,0]]
y = []
x = []
w = []
v = []

xasd1, xasd2, xasd3= np.random.multivariate_normal([0,0,0], [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]] ).T

wasd1, wasd2, wasd3= np.random.multivariate_normal([0,0,0], [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]] ).T

A = [[[0.5, 1, 0],
     [0, 0.5, 1],
     [0, 0, 0.5]]]

C = [1, 0, 0]

sigma = [[[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]]]

V = 1
W = [[[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]]

x.append([xasd1, xasd2, xasd3])
w.append([wasd1, wasd2, wasd3])
v.append(np.random.normal(0, 1))
cx0 = np.matmul(np.array(C),  np.array(x[0]))
y.append(cx0 + v[0])


def update_mt(t):
    a = np.array(C).dot(np.array(sigma[t-1])).dot(np.array(C).transpose())
    inversePart = 1/(np.array(C).dot(np.array(sigma[t-1])).dot(np.array(C).transpose()) + V)
    lastPart = np.array(y[t-1] - np.array(C).dot(np.array(m[t-1]).transpose()))

    mt_plus1 = np.array(A).dot(np.array(m[t-1]).transpose()) + np.array(A).dot(np.array(sigma[t-1])).dot(np.array(C).transpose())*(inversePart)*(lastPart)
    m.append(mt_plus1.tolist())


    firstPart = np.array(A).dot(np.array(sigma[t-1])).dot(np.array(A).transpose())
    secondPart= np.array(A).dot(np.array(sigma[t-1])).dot(np.array(C).transpose())
    thirdPart = 1/(np.array(C).dot(np.array(sigma[t-1])).dot(np.array(C).transpose()) + V)
    fourthPart = np.array(C).dot(np.array(sigma[t-1])).dot(np.array(A).transpose())

    sigma_tplus1 = firstPart + W - thirdPart*thirdPart*fourthPart
    sigma.append(sigma_tplus1)


    x.append((np.array(A).dot(np.array(x[t-1]).transpose()) + w[t-1]).tolist())
    y.append((np.array(C).dot(np.array(x[t-1]).transpose()) + v[t-1]).tolist())
    w.append([wasd1, wasd2, wasd3])
    v.append(np.random.normal(0, 1))

for t in range(10):
    update_mt(t+1)

a = np.array([1,2])
b = np.array([[3,4], [1,2]])
c = a.dot(b)

d = [1,2]
e = [[3,4], [1,2]]
f = np.array(d).dot(np.array(e))

print(m)
print(x)