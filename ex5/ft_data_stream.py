from typing import Generator
import random

names:      list[str] = ['Tizio', 'Caio', 'Sempronio', 'Giovanni',
                         'Bob', 'Gundam', 'Alice', 'Zelda', 'Piergiorgia']

actions:    list[str] = ['shit', 'walk', 'run', 'eat', 'kill',
                         'despair', 'rot', 'sing']


def gen_event(names: list[str], actions: list[str],
              iterations: int) -> Generator:
    for i in range(iterations):
        yield (random.choice(names), random.choice(actions))


def consume_event(events: list[tuple[str, str,]]) -> Generator:
    while events:
        index: int = random.randrange(len(events))
        looser: tuple[str, str] = events[index]
        yield looser
        events = events[:index] + events[index+1:]
        yield events


if __name__ == '__main__':
    counter = 0
    for i in gen_event(names, actions, 1000):
        print(f"Event {counter}: "
              f"{i[0]} did action {i[1]}")
        counter += 1

    events: list[tuple[str, str]] = [tup for tup in
                                     gen_event(names, actions, 10)]

    print(f"Built list of 10 events: {events}")
    switch: int = 1
    for i in consume_event(events):
        if switch > 0:
            print(f"Got event from list: {i}")
        else:
            print(f"Remaining in list:   {i}")
        switch *= -1
