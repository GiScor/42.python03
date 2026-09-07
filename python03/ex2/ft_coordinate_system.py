import math


class CoordError(Exception):
    def __init__(self) -> None:
        super().__init__(self)


def try_float(s: str) -> float | None:
    try:
        return float(s)
    except ValueError:
        print(f"ValueError: argument '{s}' is not a valid number")
        print(f"...Ignoring argument '{s}'\n")
        return None


def get_player_pos() -> tuple[float, ...]:
    raw:        list[str] = input("Enter coordinates as floats "
                                  "in format 'x,y,z': ").split(',')
    coord_lst:  list[float] = [n for s in raw
                               if (n := try_float(s)) is not None]
    if len(coord_lst) != 3:
        print("Invald input")
        raise CoordError()
    coordinates:    tuple[float, ...] = tuple(coord_lst)
    return (coordinates)


def euclide(coord1: tuple[float, ...], coord2: tuple[float, ...]) -> float:
    x1: float = coord1[0]
    y1: float = coord1[1]
    z1: float = coord1[2]
    x2: float = coord2[0]
    y2: float = coord2[1]
    z2: float = coord2[2]

    result = math.sqrt((x2-x1)**2 +
                       (y2-y1)**2 +
                       (z2-z1)**2)

    return round(result, 2)


def print_coord(coord: tuple[float, ...], n: int) -> None:
    i: int = 0
    end = ', '
    for c in ['X', 'Y', 'Z']:
        if i == 2:
            end = '\n'
        print(f"{c}{n}={coord[i]}", end=end)
        i += 1


def coordinate_system() -> None:
    print("Get first set of coordinates")
    coord1 = None
    while not coord1:
        try:
            coord1 = get_player_pos()
        except CoordError:
            coord1 = None
    print(f"Got first tuple: {coord1}")
    print("It includes:", end=" ")
    print_coord(coord1, 1)
    print(f"Distance from center: {euclide(coord1, (0, 0, 0))}")

    print("Get second set of coordinates")
    coord2 = None
    while not coord2:
        try:
            coord2 = get_player_pos()
        except CoordError:
            coord2 = None
    print(f"Got second tuple: {coord2}")
    print("It includes:", end=" ")
    print_coord(coord2, 2)
    print(f"Distance between the two sets of coordinates: "
          f"{euclide(coord2, coord1)}")


def main() -> None:
    coordinate_system()


main()
