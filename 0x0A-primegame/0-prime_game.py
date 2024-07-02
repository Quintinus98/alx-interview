#!/usr/bin/python3
"""Prime game"""


def findPrime(MAX):
    """Returns a list of prime numbers"""
    pm = [True] * (MAX + 1)

    # use sieve to find prime
    pm[0], pm[1] = False, False
    for i in range(2, MAX + 1):
        if pm[i] == True:
            for j in range(2 * i, MAX + 1, i):
                pm[j] = False
    # store the prime numbers
    prime = []
    for i in range(0, MAX + 1):
        if pm[i] == True:
            prime.append(i)

    return prime


def isWinner(x, nums):
    """The player that cannot make a move loses the game.

    Return: name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None

    pm = findPrime(max(nums))
    primes = set(pm)
    players = {"Maria": 0, "Ben": 0}

    for num in nums:
        num_set = set(range(1, num + 1))
        # initial turn
        turn = 0

        while True:
            moves = [p for p in primes if p in num_set]
            if not moves:
                break
            move = moves[0]

            # Remove multiples
            multiples_of_move = set(range(move, num + 1, move))
            num_set -= multiples_of_move

            turn = 1 - turn

        if turn:
            players["Maria"] += 1
        else:
            players["Ben"] += 1

    if players["Maria"] < players["Ben"]:
        return "Ben"
    elif players["Maria"] > players["Ben"]:
        return "Maria"
    else:
        return None


# def isWinner(x, nums):
#     """The player that cannot make a move loses the game.

#     Return: name of the player that won the most rounds
#     """
#     if not nums or x < 1:
#         return None

#     players = {"Maria": 0, "Ben": 0}

#     for num in nums:
#         pm = findPrime(num)
#         numlist = [i for i in range(num + 1)]
#         initScores = {"Maria": 0, "Ben": 0}
#         turn = 0

#         for k in range(x):
#             try:
#                 choice = pm[0]
#                 del pm[0]
#                 numlist = [elem for elem in numlist if elem % choice != 0]

#                 if turn == 0:
#                     initScores["Maria"] += 1
#                 else:
#                     initScores["Ben"] += 1
#                 turn = 1 - turn

#             except IndexError:
#                 break

#         if initScores["Maria"] == initScores["Ben"] and k < x - 1:
#             players["Ben"] += 1
#         if initScores["Maria"] > initScores["Ben"]:
#             players["Maria"] += 1

#     if players["Maria"] == players["Ben"]:
#         return None
#     if players["Maria"] > players["Ben"]:
#         return "Maria"
#     if players["Maria"] < players["Ben"]:
#         return "Ben"
