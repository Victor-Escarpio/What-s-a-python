print("Vic's magic pet shop")
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Choose your pet:")
print("1. Dragon")
print("2. Phoenix")
print("3. Unicorn")
choice = int(input("Choose (1-3): "))
if choice == 1:
    pet = "Dragon"
elif choice == 2:
    pet = "Phoenix"
elif choice == 3:
    pet = "Unicorn"
else:
    print("Try again!")
print(f"You've adopted a {pet}!")
import random
Power = random.randint(0,5)
if Power == 1:
    petpow = "Ice"
elif Power == 2:
    petpow = "Fire"
elif Power == 3:
    petpow = "Nature"
elif Power == 4:
    petpow = "Magic"
elif Power == 5:
    petpow = "Mechanical"
print(f"Pet Power: {petpow}")
rarity = random.randint(0,100)
if rarity == 1:
    rar = "LEGENDARY!!!"
if rarity > 1 and rarity <= 25:
    rar = "Rare!!"
if rarity > 25 and rarity <= 50:
    rar = "Uncommon!"
if rarity > 50 and rarity < 100:
    rar = "Common :("
print(f"Pet Rarity: {rar}")
prefixes = ["Glim", "Flare", "Shadow", "Ice", "Storm", "Ember", "Luma", "Thorn"]
suffixes = ["fang", "tail", "wing", "scale", "heart", "fire", "whisper", "blaze"]
pet_name = random.choice(prefixes) + random.choice(suffixes)
print(f"Your pet's name is: {pet_name}")



