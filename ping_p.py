import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data_py = np.loadtxt('new_pings_results_p.txt', delimiter='\t')

# Extract x and y values for Python attack
x_py, y_py = data_py[:, 1], data_py[:, 0]

# Create logarithmic plot for Python attack
plt.figure(figsize=(10, 6))
plt.semilogx(x_py, y_py, 'b')
plt.xlabel('RTT (ms)')
plt.ylabel('Number of pings')
plt.title('Ping RTT - Python Attack')
plt.grid(True)
plt.savefig('Pings_p.png')
plt.show()