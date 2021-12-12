from Machine import MACHINE
from random import shuffle, seed
import random
seed(42)

map_1 = ['A', 'B', 'C', 'D', 'E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
map_2 = ['A', 'B', 'C', 'D', 'E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
map_3 = ['A', 'B', 'C', 'D', 'E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(map_1)
shuffle(map_1)
shuffle(map_2)
shuffle(map_3)
print(map_1)
print(map_2)
print(map_3)
map_inverse = ['B', 'A', 'D', 'C', 'F','E', 'H','G','J','I','L','K','N','M','P','O','R','Q','T','S','V','U','X','W','Z','Y']

Enigma = MACHINE(map_1,map_2,map_3,map_inverse)

while 1:
    x = input()
    for i in x:
        try:
            print(Enigma.encode(i),end='')
        except:
            print('Invalid Input')
    print('')


# while 1:
#     x = input()
#     for i in x:
#         try:
#             print(Enigma.encode(i))
#             print('---')
#         except:
#             print('Invalid Input')