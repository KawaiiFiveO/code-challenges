import random

def generate_random_forest(n, unicorn_percentage=10, tree_percentage=20):
    """
    Generates a random forest grid of size n x n.
    
    Parameters:
    n: int - size of the grid (n x n)
    unicorn_percentage: int - percentage of grid cells that will contain unicorns ('U')
    tree_percentage: int - percentage of grid cells that will contain trees ('T')
    
    Returns:
    forest: list of lists - generated forest grid
    start_position: tuple - random starting position (r_start, c_start)
    """
    # Create an empty grid filled with '.'
    forest = [['.' for _ in range(n)] for _ in range(n)]
    
    # Calculate number of unicorns and trees to place
    total_cells = n * n
    num_unicorns = total_cells * unicorn_percentage // 100
    num_trees = total_cells * tree_percentage // 100
    
    # Randomly place unicorns ('U')
    unicorn_positions = random.sample(range(total_cells), num_unicorns)
    for pos in unicorn_positions:
        r, c = divmod(pos, n)
        forest[r][c] = 'U'
    
    # Randomly place trees ('T')
    tree_positions = random.sample([i for i in range(total_cells) if i not in unicorn_positions], num_trees)
    for pos in tree_positions:
        r, c = divmod(pos, n)
        forest[r][c] = 'T'
    
    # Choose a random starting position that is empty ('.')
    empty_positions = [i for i in range(total_cells) if forest[i // n][i % n] == '.']
    start_pos = random.choice(empty_positions)
    r_start, c_start = divmod(start_pos, n)
    
    return forest, (r_start, c_start)

def print_forest(forest):
    """Prints the forest grid in a readable format."""
    for row in forest:
        print(' '.join(row))

# Example usage
n = 7  # Grid size (n x n)
unicorn_percentage = 10  # Percentage of unicorns
tree_percentage = 20  # Percentage of trees

# Generate random test case
forest, start_position = generate_random_forest(n, unicorn_percentage, tree_percentage)

# Print the generated forest and starting position
print("Generated Forest:")
print_forest(forest)
print("\nStarting Position:", start_position)
