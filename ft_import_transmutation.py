# #!/usr/bin/python3


print('')

print('=== Import Transmutation Mastery ===')

print('')

print('Method 1 - Full module import:')
import alchemy.elements
print(f'alchemy.elements.create_fire(): {alchemy.elements.create_fire()}')

print('')

print('Method 2 - Specific function import:')
from alchemy.elements import create_water
print(f'create_fire(): {create_water()}')

print('')

print('Method 3 - Aliased import:')
from alchemy.potions import healing_potion as heal
print(f'heal(): {heal()}')

print('')

print('Method 4 - Multiple import:')
from alchemy.elements import create_fire, create_earth
from alchemy.potions import strenght_potion
print(f"create_earth(): {create_earth()}")
print(f'create_fire(): {create_fire()}')
print(f'strenght_potion(): {strenght_potion()}')

print('')

print('Bonus - package import:')
import alchemy
print(f"alchemy.create_fire(): {alchemy.create_fire()}")

print('')

print('All import transmutation methods mastered!')