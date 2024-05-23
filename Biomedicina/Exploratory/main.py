import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 48]

# Create a bar chart
fig, ax = plt.subplots()

# Customize the bar color
bar_color = 'skyblue'

# Create bars
bars = ax.bar(categories, values, color=bar_color)

# Customize the background color
background_color = 'white'
fig.patch.set_facecolor(background_color)

# Remove grid
ax.grid(False)

# Add labels
ax.set_xlabel('Categories', fontsize=12)
ax.set_ylabel('Values', fontsize=12)
ax.set_title('Simple Bar Chart', fontsize=14)

# Customize the axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('grey')
ax.spines['bottom'].set_color('grey')

# Customize the ticks
ax.tick_params(axis='x', colors='grey')
ax.tick_params(axis='y', colors='grey')

# Show the plot
plt.show()
