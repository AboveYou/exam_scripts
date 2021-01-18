# Wahrscheinlichkeitstheorie

Some scripts that might be helpful in the exam.

## [distribution.py](./distribution.py)

1.  transform into Standartnormalverteilung
2.  perform a lookup in the table

Meant for a task like:  

![task1](doc/task1.png)

**Output:**

- for every value  
    - Pr[X <= k]  
    - Pr[X >= k]
- for k[0] and k[1]
    - Pr[k[0] <= X <= k[1]]


## [exp_var.py](./exp_var.py)

Calculates the Exp[X] - Erwartungswert and the Var[X] - Varianz.

Meant for a task like:

![task2](doc/task2.png)

**Output:**

- Exp[X]
- Exp[X^2]
- Var[X] 