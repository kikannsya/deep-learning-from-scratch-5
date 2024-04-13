import numpy as np

N = 3 # サンプルサイズ

xs = []

for n in range(N):
    x = np.random.rand()
    xs.append(x)

x_mean = np.mean(xs)
print(x_mean)