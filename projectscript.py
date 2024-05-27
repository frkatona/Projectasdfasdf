import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Step 2: Generate noisy Gaussian data
mu, sigma, num_points = 0, 1, 100
x = np.linspace(-3, 3, num_points)
y = (1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2))) + np.random.normal(0, 0.1, num_points)

# Step 3: Define a Gaussian function to fit to the data
def gaussian(x, a, mu, sigma):
    return a * np.exp(-(x - mu)**2 / (2 * sigma**2))

# Step 4: Use curve_fit to fit the Gaussian function to the data
popt, pcov = curve_fit(gaussian, x, y)

# Step 5: Print the fit statistics
print(f"Fit parameters: a={popt[0]}, mu={popt[1]}, sigma={popt[2]}")
print(f"Covariance matrix: {pcov}")

# Step 6: Plot the original data and the fitted Gaussian
plt.scatter(x, y, label='Data')
plt.plot(x, gaussian(x, *popt), 'r', label='Fitted Gaussian')
plt.legend()
plt.show()