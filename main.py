import numpy as np
from matplotlib import pyplot as plt

def tanh(x):
  return (((np.exp(x))-(np.exp(-1*x)))/((np.exp(x))+(np.exp(-1*x))))

def sech(x):
  return (2/((np.exp(x))+(np.exp(-1*x))))

def tanh_deriv(x):
  return (sech(x)*sech(x))

def forward(x,w1,w2,predict=False):
  a1=np.matmul(x,w1)
  z1=tanh(a1)
#   print(z1," - z1 ",x," - x")
  bias=np.ones((len(z1),1))
  z1=np.concatenate((bias,z1),axis=1)
#   print(z1,"=z1")
  a2=np.matmul(z1,w2)
  z2=tanh(a2)
  if predict:
    return z2
  return a1,z1,a2,z2

#bp
def backprop(a2,z0,z1,z2,y):
  delta2=z2-y
  Delta2=np.matmul(z1.T,delta2)
#   print(w2," = w2")
  delta1=(delta2.dot(w2[1:,:].T))*tanh_deriv(a1)
  Delta1=np.matmul(z0.T,delta1)
  return delta2,Delta1,Delta2

# x=np.array([[1,1,0],
#             [1,0,1],
#             [1,0,0],
#             [1,1,1]])

x=np.array([[1,-1,-1],[1,-1,0],[1,-1,1],[1,0,-1],[1,0,0],[1,0,1],[1,1,-1],[1,1,0],[1,1,1]])

y=np.array([[-1],[1],[0],[1],[0],[-1],[0],[-1],[1]])

w1=np.random.randn(3,5)
w2=np.random.randn(6,1)

lr=0.7

costs=[]

epochs=1

m=len(x)

for i in range(epochs):
#   print(x,w1,w2," bruh")
  a1,z1,a2,z2=forward(x,w1,w2)

  delta,Delta1,Delta2 =backprop(a2,x,z1,z2,y)
  w1 -=lr*(1/m)*Delta1
  w2 -=lr*(1/m)*Delta2


  c=np.mean(np.abs(delta))
  costs.append(c)
  if i % 1000 == 0:
    print(f"Iteration:{i}.Error:{c}")
    # print(y," y")

print("Training complete")

z3=forward(x,w1,w2,True)
print("Percentages:")
print(z3," = z3")
print("Predictions:")
print(np.round(z3+1))

plt.plot(costs)
plt.show()
