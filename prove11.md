# CSE 280 Prove 11

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Spencer Damiano

**Section**: CSE 280 02

**Teacher**: Macbeth

## Question 1 (9 points)

Find the $gcd$ for each of the following by hand using Eulid's Algorithm  Show your work in the tables below.  The first one is done for you.  Add more rows to each table as needed.  You can check your work with a calculator.

**Problem A**: $gcd(43,57)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|43|57|14|
|57|14|1|
|14|1|0|

Answer: 1

**Problem B**: $gcd(39,501)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|39|501|33|
|501|33|6|
|6|3|0|

Answer: 3

**Problem C**: $gcd(110,765)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|765|110|105|
|110|105|5|
|105|5|0|

Answer: 5

**Problem D**: $gcd(493,899)$

|$x$|$y$|$r = y \mod x$|
|:-:|:-:|:-:|
|899|493|406|
|493|406|87|
|406|87|58|
|87|58|29|
|58|29|0|

Answer: 29

## Question 2 (10 points)

Find the $gcd$ for the first three problems from Question 1 using the Extended Eulcid Algorithm to express the answer as a linear combination.  The first one is done for you.

|Problem|$gcd = s*x + t*y$|
|:-:|:-:|
|$gcd(43,57)$|$1 = 4*43 - 3*57$|
|$gcd(39,501)$|$3 = -77(39) + 6(501)$|
|$gcd(110,765)$|5 = 7(110) - 1(765)$|


## Question 3 (8 points)

Find the multiplicative inverse for $x \text{ mod } n$ in the table below.  These numbers are smaller so you don't need to use the Extended Euclidean Algorithm to solve.  You can check your answers by verifying that $sx \text{ mod } n = 1$ where $s$ is the multiplicative inverse you calculated.

| $x$ | $n$ | Multiplicative Inverse |
|:---:|:---:|:----------------------:|
|  2  |  7  |           4            |
|  5  | 11  |           9            |
|  7  | 20  |           3            |
|  3  | 13  |           9            |

## Question 4 (9 points)
Use the Extended Euclidean Algorithm to find the multiplicative inverse of $83 \text{ mod } 96$.  You can check your answer by verifying that $s*83 \text{ mod } 96 = 1$ where $s$ is the multiplicative inverse you calculated.  

In your answer, provide both the linear combination of $1 = s*83 + t*96$ and the multiplicative inverse derived from it.

Answers:
* $s = -37$
* $t = 32$
* Multiplicative Inverse = 59

## Question 5 (14 points)

### Part 1

Create public and private RSA keys by using the two prime number $p = 137$ and $q = 211$. Calculate $N$ and $\phi$.  Select a value of $e$ such that $gcd(e,\phi)=1$.  Find the multiplicative inverse for $e \text{ mod } \phi$ (called $d$).  You can use the following code to find the value of $d$.  This code implements the Extended Eculidean Algorithm and provides the GCD and the linear combination for the GCD.  If `x` and `y` are provided to the function, it will return a tuple `(r,s,t)` where `r` is the GCD and $r = s*x + t*y$.

```python
def gcd_ext(x,y):

    (old_r, r) = (x, y)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    while r != 0:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)
    return (old_r, old_s, old_t)
```

Answers:
* $p = 137$
* $q = 211$
* $N = 28907$
* $\phi = 28560$
* $e = 65537$
* $d = 3953$

### Part 2

The values of $N$ and $e$ are the public keys.  The value of $d$ is the private key.  Complete the python code below to encrypt the value $m = 5645$ and then decrypt it again. 

```python
# Put your values from Part 1
p = 137
q = 211
e = 65537
N = 28907
phi = 28560
d = 3953

# Message to be encrypted
m = 5645

# Encrypt the message
c = pow(m, e, N)  # Encrypted message
print(f"Encrypted message: {c}")

# Decrypt the message
decrypted_m = pow(c, d, N)  # Decrypted message, should be equal to m
print(f"Decrypted message: {decrypted_m}")
```

  
