import os

for k, v in os.environ.items():
    print(k.ljust(10), v)