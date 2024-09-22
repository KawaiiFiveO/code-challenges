def count_visible_unicorns(forest, r_start, c_start):
    # TODO: Implement the function to count visible unicorns based on the problem statement.
    pass  # Replace this with your implementation


def run_tests():
    # Test cases: (forest, r_start, c_start, expected_answer)
    test_cases = [
        (
            [
                ['U', '.', 'T', 'U', '.', '.', 'T'],
                ['T', '.', 'T', '.', 'U', '.', '.'],
                ['.', 'U', '.', '.', '.', 'T', '.'],
                ['.', '.', 'U', 'T', '.', 'U', '.'],
                ['U', '.', 'T', '.', '.', '.', 'U'],
                ['.', 'T', '.', 'U', '.', '.', 'T'],
                ['U', '.', 'U', '.', 'T', '.', '.']
            ],
            3,  # r_start
            4,  # c_start
            1   # expected answer
        ),
        # Add more test cases here
    ]

    for i, (forest, r_start, c_start, expected) in enumerate(test_cases):
        result = count_visible_unicorns(forest, r_start, c_start)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed!")


if __name__ == "__main__":
    run_tests()
