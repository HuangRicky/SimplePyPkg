import pandas as pd


# you can use __all__ variable to specify what to import when from x import *
__all__ = ['mod1_f2_fun2_generate_x']


def mod1_f2_fun2_generate_x():
    x = pd.Series([1, 1.5, 2, 2.25, 3])
    return x
