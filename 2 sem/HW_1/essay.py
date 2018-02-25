import matplotlib.pyplot as plt
import seaborn
import numpy as np


def f(x):
    return x*np.exp(x) + np.sin(np.exp(x))

a,b = -5,0
plt.figure(figsize=(10,6))
plt.plot(np.linspace(a,b), f(np.linspace(a,b)))
plt.title("f", fontsize=18)
