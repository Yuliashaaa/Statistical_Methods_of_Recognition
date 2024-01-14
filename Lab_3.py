# All imports for task
import numpy as np

# Define constants
n = 100
dispersion = 1
a_1, a_2 = 1, 2
p_k_1, p_k_2 = 0.5, 0.5
epsilon = 0.001


def self_training_algorithm(n, dispersion, a_1, a_2, p_k_1, p_k_2, epsilon):
    sequence = []

    # Generate a sequence based on the specified parameters
    for _ in range(n):
        if np.random.rand() < 1 / 3:
            sequence.append(np.random.normal(0, np.sqrt(dispersion)))   # State k = 1
        else:
            sequence.append(np.random.normal(3, np.sqrt(dispersion)))   # State k = 2

    # Self-training loop
    while True:
        # Estimate probabilities and means
        p_k_1_estimated = np.sum([1 for x_i in sequence if x_i < 1.5]) / n
        p_k_2_estimated = 1 - p_k_1_estimated

        a_1_estimated = np.sum([x_i for x_i in sequence if x_i < 1.5]) / np.sum([1 for x_i in sequence if x_i < 1.5])
        a_2_estimated = np.sum([x_i for x_i in sequence if x_i >= 1.5]) / np.sum([1 for x_i in sequence if x_i >= 1.5])

        # Check for convergence
        if (
                abs(a_1 - a_1_estimated) < epsilon and
                abs(a_2 - a_2_estimated) < epsilon and
                abs(p_k_1 - p_k_1_estimated) < epsilon and
                abs(p_k_2 - p_k_2_estimated) < epsilon
        ):
            break

        # Update parameters
        a_1, a_2 = a_1_estimated, a_2_estimated
        p_k_1, p_k_2 = p_k_1_estimated, p_k_2_estimated

    return sequence, (a_1, a_2), (p_k_1, p_k_2)


generated_sequence, final_means, final_probabilities = self_training_algorithm(n, dispersion, a_1, a_2, p_k_1, p_k_2, epsilon)
print('Generated sequence: {}'.format(generated_sequence))
print()
print('Final estimates:')
print('a_1: {}'.format(final_means[0]))
print('a_2: {}'.format(final_means[1]))
print('p_1: {}'.format(final_probabilities[0]))
print('p_2: {}'.format(final_probabilities[1]))
