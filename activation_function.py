import numpy as np
import matplotlib.pyplot as plt

# 定义激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.06):
    return np.maximum(alpha*x, x)

def prelu(x, alpha=0.01):
    return np.maximum(alpha*x, x)

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def swish(x, beta=0.5):
    return x * sigmoid(beta * x)

def mish(x):
    return x * np.tanh(np.log(1 + np.exp(x)))

# 生成输入数据
x = np.linspace(-5, 5, 100)

# 绘制激活函数
plt.figure(figsize=(14, 8))

plt.subplot(2, 4, 1)
plt.plot(x, sigmoid(x))
plt.title('(a) sigmoid')

plt.subplot(2, 4, 2)
plt.plot(x, tanh(x))
plt.title('(b) tanh')

plt.subplot(2, 4, 3)
plt.plot(x, relu(x))
plt.title('(c) ReLU')

plt.subplot(2, 4, 4)
plt.plot(x, leaky_relu(x))
plt.title('(d) Leaky ReLU')

plt.subplot(2, 4, 5)
plt.plot(x, prelu(x))
plt.title('(e) PReLU')

plt.subplot(2, 4, 6)
plt.plot(x, elu(x))
plt.title('(f) ELU')

plt.subplot(2, 4, 7)
plt.plot(x, swish(x))
plt.title('(g) Swish')

plt.subplot(2, 4, 8)
plt.plot(x, mish(x))
plt.title('(h) Mish')

plt.tight_layout()
plt.savefig("activition_functions_gai_2.eps",format="eps")
