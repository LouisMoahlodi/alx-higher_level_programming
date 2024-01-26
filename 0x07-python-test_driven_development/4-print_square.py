def print_square(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    if isinstance(size, float) or size < 0:
        raise TypeError("size must be an integer")
    
    else:
        # Print Square
        for i in range(1, size + 1):
            print('#' * size)