import random     # import random module

coin = random.choice(["heads", "tails"])             # random choice b/w heads and tails (both inclusive) with 0.5 probability
#print(coin)


from random import choice     # import choice function from random module
new_coin = choice(["heads", "tails"])             # random choice b/w heads and tails (both inclusive) with 0.5 probability
print(new_coin, coin)

print("------------------\n")

# generate a random int b/w 1 and 6 (both inclusive)
dice = random.randint(1, 6)
print(dice)

print("------------------\n")

# shuffle a list
deck = ["Ace", "King", "Queen", "Jack", "10", "9"]
random.shuffle(deck)
for card in deck:
    print(card)
