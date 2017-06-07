#!/usr/bin/python
# -*- Coding:UTF-8 -*-


"""
      guess number play, when play end,
      ask player want to play or not ,
      if the answer is Y then go on,
      or ending the game.

"""


from __future__ import print_function
import random


def guess_number(number):
    while True:
        a = int(input("Please input a number:"))
        if a > number:
            print("It is a little big")
        elif a < number:
            print("It is a little small")
        else:
            print("You guess it")
            break


def main():
    print("------------------begin game------------")
    number = random.randint(0, 99)
    guess_number(number)
    choice = raw_input("Do you want to play again?Y/N")
    if choice == "Y":
        guess_number(number)


if __name__ == '__main__':
    main()
