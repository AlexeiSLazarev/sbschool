val1 = 0
val1 |= 1 << 0
val2 = 0
val2 |= 1 << 32
print(bin(val1 | val2))
