import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data_py = np.loadtxt('syns_results_p.txt', delimiter='\t')

# Extract x and y values for Python attack
x_py, y_py = data_py[:, 1], data_py[:, 0]



# Create logarithmic plot for Python attack
plt.figure(figsize=(10, 6))
plt.semilogy(x_py, y_py, 'b')
plt.xlabel('Time needed to send a packet (seconds)')
plt.ylabel('Number of packets sent')
plt.title('Packet Sending Time - Python Attack')
plt.grid(True)
plt.savefig('Syn_results_p.png')
plt.show()