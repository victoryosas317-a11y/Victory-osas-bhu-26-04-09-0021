# Numbers.py
# Functions for basic statistical operations on a list of numbers.


def sum_numbers(numbers):
    """Return the sum of all numbers in the list."""
    return sum(numbers)


def average(numbers):
    """Return the mean (average) of the numbers in the list."""
    if not numbers:
        raise ValueError("The list must not be empty.")
    return sum(numbers) / len(numbers)


def median_mode(numbers):
    """Return the median and mode(s) of the numbers in the list."""
    if not numbers:
        raise ValueError("The list must not be empty.")

    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)

    # Find the median.
    if count % 2 == 1:
        median = sorted_numbers[count // 2]
    else:
        middle_right = count // 2
        middle_left = middle_right - 1
        median = (sorted_numbers[middle_left] + sorted_numbers[middle_right]) / 2

    # Find the mode(s).
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1

    highest_frequency = max(frequencies.values())

    if highest_frequency == 1:
        modes = []  # No number occurs more than once.
    else:
        modes = [
            number
            for number, frequency in frequencies.items()
            if frequency == highest_frequency
        ]

    return median, modes


# Example usage:
if __name__ == "__main__":
    values = [2, 4, 4, 6, 8]

    print("Sum:", sum_numbers(values))
    print("Average:", average(values))

    median, modes = median_mode(values)
    print("Median:", median)
    print("Mode:", modes)
