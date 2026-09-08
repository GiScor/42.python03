import sys


def scoreboard(scores: list[int]) -> None:
    o_scores:       list[int] = order_scores(scores)
    total:          int = sum(scores)
    avg:            float = total / len(scores)
    high_score:     int = max(scores)
    low_score:      int = min(scores)
    total_players:  int = len(scores)
    longest:        int = 0

    tab1:           list[str] = [
        "Total players",
        "Total score",
        "Average score",
        "Lowest score",
        "Score range",
        "High Score",
    ]
    for n in tab1:
        if n == "Leaderboard":
            continue
        else:
            longest = max(longest, len(n))
    width:          int = max(count_char(max(o_scores)), longest)
    padding:        int = width // 2
    tab2:           list[int | float | list[int]] = [
        total_players,
        total,
        avg,
        low_score,
        high_score - low_score,
        high_score,
    ]
    if longest > padding:
        padding = longest
        width = padding*2
    print(f" {'SCORE ANALYTICS':+^{width+padding+padding+4}} ")
    count = 1
    for i in range(1, 6):
        name:   str = tab1[i]
        val:    int | float | list[int] = tab2[i]
        osc_animation(width, padding, 3)
        if name != "High Score":
            row = pretty(name, val, width, padding,)
        else:
            print(" ", "+" * (row-2), sep="")
            row = pretty(None, name, width, padding, fill='~', align='^')
            row = pretty(None, val, width, padding, fill='~', align='^')
            print(" ", "+" * (row-2), sep="")
    print("|", end='')
    row = pretty(None, "Leaderboard", width, padding,
                 fill=' ', align='^', wrap='', end=' ')
    print("|")
    for j in o_scores:
        row = pretty(count, j, width, padding, fill='.', align='^')
        count += 1
    print(f" {'GAME OVER':+^{width+padding+padding+4}} ")


def pretty(name: str | int | None, val: list[int] | int | float | str | None,
           width: int, padding: int, fill: str = '.',
           align: str = '>', end: str = '\n', wrap: str = '|') -> int:
    if name is None:
        if align == '^':
            col1 = f" {fill:{fill}>{padding-1}} {wrap}"
            col2 = f"{val:{align}{width + 3}}"
            col3 = f"{wrap :{fill}<{padding-2}} "

            print(f"{wrap}{col1 + col2 + col3}{wrap}", end=end)
            return (len(f"{wrap}{col1 + col2 + col3}{wrap}"))
    else:
        if align == '^':
            col1 = f" {name:~>{padding+1}}"
            col2 = f" {val:{fill}>{width + 2}}{wrap}"
            col3 = f" {wrap:~>{padding-2}}"
            print(f"{wrap}{col1 + col2 + col3}", end=end)
            return (len(f"{wrap}{col1 + col2 + col3}"))
        else:
            col1 = f"{f'{name}':>{padding}} {wrap}"
            col2 = f" {f' {val} ':{fill}{align}{width + padding + 1}}{wrap}"
            print(f"{wrap}{col1 + col2}", end=end)
            return (len(f"{wrap}{col1 + col2}"))
    return (0)


def osc_animation(width: int, padding: int, time: int) -> None:
    width *= 2
    left:   int = 0
    right:  int = width
    l_mod:  int = +1
    r_mod:  int = -1
    i:      int = 0
    while i < width:
        to_print = (' ' * left) + 'OwO' + (' ' * right)
        left += l_mod
        right += r_mod
        if left >= width or left <= 0:
            l_mod *= -1
            r_mod *= -1
        i += 1
        print(f"  {to_print}", end='\r', flush=True)
        my_sleep(time)
    print('\r', end='\r', flush=True)


def try_int(s: str) -> int | None:
    try:
        if int(s) <= 0:
            raise ValueError
        return int(s)
    except ValueError:
        print(f"ValueError: argument '{s}' is not a valid score")
        my_sleep(50)
        print(f"...Ignoring argument '{s}'\n")
        my_sleep(150)
        return None


def order_scores(scores: list[int]) -> list[int]:
    o_scores = scores
    temp = 0
    while not check_order(o_scores):
        for i in range(0, len(o_scores)-1):
            if o_scores[i] < o_scores[i+1]:
                temp = o_scores[i]
                o_scores[i] = o_scores[i+1]
                o_scores[i+1] = temp
        i = 0
    return (o_scores)


def check_order(scores: list[int]) -> bool:
    for i in range(0, len(scores)-1):
        if scores[i] < scores[i+1]:
            return False
    return True


def my_sleep(intensity: int) -> int:
    total:  int = 0
    for _ in range(intensity * 100_000):
        total += 1
    return total


def calc_width(lst: list[int]) -> int:
    total:  int = len(lst) * 2
    for i in lst:
        total += count_char(i)
    return total


def count_char(i: int) -> int:
    total:  int = 1
    while i // 10 > 0:
        i = i // 10
        total += 1
    return total


def main() -> None:
    args:   list[str] = sys.argv[1:]

    if len(args) > 0:
        scores: list[int] = [n for s in args if (n := try_int(s)) is not None]
        # the walrus operator [:=] assigns and evaluates in a single statement
        if not scores:
            print("No scores submitted!")
            return
        if len(scores) < 3:
            print("Not a lot of scores, this will be boring!")
        scoreboard(scores)
    else:
        print("No scores submitted!")


main()
