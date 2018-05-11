import matplotlib.pyplot as plt
plt.plot([1,2.8,8.6,12.3, 14.7, 18.6,23.4], [1,2,3,4,5,6,7], 'ro')
#plt.axis([0, 20, 0, 20])
plt.xticks([])
plt.yticks([])
plt.xlabel("Key Values")
plt.ylabel("Memory Location")
plt.savefig("key1.png")
