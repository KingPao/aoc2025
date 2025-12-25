test_input = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]

with open("input/day1.txt") as f:
    day1_input = f.read().splitlines()


def convert_input_to_number(input_string):
    direction = input_string.strip()[0]

    if direction == "L":
        return -int(input_string[1:])
    elif direction == "R":
        return int(input_string[1:])

    raise ValueError("Invalid direction")


def sign(num):
    return -1 if num < 0 else 1


def star_1(dial_state):
    zero_counter = 0
    for number in used_input:
        direction_number = convert_input_to_number(number)
        dial_state += direction_number

        if dial_state == 0 or dial_state % 100 == 0:
            zero_counter += 1

    print(zero_counter)


def star_2(dial_state):
    zero_counter = 0
    for number in used_input:
        direction_number = convert_input_to_number(number)
        sign_one = sign(direction_number)
        for _ in range(abs(direction_number)):
            dial_state += sign_one
            if dial_state == 0 or dial_state % 100 == 0:
                zero_counter += 1

    print(zero_counter)


used_input = day1_input
dial_state = 50

if __name__ == "__main__":
    star_2(dial_state)
