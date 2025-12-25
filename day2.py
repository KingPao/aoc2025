import math

test_input = [
    "11 - 22",
    "95 - 115",
    "998 - 1012",
    "1188511880 - 1188511890",
    "222220 - 222224",
    "1698522 - 1698528",
    "446443 - 446449",
    "38593856 - 38593862",
    "565653 - 565659",
    "824824821 - 824824827",
    "2121212118 - 2121212124"
]

with open("input/day2.txt") as f:
    day_input = f.read().split(",")


def convert_input_to_number(input_string):
    s = input_string.split("-")
    return int(s[0]), int(s[1])


def _count_digit(number):
    return math.floor(math.log10(number)) + 1


def star_1():
    for i in used_input:
        start, end = convert_input_to_number(i)
        all_number_set = set(range(start, end + 1))

        if _count_digit(start) == _count_digit(end):
            if _count_digit(start) % 2 != 0:
                continue
            x = _count_digit(start)
        elif _count_digit(end) % 2 == 0:
            x = _count_digit(end)
        elif _count_digit(start) % 2 == 0:
            x = _count_digit(start)
        else:
            print("fuck")
            break

        x /= 2
        pattern = int(math.pow(10, x)) + 1
        start = int(math.pow(10, x))
        end = int(math.pow(10, x + 1))

        pattern_set = set(range(start, end, pattern))

        result_set = all_number_set.intersection(pattern_set)
        print(len(result_set))


def star_2():
    pass


used_input = test_input

if __name__ == "__main__":
    star_1()
