"""Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. The goal of the game is to take the last object."""

from nim_controller import (
    set_up_piles,
    take_from_pile,
    show_positions,
    is_game_over,
    _holder,
)

set_up_piles()

user = 1

while True:
    print("Current position: ")
    print(show_positions())
    print("User #{} is to move".format(user))
    pos = int(input("Take stones from pile: "))
    qua = int(input("How many stones: "))
    print()
    if qua > 0:
        take_from_pile(position=pos, quanity=qua)
    else:
        print("Follow the rules! Enter correct values.")
        continue
    if is_game_over():
        break
    user = 2 if user == 1 else 1

print("The user #", user, "wins")
