import numpy as np
import matplotlib.pyplot as plt

# Define the joint probability distribution
P_XY = np.array([[0.1, 0.2], [0.3, 0.4]])

# Define the conditional probability distribution P(Y|X=x)
def conditional_prob(P_XY, x):
    P_Y_given_X = P_XY[x, :] / np.sum(P_XY[x, :])
    return P_Y_given_X

# Generate and visualize the conditional probability distribution
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

for x in range(P_XY.shape[0]):
    P_Y_given_X = conditional_prob(P_XY, x)
    axs[0].plot(P_Y_given_X, label=f'P(Y|X={x})')
axs[0].set_xticks([0, 1])
axs[0].set_xlabel('Y')
axs[0].set_ylabel('Probability')
axs[0].legend()

# Generate and visualize the joint probability distribution
X, Y = np.meshgrid(range(P_XY.shape[0]), range(P_XY.shape[1]))
axs[1].pcolormesh(X, Y, P_XY.T, cmap='Blues')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Y')
axs[1].set_xticks([0, 1])
axs[1].set_yticks([0, 1])
axs[1].set_title('Joint Probability Distribution')

plt.show()
