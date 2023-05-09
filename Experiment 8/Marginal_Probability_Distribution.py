import numpy as np
import matplotlib.pyplot as plt

# Define the joint probability distribution
P_XY = np.array([[0.1, 0.2], [0.3, 0.4]])

# Compute the marginal probability distributions P(X) and P(Y)
P_X = np.sum(P_XY, axis=1)
P_Y = np.sum(P_XY, axis=0)

# Visualize the marginal probability distributions
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

axs[0].bar(range(P_X.shape[0]), P_X)
axs[0].set_xlabel('X')
axs[0].set_ylabel('Probability')
axs[0].set_xticks([0, 1])
axs[0].set_title('Marginal Probability Distribution of X')

axs[1].bar(range(P_Y.shape[0]), P_Y)
axs[1].set_xlabel('Y')
axs[1].set_ylabel('Probability')
axs[1].set_xticks([0, 1])
axs[1].set_title('Marginal Probability Distribution of Y')

plt.show()
