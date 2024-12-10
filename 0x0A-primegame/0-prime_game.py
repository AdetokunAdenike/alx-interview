#!/usr/bin/python3
"""
Module to determine the winner of the Prime Game, where two players,
Maria and Ben, take turns removing primes and their multiples from a
set of integers.
"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of primes up to n using the Sieve of Eratosthenes.

    Args:
    n (int): The upper limit for prime generation.

    Returns:
    list: A list of boolean values where True represents a prime number.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """
    Determine who wins the most rounds in the Prime Game.

    In each round, Maria and Ben alternate picking prime numbers from a set of
    consecutive integers starting from 1 to n. The player unable to make a move
    loses. Maria always starts first, and both players play optimally.

    Args:
    x (int): The number of rounds to play.
    nums (list): A list of integers where each integer n represents the
    upper limit of the set for a round.
    Returns:
    str: The name of the player who won the most rounds. If there is a tie,
    return None.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        sieve = sieve_of_eratosthenes(n)
        remaining_numbers = [True] * (n + 1)

        turn = 0

        while True:
            for i in range(2, n + 1):
                if remaining_numbers[i] and sieve[i]:
                    prime = i
                    break
            else:
                break

            for j in range(prime, n + 1, prime):
                remaining_numbers[j] = False

            turn = 1 - turn

        if turn == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
