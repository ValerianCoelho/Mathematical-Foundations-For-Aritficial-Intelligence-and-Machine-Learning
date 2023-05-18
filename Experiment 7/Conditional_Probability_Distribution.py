import matplotlib.pyplot as plt

# Conditional probabilities
rain_prob = 0.3
umbrella_given_rain_prob = 0.8
umbrella_given_no_rain_prob = 0.2

# Data for the bar chart
x = ['Rain', 'No Rain']
y = [umbrella_given_rain_prob, umbrella_given_no_rain_prob]

# Plotting the bar chart
plt.bar(x, y)
plt.xlabel('Weather')
plt.ylabel('Probability of Using Umbrella')
plt.title('Conditional Probability: Use of Umbrella given Weather')
plt.show()