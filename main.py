def main():
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


if __name__ == "__main__":
    main()
