import matplotlib.pyplot as plt 



x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y,
    color='green',          # Line color
    linestyle="--",          # Solid line style
    linewidth=2,            # Line width
    marker='s',             # Square markers
    markerfacecolor='orange', # Marker fill color
    markersize=8            # Marker size
)



# Add titles and labels
plt.title("Styled Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

# Customize grid and add legend
plt.grid(True, linestyle='--', linewidth=0.5) # Dashed grid lines
plt.legend(["Sample Data"], loc="upper left")

plt.show()