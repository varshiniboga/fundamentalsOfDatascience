import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Read the data from the file
data = pd.read_csv('data6-1.csv', header=None, names=['Salary'])

# Calculate the mean salary ( ̃W) and standard deviation
mean_salary = data['Salary'].mean()
std_dev = data['Salary'].std()

# Create a histogram with a probability density function
plt.hist(data['Salary'], density=True, bins=30, alpha=0.7, color='Turquoise', label='Empirical PDF')

# Create a range of values for the x-axis
x = np.linspace(data['Salary'].min(), data['Salary'].max(), 1000)

# Plot the normal distribution PDF
pdf_values = norm.pdf(x, mean_salary, std_dev)
plt.plot(x, pdf_values, color='orange', label='Normal Distribution PDF')

# Calculate the required value X (fraction of population with salaries between  ̃W and 1.25  ̃W)
X = mean_salary * 1.25

# Plot vertical dotted lines for mean and X
plt.axvline(mean_salary, color='red', linestyle='dashed', linewidth=2, label='Mean Salary ( ̃W):26847.65 Euros')
plt.axvline(X, color='green', linestyle='dashed', linewidth=2, label='X=33559.56 Euros')

# Add labels, title, and legend
plt.xlabel('Annual Salary (Euros)')
plt.ylabel('Probability Density')
plt.title('Salary Distribution Analysis')
plt.legend()

# Display the graph
plt.show()

# Print the calculated values
print(f"Mean Salary ( ̃W): {mean_salary:.2f} Euros")
print(f"X: {X:.2f} Euros")
