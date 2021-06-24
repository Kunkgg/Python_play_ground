# -*- coding: utf-8 -*-
import copy

x = [1]

x.append(x)

y = copy.deepcopy(x)

print(f"x: {x}")
print(f"y: {y}")

print(f"x == y: {x == y}")
