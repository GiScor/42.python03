import random

names:          list[str] = ['Tizio', 'Caio', 'Sempronio', 'Giovanni',
                             'Bob', 'Gundam', 'alice', 'Zelda', 'piergiorgia',
                             'mario', 'luca', 'antonello', 'giada', 'mariano']
names_all_caps: list[str] = [n.capitalize() for n in names]
names_caps_only: list[str] = [n for n in names if n[0].isupper()]
score: dict[str, int] = {n: random.randrange(1000) for n in names_all_caps}
top_half: dict[str, int] = {k: score[k] for k in score
                            if score[k] > (sum(score.values()) / len(score))}


if __name__ == '__main__':
    print(f"Initual list of players: {names}")
    print(f"List with capitalized names: {names_all_caps}")
    print(f"List with capitalized names only: {names_caps_only}")
    print(f"Score dict: {score}")
    print(f"Top {len(score) // 2} scores: {top_half}")
