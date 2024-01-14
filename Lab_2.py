# All imports for task
import numpy as np

# Define constants
N = 50
max_steps = 1000


def generate_vectors(N):
    first_two_coordinates = np.random.exponential(scale=1, size=(N, 2))
    third_coordinate = np.random.normal(size=N)
    vectors = np.column_stack((first_two_coordinates, third_coordinate))

    return vectors


def kozinec_algorithm(vectors, steps):
    center_of_mass = np.mean(vectors, axis=0)  # Find the center of mass of the set of points
    initial_vector = vectors[0]  # Choose an initial vector
    direction = initial_vector - center_of_mass  # Direction of search
    direction /= np.linalg.norm(direction)  # Normalize the direction

    # Search for the separating vector
    for step in range(steps):
        projections = np.dot(vectors, direction)    # Compute projections of vectors onto the direction
        max_index = np.argmax(projections)
        max_projection = projections[max_index]
        extreme_point = vectors[max_index]  # Find a point on the boundary of the convex hull

        # Check if this is a separating vector
        if max_projection > 0:
            return direction

        # Update the direction for the next step
        direction = extreme_point - center_of_mass
        direction /= np.linalg.norm(direction)

    return direction


generated_vectors = generate_vectors(N)
separating_vector = kozinec_algorithm(generated_vectors, max_steps)
print('Generated vectors:')
print(generated_vectors)
print()
print('Separating vector: {}'.format(separating_vector))
