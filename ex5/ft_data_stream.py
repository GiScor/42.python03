from typing import Generator
import random

names:      list[str] = ['Tizio', 'Caio', 'Sempronio', 'Giovanni',
                         'Bob', 'Gundam', 'Alice', 'Zelda', 'Piergiorgia']

actions:    list[str] = ['shit', 'walk', 'run', 'eat', 'kill',
                         'despair', 'rot', 'sing']


def gen_event(names: list[str], actions: list[str],
              iterations: int) -> Generator[tuple[str, str], None, None]:
    for i in range(iterations):
        yield (random.choice(names), random.choice(actions))


def consume_event(
    events: list[tuple[str, str,]]) -> Generator[tuple[str, str],
                                                 None, None]:
    while events:
        index: int = random.randrange(len(events))
        looser: tuple[str, str] = events.pop(index)
        yield looser


if __name__ == '__main__':
    counter = 0
    for i in gen_event(names, actions, 1000):
        print(f"Event {counter}: "
              f"{i[0]} did action {i[1]}")
        counter += 1

    events: list[tuple[str, str]] = [tup for tup in
                                     gen_event(names, actions, 10)]

    print(f"Built list of 10 events: {events}")
    for i in consume_event(events):
        print(f"Got event from list: {i}")
        print(f"Remaining in list:   {events}")
