import numpy as np

def return_it(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    return_it(np.arange(1, 11))