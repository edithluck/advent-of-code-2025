def day1():
    zeros = 0
    position = 50
    
    with open("codes.txt", "r") as file:
        codes = file.readlines()

    for code in codes:
        print(code)
        direction = code[0]
        distance = int(code[1:])
        print(direction, distance)
        if direction == "L":
            for i in range(distance):
                if position == 0:
                    position = 99
                else:
                    position -= 1
                    if position == 0:
                        zeros += 1
        elif direction == "R":
            for i in range(distance):
                if position == 99:
                    position = 0
                    zeros += 1
                else:
                    position += 1
        
        
    print(zeros)

def is_invalid_id(id_num):
    """
    Check if an ID is invalid (made of a sequence of digits repeated at least twice).
    Examples: 55 (5 twice), 111 (1 three times), 12341234 (1234 twice), 
              123123123 (123 three times), 1212121212 (12 five times)
    """
    id_str = str(id_num)
    n = len(id_str)
    
    # Try all possible pattern lengths from 1 to n//2
    # The pattern must repeat at least 2 times, so max pattern length is n//2
    for pattern_len in range(1, n // 2 + 1):
        # Check if n is divisible by pattern_len (so pattern can repeat evenly)
        if n % pattern_len != 0:
            continue
        
        pattern = id_str[:pattern_len]
        num_repeats = n // pattern_len
        
        # Must repeat at least 2 times
        if num_repeats < 2:
            continue
        
        # Check if the entire string is just the pattern repeated
        if pattern * num_repeats == id_str:
            return True
    
    return False

def day2():
    with open("ids.txt", "r") as file:
        content = file.read().strip()
    
    # Parse ranges
    ranges = []
    for range_str in content.split(","):
        first, last = map(int, range_str.split("-"))
        ranges.append((first, last))
    
    # Find all invalid IDs
    invalid_ids = []
    for first, last in ranges:
        for id_num in range(first, last + 1):
            if is_invalid_id(id_num):
                invalid_ids.append(id_num)
    
    # Sum all invalid IDs
    total = sum(invalid_ids)
    print(f"Total invalid IDs: {len(invalid_ids)}")
    print(f"Sum of invalid IDs: {total}")
    return total

def main():
    day2()

if __name__ == "__main__":
    main()
