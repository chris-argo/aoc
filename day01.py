from typing import List

INPUT = [1721, 979, 366, 299, 675, 1456]

def find_product(input: List) -> int:
    for i in input:
        for j in input:
            if i + j == 2020:
                return i * j

def find_triple_product(input: List) -> int:
    for i in input:
        for j in input:
            for k in input:
                if i + j + k == 2020:
                    return i * j * k

print(find_product(INPUT))

with open("inputs/day01.txt") as f:
    inputs = [int(line.strip()) for line in f]

print(find_product(inputs))
print(find_triple_product(inputs))