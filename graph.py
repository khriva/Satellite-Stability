import matplotlib.pyplot as plt
a = [9,(4.35**2),(5.4**2),(6.2**2),(6.9**2),(7.4**2),(7.8**2)]
n = [1,2,3,4,5,6,7]
plt.grid(True)
plt.scatter(n,a)
plt.plot(n,a)
plt.show()
n_0=2.29
Lambda = 0.63/1000000
L=87.5/100
k = (a[2] - a[1]) /10000
l = 26/1000
minusik  =((n_0*L)**2)*Lambda/l/k
print(minusik)