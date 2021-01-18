# Sebastian Schirle
# 06.01.2021
# transform into Standartnormalverteilung and perform table lookup 

from scipy.stats import norm
import math

# format
#   N(my,sigma^2)

my = 5
# sigma_pre = sigma^2
sigma_pre = 2
sigma = math.sqrt(sigma_pre)
# values to comparte to (order matters)
#   e.g. Pr[4.01 <= X <= 5.14] -> k[0] = 4.01, k[1] = 5.14
k = [4.01, 5.14]

print("My \t %.2f" % my)
print("Sigma \t %f" % sigma)
print("k \t %s\n" % k)

def calculate(k):
    # transform into Standartnormalverteilung - N(0,1)
    y = (k-my)/sigma
    # round to 2 decimals
    y = round(y, 2)
    # table lookup (also handles negative values)
    return norm.cdf(y)

if __name__ == "__main__":
    # Pr[X <= k] and Pr[X >= k]
    for el in k:
        print("Pr[X <= %.4f] = %f" % (el, calculate(el)))
        print("Pr[X >= %.4f] = %f\n" % (el, 1-calculate(el)))
    # Pr[k1 <= X <= k2]
    if(len(k) == 2):
        print("Pr[%.4f <= X <= %.4f] = %f" % (k[0], k[1], calculate(k[1])-calculate(k[0])))