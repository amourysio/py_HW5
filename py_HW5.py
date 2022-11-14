import numpy as np
# recursive function


def func(x):
    return 1 if x <= 1 else x * func(x - 1)


print(func(6))

randomList = np.random.randint(1, 10, size=(3, 3))

result = list(map(lambda x: sum(x),randomList))
result = list(filter(lambda x: np.sqrt(x) * np.sqrt(x) == x, result))
print(result)
