from typing import Counter

RAW = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def count_union_yes(raw: str) -> int:
    total_count = 0;
    groups = raw.split("\n\n")
    for group in groups:
        #answers = { answer for people in group.split("\n") for answer in people }
        answers = set()
        for people in group.split("\n"):
            for answer in people:
                answers.add(answer)
        total_count += len(answers)
    return total_count

assert count_union_yes(RAW) == 11

def count_intersect_yes(raw: str) -> int:
    total_count = 0;
    groups = raw.split("\n\n")
    for group in groups:
        people = group.split("\n")
        yes_answers = Counter(answer for person in people for answer in person)
        for c, count in yes_answers.items():
            print(c, count, len(people))
        total_count += sum(count == len(people) for c, count in yes_answers.items())
    return total_count

assert count_intersect_yes(RAW) == 6


with open("inputs/day06.txt") as f:
    raw = f.read()
    print(count_union_yes(raw))
    print(count_intersect_yes(raw))