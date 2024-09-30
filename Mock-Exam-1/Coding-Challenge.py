def can_afford(cost):
    # Define available coins
    coins = {
        0.01: 6,
        0.02: 4,
        0.05: 7,
        0.10: 6,
        0.20: 4,
        0.50: 10,
        1.00: 6,
        2.00: 2
    }

    # Dictionary to store the number of each coin used
    used_coins = {
        0.01: 0,
        0.02: 0,
        0.05: 0,
        0.10: 0,
        0.20: 0,
        0.50: 0,
        1.00: 0,
        2.00: 0
    }

    # Convert cost to a floating point with 2 decimal places precision
    remaining = round(cost, 2)

    # Try using the highest denomination coins first
    for coin in sorted(coins.keys(), reverse=True):
        while remaining >= coin and coins[coin] > 0:
            remaining = round(remaining - coin, 2)  # Subtract coin value
            coins[coin] -= 1  # Decrease available coins
            used_coins[coin] += 1  # Record used coin

    # If the remaining cost is 0, return the used coins
    if remaining == 0:
        return used_coins
    else:
        return "Window shopping only bestie!"

print(can_afford(12.50))
print(can_afford(16.90))