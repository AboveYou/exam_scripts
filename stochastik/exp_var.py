# Sebastian Schirle
# 06.01.2021
# calculates the Exp(X) - Erwartungswert and the Var(X) - Varianz

import numpy as np
# PRECISION = 4 decimals

# np-arrays to easily calculate the power of all values
data = [
    # the values for k
    np.array([0, 1, 2, 3, 4, 5, 6]),
    # the values for Pr[X=k]
    np.array([0.015625, 0.09375, 0.234375, 0.3125, 0.234375, 0.09375, 0.015625])
]

# Exp(X)
def exp(k, pr):
    sum = 0
    if len(k) == len(pr):
        # Exp[X] = Sum over elements in k ( k*Pr[X=k] )
        for i in range(len(k)):
            sum += k[i] * pr[i]
        return sum
        # alternative
            # retrun np.around(np.sum(k*pr), decimals=4)
    else:
        # data arrays do not have the same length (sth is wrong)
        return None

# Var(X)
def var(exp1, exp2):
    # Var [X] = Exp[X^2] - Exp[X]^2
    return exp1-exp2

if __name__ == "__main__":
    # Exp[X]
    exp_x = exp(data[0], data[1])
    print("Exp[X] \t = \t %.4f" % exp_x)

    # Exp[X^2]
    exp_x2 = exp(data[0]**2, data[1])
    print("Exp[X^2] = \t %.4f" % exp_x2)

    # Var[X]
    var_x = var(exp_x2, exp_x**2)
    print("Var[X] \t = \t %.4f" % var_x)