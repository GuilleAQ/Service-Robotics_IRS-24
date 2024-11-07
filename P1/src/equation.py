import numpy as np

# Define the pixel coordinates (x, y) and world coordinates (x', y')
pixel_coords = [
    (59, 74),
    (369, 82),
    (421, 627),
    (273, 685),
    (481, 329),
    (955, 318),
    (790, 775),
    (826, 961),
    (188, 863),
    (59, 967)
]

world_coords = [
    (5.07, -3.27),
    (2.06, -3.10),
    (1.49, 2.11),
    (2.94, 2.56),
    (0.93, -0.82),
    (-3.62, -0.84),
    (-2.1, 3.55),
    (-2.44, -5.34),
    (3.84, 4.52),
    (5.07, 5.52)
]

# Create the matrix A and vector B for the least squares solution
A = []
B = []

for (x, y), (x_prime, y_prime) in zip(pixel_coords, world_coords):
    # Each pair of points gives us two equations, so we need to append both
    A.append([x, -y, 1, 0])  # Equation for x'
    A.append([y,  x, 0, 1])  # Equation for y'
    B.append(x_prime)
    B.append(y_prime)

# Convert A and B to numpy arrays
A = np.array(A)
B = np.array(B)

# Solve for the transformation parameters using least squares
params, _, _, _ = np.linalg.lstsq(A, B, rcond=None)

# Extract the parameters from the solution
cos_alpha, sin_alpha, tx, ty = params

# Calculate the rotation angle (alpha) and the scaling factor
alpha = np.arctan2(sin_alpha, cos_alpha)
scale = np.sqrt(cos_alpha**2 + sin_alpha**2)

# Print the transformation parameters
print(f"Rotation angle (α): {alpha} radians")
print(f"Translation (tx, ty): {tx}, {ty}")
print(f"Scale factor: {scale}")
