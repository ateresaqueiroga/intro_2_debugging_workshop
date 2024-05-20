# main_script_case_4_bug_atq.R
#
# This script demonstrates a bug in an R script designed to create a scatter plot.
# Due to a logical error, the plot does not display correctly.
#
# INPUTS
# ---------
# None (The script generates random data within the script).
#
# OUTPUTS
# ---------
# None
#
# The script performs the following operations:
# 1. Generates random data for two variables.
# 2. Creates a scatter plot of the data.
# 3. Attempts to highlight points above a certain threshold, but fails due to a logical error.
#
# NOTE: This script is designed to illustrate how logical errors can affect data visualization in R.
#
# -----------------------------------------------------------------------------------------
# Ana Teresa Queiroga, 2024
# PhD student @ Department of Clinical Medicine, Center for Music in the Brain
# Aarhus University, Denmark

# Load necessary libraries
library(ggplot2)

# Set seed for reproducibility
set.seed(123)

# Generate random data
data <- data.frame(
  x = rnorm(100),
  y = rnorm(100)
)

# Plot the data
p <- ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Scatter Plot with Highlighted Points",
       x = "X-Axis",
       y = "Y-Axis")

# Add logical error: Attempt to highlight points where x >= 0.5 or y >= 0.5
highlighted_points <- data[data$x >= 0.5 & data$y > 0.5, ] # Logical error: Incorrect logical operator

# Debugging: Print the highlighted points to verify
print(highlighted_points)

# Check if there are any points to highlight
if (nrow(highlighted_points) > 0) {
  # Add highlighted points to the plot
  p <- p + geom_point(data = highlighted_points, aes(x = x, y = y), color = "red", size = 3)
} else {
  message("No points to highlight.")
}

# Display the plot
print(p)
