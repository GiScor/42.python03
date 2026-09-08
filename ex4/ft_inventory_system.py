import sys


class QuantityError(Exception):
    def __init__(self, message: str = "Quantity error"):
        super().__init__(message)


class FormatError(Exception):
    def __init__(self, message: str = "Format error"):
        super().__init__(message)


class RedundancyError(Exception):
    def __init__(self, message: str = "Redundancy error"):
        super().__init__(message)


def try_int(s: str) -> int | None:
    try:
        if int(s) <= 0:
            raise ValueError
        return int(s)
    except ValueError:
        print(f"ValueError: argument '{s}' is not a valid int")
        return None


def try_dict(arg: str, inv: dict) -> list[str]:
    colon: int = 0
    count: int = 0
    for i in range(len(arg)):
        if arg[i] == ':':
            colon = i
            count += 1
    if colon < 1 or count != 1:
        raise FormatError(f"Invalid colon position in '{arg}'")
    if arg[:colon] in inv:
        raise RedundancyError(f"Redundant item '{arg}' -- discarding")
    return([arg[:colon], try_int(arg[colon+1:])])



if __name__ == '__main__':
    args:   list[str] = sys.argv[1:]
    inv:    dict = {}
    for arg in args:
        try:
            if try_dict(arg, inv)[1] is not None:
                inv.update({try_dict(arg, inv)[0]: try_dict(arg, inv)[1]})
        except (FormatError, RedundancyError) as e:
            print(e)
    print(inv)
