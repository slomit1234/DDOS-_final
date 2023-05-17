import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data_c = np.loadtxt('pintc.txt.txt', delimiter='\t')
# Extract x and y values for C attack
x_c, y_c = data_c[:, 1], data_c[:, 0]

# Create logarithmic plot for C attack
plt.figure(figsize=(10, 6))
plt.semilogx(x_c, y_c, 'r')
plt.xlabel('RTT (ms)')
plt.ylabel('Number of pings')
plt.title('Ping RTT - C Attack')
plt.grid(True)
plt.savefig('Pings_c.png')
plt.show()