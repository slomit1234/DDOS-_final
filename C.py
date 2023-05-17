import matplotlib.pyplot as plt
import numpy as np

# Read data from the file
data_c = np.loadtxt('syns_results_c.txt', delimiter='\t')

# Extract x and y values for C attack
x_c, y_c = data_c[:, 1], data_c[:, 0]

# Create logarithmic plot for C attack
plt.figure(figsize=(10, 6))
plt.semilogy(x_c, y_c, 'r')
plt.xlabel('Time needed to send a packet (seconds)')
plt.ylabel('Number of packets sent')
plt.title('Packet Sending Time - C Attack')
plt.grid(True)
plt.savefig('Syn_pkts_c.png')
plt.show()