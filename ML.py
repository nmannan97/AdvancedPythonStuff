from sklearn.linear_model import LinearRegression
import random
import numpy as np
import matplotlib.pyplot as plt

valuesY = np.array([])
valuesX = np.array([]) 
for i in range(20):
    valuesX = np.append(valuesX, [i])
    valuesY = np.append(valuesY, [i + random.random()])

print(valuesX)

X = valuesX

reg = LinearRegression().fit(valuesX.reshape(-1,1), valuesY)

print(reg.coef_)
print(reg.intercept_)

linX = []
linY = []
for i in range(20):
    linX.append(i)
    linY.append(reg.coef_[0]*i + reg.intercept_)

plt.plot(linX, linY)
plt.plot(valuesX, valuesY, 'ro')
plt.show()
