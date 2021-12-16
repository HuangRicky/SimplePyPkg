from mod1 import mod1_f1_fun1_mean, mod1_f2_fun2_generate_x
from mod2 import *


x = mod1_f2_fun2_generate_x()

x_mean = mod1_f1_fun1_mean(x)
print("x_mean is ")
print(x_mean)

x_max = mod2_f3_fun3_max(x)
print("x_max is ")
print(x_max)

