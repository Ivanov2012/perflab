import sys
import numpy as np

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal_elements(nums):
    median = int(np.median(nums))
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        
        sys.exit(1)
    
    file_path = sys.argv[1]
    nums = read_numbers(file_path)
    
    result = min_moves_to_equal_elements(nums)
    print(result)
