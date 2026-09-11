import sys


class QuantityError(Exception):
    def __init__(self, message: str = "Quantity error") -> None:
        super().__init__(message)


class FormatError(Exception):
    def __init__(self, message: str = "Format error") -> None:
        super().__init__(message)


class RedundancyError(Exception):
    def __init__(self, message: str = "Redundancy error") -> None:
        super().__init__(message)


def try_dict(arg: str, inv: dict[str, int]) -> tuple[str, int]:
    colon: int = 0
    count: int = 0
    for i in range(len(arg)):
        if arg[i] == ':':
            colon = i
            count += 1
    if colon < 1 or count != 1:
        raise FormatError(f"Error - invalid parameter '{arg}'")
    if arg[:colon] in inv:
        raise RedundancyError(f"Redundant item '{arg[:colon]}' - discarding")
    try:
        int(arg[colon+1:])
        return ((arg[:colon], int(arg[colon+1:])))
    except ValueError:
        raise QuantityError(f"QuantityError for '{arg[:colon]}': "
                            f"invalid literal for "
                            f"int() with base 10: '{arg[colon+1:]}'")


def find_max(inv: dict[str, int]) -> str:
    high:    str = ''
    high_n:  int = 0
    for i in inv:
        if inv[i] > high_n:
            high = i
            high_n = inv[i]
    return (high)


def find_min(inv: dict[str, int]) -> str:
    low:    str = list(inv.keys())[0]
    low_n:  int = list(inv.values())[0]
    for i in inv:
        if inv[i] < low_n:
            low = i
            low_n = inv[i]
    return (low)


if __name__ == '__main__':
    args:   list[str] = sys.argv[1:]
    inv:    dict[str, int] = {}
    for arg in args:
        try:
            key, val = try_dict(arg, inv)
            inv[key] = val
        except (FormatError, RedundancyError, QuantityError) as e:
            print(e)
    items: list[str | int] = [i for i in inv.keys()]
    print(f"Got inventory: {inv}")
    print(f"Item list: {items}")
    print(f"Total quantity of the {len(items)} items: {sum(inv.values())}")
    if len(items) > 1:
        for i in inv.keys():
            print(f"Item {i} represents "
                  f"{((inv[i] / sum(inv.values())) * 100):.2f}%")
        print(f"Item most abundant: {find_max(inv)} "
              f"with quantity {inv[find_max(inv)]}")
        print(f"Item least abundant: {find_min(inv)} "
              f"with quantity {inv[find_min(inv)]}")
    else:
        print("\nDude you're so fucking broke. Here, take this!")
    inv.update({'CACCONA': 999999999})
    print(f"Updated inventory: {inv}")
