import sys

def circular_path(n, m):
    circular_array = list(range(1, n + 1))
    

    path = []
    
    
    current_index = 0
    while True:
        
        interval = []
        for _ in range(m):
            interval.append(circular_array[current_index])
            current_index = (current_index + 1) % n
        
        
        path.append(interval[0])
        
        
        if interval[-1] == circular_array[0]:
            break
    
    
    return ''.join(map(str, path))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        
        sys.exit(1)
    
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    
    result = circular_path(n, m)
    
    
    print(result)