import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot
def scatter_plot(x, y, title, x_label, y_label):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Bar chart
def bar_chart(x, y, title, x_label, y_label):
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Heatmap
def heat_map(data, title):
    sns.heatmap(data)
    plt.title(title)
    plt.show()

# Example usage
# Assuming we have data for scatter plot, bar chart, and heatmap

# Scatter plot example
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]
scatter_plot(x, y, "Scatter Plot Example", "X-axis", "Y-axis")

# Bar chart example
x = ['A', 'B', 'C', 'D']
y = [20, 15, 10, 8]
bar_chart(x, y, "Bar Chart Example", "Categories", "Values")

# Heatmap example
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
heat_map(data, "Heatmap Example")
