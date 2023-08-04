import matplotlib.pyplot as plt

# Sample data
data = [1, 1, 2, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 8, 9]

# Create the histogram
plt.hist(data, bins=20)

# Set labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of Data")

# Display the histogram
plt.show()
