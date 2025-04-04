"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

def cistercian_rev(number: int) -> list[list[str]]:

    Coord = tuple[int, int]
    Figure = tuple[Coord, Coord, Coord, Coord, Coord, Coord]
    Digit = tuple[int, int, int, int, int, int]

    ones: Figure = (0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)
    tens: Figure = (0, 1), (0, 0), (1, 1), (1, 0), (2, 1), (2, 0)
    hund: Figure = (6, 3), (6, 4), (5, 3), (5, 4), (4, 3), (4, 4)
    thou: Figure = (6, 1), (6, 0), (5, 1), (5, 0), (4, 1), (4, 0)
    numb = thou, hund, tens, ones

    digits: list[Digit] = [
        (0, 0, 0, 0, 0, 0),
        (1, 1, 0, 0, 0, 0),
        (0, 0, 0, 0, 1, 1),
        (0, 0, 1, 0, 0, 1),
        (0, 1, 1, 0, 0, 0),
        (1, 1, 1, 0, 0, 0),
        (0, 1, 0, 1, 0, 1),
        (1, 1, 0, 1, 0, 1),
        (0, 1, 0, 1, 1, 1),
        (1, 1, 0, 1, 1, 1)
    ]
    image: list[list[str]] = [[" ", " ", "0", " ", " "] for _ in range(7)]
    n = str(number).zfill(4)
    for digit, fig in zip(n, numb):
        for (r, c), val in zip(fig, digits[int(digit)]):
            if val:
                image[r][c] = "0"

    return image

from random import randint





TESTS = {
    "Basics": [
        {
            "input": [4],
            "answer": [
                [' ', ' ', '0', ' ', '0'],
                [' ', ' ', '0', '0', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' ']
            ],
        },
        {
            "input": [50],
            "answer": [
                ['0', '0', '0', ' ', ' '],
                [' ', '0', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' ']
            ],
        },
        {
            "input": [600],
            "answer": [
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', '0'],
                [' ', ' ', '0', ' ', '0'],
                [' ', ' ', '0', ' ', '0']
            ],
        },
        {
            "input": [7000],
            "answer": [
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                ['0', ' ', '0', ' ', ' '],
                ['0', ' ', '0', ' ', ' '],
                ['0', '0', '0', ' ', ' ']
            ],
        },
        {
            "input": [1993],
            "answer": [
                ['0', '0', '0', ' ', ' '],
                ['0', ' ', '0', '0', ' '],
                ['0', '0', '0', ' ', '0'],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', '0', '0'],
                [' ', ' ', '0', ' ', '0'],
                ['0', '0', '0', '0', '0']
            ],
        },
    ],
    "Extra": [
        {
            "input": [4723],
            "answer": [
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', '0', ' '],
                ['0', '0', '0', ' ', '0'],
                [' ', ' ', '0', ' ', ' '],
                [' ', ' ', '0', ' ', '0'],
                [' ', '0', '0', ' ', '0'],
                ['0', ' ', '0', '0', '0']
            ]
        },
        {
            "input": [6859],
            "answer": [
                ['0', '0', '0', '0', '0'],
                [' ', '0', '0', ' ', '0'],
                [' ', ' ', '0', '0', '0'],
                [' ', ' ', '0', ' ', ' '],
                ['0', ' ', '0', '0', '0'],
                ['0', ' ', '0', ' ', '0'],
                ['0', ' ', '0', ' ', '0']
            ]
        },
        {
            "input": [7085],
            "answer": [
                ['0', ' ', '0', '0', '0'],
                ['0', ' ', '0', '0', ' '],
                ['0', '0', '0', ' ', ' '],
                [' ', ' ', '0', ' ', ' '],
                ['0', ' ', '0', ' ', ' '],
                ['0', ' ', '0', ' ', ' '],
                ['0', '0', '0', ' ', ' ']
            ]
        },
        {
            "input": [9433],
            "answer": [
                [' ', ' ', '0', ' ', ' '],
                [' ', '0', '0', '0', ' '],
                ['0', ' ', '0', ' ', '0'],
                [' ', ' ', '0', ' ', ' '],
                ['0', '0', '0', ' ', ' '],
                ['0', ' ', '0', '0', ' '],
                ['0', '0', '0', ' ', '0']
            ]
        },
    ],
    "Random": [{"input": [num:=randint(1, 9999)],
                "answer": cistercian_rev(num)}
                for _ in range(20)]
}
