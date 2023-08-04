import matplotlib.pyplot as plt

# initializing the data
x = [10, 20, 30, 40,50,60,70,80,90,100,110,120]
y = [0, 25, 35, 100,23,56,78,12,1,59,76,45]

# plotting the data
plt.plot(x, y)

# Adding title to the plot
plt.title("Linear graph", fontsize=25, color="purple")

# Adding label on the x-axis
plt.xlabel('X-Axis',fontsize=13, color="black")

# Adding label on the y-axis
plt.ylabel('Y-Axis', fontsize=13, color="black")


# setting the labels of x-axis
plt.xticks(x, labels=["1", "2", "3", "4","5","6","7","8","9","10","11","12"])

# Setting the limit of y-axis
plt.ylim(0, 100)

# Adding legends
plt.legend(["my_first_graph"])

plt.show()
