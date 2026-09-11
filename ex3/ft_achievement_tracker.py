import random


def gen_achievments(achievments: list[str]) -> set[str]:
    return (set(random.choices(achievments,
                               k=random.randrange(4, len(achievments)))))


def all_achievments(players: dict[str, set[str]]) -> set[str]:
    ret: set[str] = set()
    for name in players:
        ret = ret.union(players[name])
    return ret


def unique_achievments(players: dict[str, set[str]], player: str,
                       all_collected: set[str]) -> set[str]:
    diff = all_collected
    for name in players:
        if name == player:
            continue
        diff = diff.difference(players[name])
    return (diff)


def get_player_achievments() -> None:
    achievments: list[str] = ['Crafting Genius', 'Strategist',
                              'World Savior', 'Speed Runner',
                              'Survivor', 'Master Explorer',
                              'Treasure Hunter', 'Unstoppable',
                              'First Steps', 'Collector Supreme',
                              'Untouchable', 'Sharp Mind',
                              'Boss Slayer']

    players: dict[str, set[str]] = {'Alice': gen_achievments(achievments),
                                    'Bob': gen_achievments(achievments),
                                    'Charlie': gen_achievments(achievments),
                                    'Dylan': gen_achievments(achievments)}

    all_collected = all_achievments(players)
    common = set(achievments).intersection(*(players[i] for i in players))

    for name in players:
        print(f"\n{name:=^25}")
        print(players[name])
        line = f"Only {name} has"
        print(f"{line:-^25}")
        print(f"{unique_achievments(players, name, all_collected)}")
        print(f"{'but is missing':-^25}")
        print(f"{set(achievments).difference(players[name])}")

    print(f"\nCommon achievments: {common}")
    print(f'\n{"Distinct achievments":=^25}')
    print(f"{all_collected}")


if __name__ == '__main__':
    get_player_achievments()
