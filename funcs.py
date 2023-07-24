import random
import numpy as np

def list2bin(list: list[int] = [], width: int = 32) -> list[str]:
    """This function returns the binary representation of `list` on `width` bits """
    binList = []
    
    for num in list:
        binList.append(np.binary_repr(num, width=width))  
         
    return binList


def randomInts(signed: bool = False, amount: int = 10, width: int = 32) -> list[int]:
    """This function returns a list of `amount` random integers, signed or unsigned, representable with `width` bits """
    rng = random.SystemRandom()
    intList = []
    
    if (signed):
        lowerBound = -2**(width - 1)
        upperBound = 2**(width - 1) - 1
    else:
        lowerBound = 0
        upperBound = 2**width - 1
        
    for i in range(0, amount):
        intList.append(round(rng.uniform(lowerBound, upperBound)))
        
    return intList
    
