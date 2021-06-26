import coinModule
import random

print("/////////////////////////////////")
print("Welcome to Coin tossing Programme ")

print(coinModule.coin)

if random.randint(0,1)==0:
    print(coinModule.heads)
else:
    print(coinModule.tails)