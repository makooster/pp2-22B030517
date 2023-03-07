import os

print(os.access(".", os.F_OK))
print(os.access(".", os.R_OK))
print(os.access(".", os.W_OK))
print(os.access(".", os.X_OK))