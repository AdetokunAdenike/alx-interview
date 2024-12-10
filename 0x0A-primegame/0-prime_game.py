#!/usr/bin/python3
"""
Module to determine the winner of the Prime Game, where two players,
Maria and Ben,
take turns removing primes and their multiples from a set of integers.
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
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
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

    # Iterate through each round and calculate the winner
    for n in nums:
        # Generate primes up to n
        sieve = sieve_of_eratosthenes(n)
        prime_count = sum(sieve)  # Count the number of primes

        # Determine the winner for this round based on the number of primes
        if prime_count % 2 == 1:
            maria_wins += 1  # Maria wins if the count is odd
        else:
            ben_wins += 1  # Ben wins if the count is even

    # Return the overall winner based on the most rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
