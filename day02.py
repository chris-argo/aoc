from __future__ import annotations
from typing import NamedTuple, List

PASSWORDS = ["1-3 a: abcde",
             "1-3 b: cdefg",
             "2-9 c: ccccccccc"]

class Password(NamedTuple):
    low: int
    high: int
    char: str
    password: str

    def is_valid(self):
        count = self.password.count(self.char)
        return self.low <= count <= self.high 

    def is_toboggan_valid(self):
        low_match = self.password[self.low - 1] == self.char
        high_match = self.password[self.high - 1] == self.char
        return low_match ^ high_match



def parse(line: str):
    nums, char, password = line.strip().split()
    char = char[0]
    low, high = [int(n) for n in nums.split("-")]
    return Password(low, high, char, password)


for password in PASSWORDS:
    print((parse(password)).is_valid())
    # print((parse(password)).is_toboggan_valid())

with open("inputs/day02.txt") as f:
    passwords = [parse(line) for line in f]
    print(sum(password.is_valid() for password in passwords))
    print(sum(password.is_toboggan_valid() for password in passwords))