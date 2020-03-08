"""Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. The goal of the game is to take the last object."""


from random import randint


_holder = []


def set_up_piles():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 10))


def take_from_pile(position, quanity):
    if 1 <= position <= len(_holder):
        _holder[position - 1] -= quanity


def show_positions():
    return _holder


def is_game_over():
    return sum(_holder) == 0
