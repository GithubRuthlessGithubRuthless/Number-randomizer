import random
import time
print("Рандомайзер чисел")
time.sleep(2)
rangeone = int(input("Введите 1 число:"))
rangetwo = int(input("Введите 2 число:"))
result = random.randint(rangeone, rangetwo)
print(result)
