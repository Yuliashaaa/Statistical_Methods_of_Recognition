# All imports for task
import random

# Define constants
sequence_length = 100
occurrence_probability = 0.5
steps = 1000
calculated_penalty = 0


def generate_original_sequence(length):
    return [random.choice([0, 1]) for _ in range(length)]


def generate_changed_sequence(sequence, probability):
    return [(1 - entry) if (random.random() < probability) else entry for entry in sequence]


def calculate_penalty(sum_1, sum_2):
    return (sum_1 - sum_2) ** 2


def calculate_optimal_sum(sequence, length, probability):
    sequence_sum = sum(sequence)
    original_sequence_expected_sum = sequence_sum * (1 - probability) + (length - sequence_sum) * probability
    original_sequence_expected_sum = round(original_sequence_expected_sum)
    sum_penalty = calculate_penalty(original_sequence_expected_sum, sequence_sum)

    return original_sequence_expected_sum, sum_penalty


original_sequence = generate_original_sequence(sequence_length)
changed_sequence = generate_changed_sequence(original_sequence, occurrence_probability)
optimal_sum, penalty = calculate_optimal_sum(changed_sequence, sequence_length, occurrence_probability)

print('Original sequence: {}'.format(original_sequence))
print('Changed sequence: {}'.format(changed_sequence))
print('Optimal sum: {}'.format(optimal_sum))
print('Penalty: {}'.format(penalty))
print()

for _ in range(steps):
    original_sequence = generate_original_sequence(sequence_length)
    changed_sequence = generate_changed_sequence(original_sequence, occurrence_probability)
    optimal_sum, penalty = calculate_optimal_sum(changed_sequence, sequence_length, occurrence_probability)
    calculated_penalty += penalty

average_penalty = calculated_penalty / steps
print('Average penalty: {}'.format(average_penalty))
