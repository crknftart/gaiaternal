import matplotlib.pyplot as plt
import numpy as np

# Assuming some core_radius value
core_radius = 1

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Draw the Earth's core
core = plt.Circle((0, 0), core_radius, color='blue', alpha=0.5)
ax.add_artist(core)

# Assuming filtered_x_data and filtered_y_data are defined arrays
# Example data for filtered_x_data and filtered_y_data
filtered_x_data = np.random.rand(100) * 2 - 1
filtered_y_data = np.random.rand(100) * 2 - 1

# Calculate the field strength
field_strength = np.sqrt(filtered_x_data**2 + filtered_y_data**2)

# Plot field lines and highlight breaking areas
for i in range(len(filtered_x_data)):
    x = filtered_x_data[i]
    y = filtered_y_data[i]
    strength = field_strength[i]
    if strength > core_radius:  # Assuming breaking area is where strength exceeds core_radius
        ax.plot([0, x], [0, y], color='red', alpha=0.7)  # Highlight breaking area in red
    else:
        ax.plot([0, x], [0, y], color='green', alpha=0.7)  # Regular field lines in green
 #print values

print(strength)
# Add labels and title

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Field Lines Around the Earth\'s Core')

# Show the plot
plt.show()
