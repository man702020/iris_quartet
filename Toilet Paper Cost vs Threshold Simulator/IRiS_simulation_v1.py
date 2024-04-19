import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000  # Number of people in the population
mean_threshold = 50
r = 2  # Scaling factor
b = 10  # Benefit of replacing the toilet paper roll
std_values = [5, 10, 20]  # Different values of standard deviation
cost = 25  # Cost of replacing the toilet paper roll; change values as fits
initial_happiness = 100
num_simulations = 100000

# Function to calculate thresholds for replacing toilet paper rolls
def calculate_thresholds(mean, std, r, cost, N):
    return np.random.normal(mean, std, N)*cost

# Function to simulate the process and calculate happiness
def simulate_process(thresholds, std):
    happiness_over_time = []
    current_happiness = initial_happiness
    for _ in range(num_simulations):
        random_number = np.random.uniform(0, max(thresholds))
        random_person_index = np.random.randint(0, N)
        # Check if the threshold of the selected person is smaller than the random number
        if thresholds[random_person_index] < random_number:
            current_happiness +=b # Increase happiness by b
        else:
            # With a probability equal to e^-(change in happiness if the toilet paper is not replaced)
            if np.random.random() < np.exp(-(current_happiness*(b/100))):
                current_happiness +=b# Increase happiness by b
            else:
                current_happiness *= (1-b/100)  # Decrease happiness geometrically by b
        happiness_over_time.append(current_happiness)
    return happiness_over_time

# Plot happiness over time for each condition
plt.figure(figsize=(10, 5))
for std in std_values:
    thresholds = calculate_thresholds(mean_threshold, std, r, cost, N)
    happiness_over_time = simulate_process(thresholds, std)
    plt.plot(happiness_over_time, label=f"std={std}")
plt.xlabel('Simulation Iteration')
plt.ylabel('Happiness')
plt.title('Happiness Over Time for Different Standard Deviation Values')
plt.legend()
plt.grid(True)
plt.savefig('/Users/abhinavajaganmadabhushi/Library/CloudStorage/OneDrive-UniversityofCincinnati/Documents/IRiS 2023-24/Happiness_over_time_c=25.svg')
plt.show()

# Plot frequency histogram line plot of threshold for all the conditions in the same figure
plt.figure(figsize=(10, 5))
for std in std_values:
    thresholds = calculate_thresholds(mean_threshold, std, r, cost, N)
    plt.hist(thresholds, bins=30, histtype='step', label=f"std={std}")
plt.xlabel('Thresholds')
plt.ylabel('Frequency')
plt.title('Frequency Histogram Line Plot of Thresholds for Different Standard Deviation Values')
plt.legend()
plt.grid(True)
plt.savefig('/Users/abhinavajaganmadabhushi/Library/CloudStorage/OneDrive-UniversityofCincinnati/Documents/IRiS 2023-24/threshold_hist_c=25.svg')
plt.show()

# Box plot of happiness for each condition
plt.figure(figsize=(10, 5))
plt.boxplot([simulate_process(calculate_thresholds(mean_threshold, std, r, cost, N), std) for std in std_values], labels=std_values)
plt.xlabel('Standard Deviation')
plt.ylabel('Happiness')
plt.title('Box Plot of Happiness for Different Standard Deviation Values')
plt.grid(True)
plt.savefig('/Users/abhinavajaganmadabhushi/Library/CloudStorage/OneDrive-UniversityofCincinnati/Documents/IRiS 2023-24/box_plot_happiness_c=25.svg')
plt.show()