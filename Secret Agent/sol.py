def SecretAgent(pin):
    digit_equivalent = {
        "0": ["0", "8"],
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": ["3", "5", "6", "9"],
        "7": ["4", "7", "8"],
        "8": ["0", "5", "7", "8", "9"],
        "9": ["6", "8", "9"]
    }

    comb = []
    for digit in reversed(pin):
        arr = digit_equivalent[digit]
        comb = get_combinations(arr, comb)
    return comb


def get_combinations(arr1, arr2):
    combination = []
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    for i in arr1:
        for j in arr2:
            combination.append(i + j)

    return combination


if __name__ == "__main__":
    pin = input("")
    combinations = SecretAgent(pin)
    print(" ".join(combinations))
