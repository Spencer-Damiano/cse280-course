# CSE 280 Prove 02

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Spencer Damiano

**Section**:

**Teacher**: Bro MacBeth

## Question 1 (7 points)

Complete the following truth table to show that $A \equiv B$ (logically equivalent) where

$A : p \to \neg (q \land r)$

$B : \neg (p \land q \land r)$

|$p$|$q$|$r$|$q \land r$|$\neg (q \land r)$|$A: p \to \neg (q \land r)$|$p \land q \land r$|$B: \neg (p \land q \land r)$|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|T|T|T|T|F|F|T|F|
|T|T|F|F|T|T|F|T|
|T|F|T|T|F|F|F|T|
|T|F|F|F|T|T|F|T|
|F|T|T|F|T|T|F|T|
|F|T|F|F|T|T|F|T|
|F|F|T|F|T|T|F|T|
|F|F|F|F|T|T|F|T|

## Question 2 (8 points)

Using the following predicates where the domain of $x$ is the set of all people:

$P(x) = x \text{ is older than 21}$

$S(x) = x \text{ is a student}$

express the following propositions in English senteneces (the first two are done for you):

|Proposition|English Sentence|
|-|-|
|$\exists x \ P(x)$|There exists a person who is older than 21.|
|$\forall x \ P(x)$|All people are older than 21.|
|$\exists x \ \neg P(x)$|There exists a person whi is not older than 21|
|$\forall x \ \neg P(x)$|All people are not older than 21|
|$\exists x \ S(x)$|There ists person who is a student|
|$\forall x \ S(x)$|All people are students|
|$\neg \exists x \ S(x)$|There does not exist a person who is a student|
|$\exists x \ \neg S(x)$|Ther are some people who are not a student|
|$\neg \forall x \ \neg S(x)$|There are no people who are not a student|
|$\forall x \ \neg S(x)$|All people are not a student|

## Question 3 (6 points)

Using the following predicates where the domain of $x$ is the set of all people:

$F(x) = x \text{ is my friend}$

$C(x) = x \text{ is cool}$

$S(x) = x \text{ is a student}$

$N(x) = x \text{ is from Nepal}$

identify which of the following english sentences match to each proposition (the first one is done for you).  Each sentence matches to one of the propositions in the table.

* All people are both students and from Nepal.
* All of my friends are cool.
* Someone is my friend or cool (maybe even both).
* Some student is from Nepal.
* Someone is my friend and is cool.
* All students are from Nepal.
* Everyone is a friend and is cool.

|Proposition|English Sentence|
|-|-|
|$\forall x \ (F(x) \to C(x))$|All of my friends are cool.|
|$\exists x \ (F(x) \land C(x))$|Some people are my friends and are cool|
|$\forall x \ (F(x) \land C(x))$|All people are my friends and are cool|
|$\exists x \ (F(x) \lor C(x))$|Some people are my friends or they are cool|
|$\forall x \ (S(x) \to N(x))$|Every one who is a student is form Nepal|
|$\forall x \ (S(x) \land N(x))$|All people are a student and from Nepal|
|$\exists x \ (S(x) \land N(x))$|Some people are students and form Nepal|

## Question 4 (8 points)

Evaluate the following propositions to be True or False given that the domain of $x$ is the following integers: $\lbrace -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 \rbrace$:

|Proposition|True or False|
|-|-|
|$\forall x \ (x \text{ is odd})$|F|
|$\exists x \ (x \text{ is odd})$|T|
|$\forall x \ (x \text{ is negative})$|F|
|$\exists x \ (x \text{ is negative})$|T|
|$\forall x \ (x^2 \ge 0)$|T|
|$\exists x \ (x^2 \ge 0)$|T|
|$\exists x \ (x + x = 1)$|F|
|$\exists x \ (x + 2 = 1)$|T|

## Question 5 (10 points)

Negate each of the following logical statements by adding a negation symbol $\neg$, then apply De Morgan's Laws one or more times to move the $\neg$ as far to the right as possible. The first one is done for you.

|Predicate|$\neg$ Predicate|
|:-:|:-:|
|$\forall x \forall y \ P(x,y)$|$\exists x \exists y \ \neg P(x,y)$|
|$\exists x \forall y \ P(x,y)$|$\forall x \exists y \neg P(x,y)$|
|$\exists x \exists y \forall z \ \neg P(x,y,z)$|$\forall x \forall y \exists z P(x,y,x) $|
|$\forall x \exists y \forall z \ P(x,y,z)$|$\exists x \forall y \exists z \neg P(x,y,z)$|
|$\exists x \exists y \ (P(x,y) \land Q(x,y))$|$\forall x \forall y (\neg P(x,y) \lor \neg Q(x,y))$|
|$\forall x \forall y \exists z \ (P(x,y) \to Q(y,z))$|$ \exists x \exists y \forall z(P(x,y) \land \neg Q(y,z))$|

## Question 6 (11 points)

The following code provides several predicates (`is_even`, `is_natural`, and `is_palindrome`).  There are multiple test cases that will determine whether the quantifier proposition is True or False given the specified domain.  You need to implement the `forall` and `exists` functions.  Hint: You will need to loop through all the items in the `domain` (which is a list) and use the `predicate` (which is a function) to test all or some of the values in the `domain`.

```python
def is_even(x):
    return x % 2 == 0

def is_natural(x):
    return x > 0

def is_palindrome(x):
    return x == x[::-1]

def in_unit_circle(point):
    return (point[0]**2 + point[1]**2) <= 1

def forall(predicate, domain):
    #print(f"\u2200x ({predicate.__name__}) domain={domain}") # this would cause the code not to run, commented it out
    # Add your code here to return True or False
    for x in domain:
        if not predicate(x):
            return False      
    return True

def exists(predicate, domain):
    #print(f"\u2203x ({predicate.__name__}) domain={domain}") # this would cause the code not to run, commented it out
    # Add your code here to return True or False
    for x in domain:
        if predicate(x):
            return True
        if type(x)== None: # this was added due to bug in Words 3
            return False 
    return False

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_even,numbers1)) # False
print(exists(is_even,numbers1)) # True
print("================================")
print(forall(is_natural,numbers1)) # True
print(exists(is_natural,numbers1)) # True
print("================================")

numbers2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(forall(is_natural,numbers2)) # False
print(exists(is_natural,numbers2)) # True

print("================================")
words1 = ['civic', 'rotor', 'apple']
print(forall(is_palindrome,words1)) # False
print(exists(is_palindrome,words1)) # True
print("================================")

words2 = ['racecar', 'madam', '123454321']
print(forall(is_palindrome,words2)) # True
print(exists(is_palindrome,words2)) # True
print("================================")

words3 = ['no', 'palindromes', 'here']
print(forall(is_palindrome,words3)) # False
print(exists(is_palindrome,words3)) # False
print("================================")

points1 = [(0.5,0.5), (-1,0), (-0.75,-0.3)]
print(forall(in_unit_circle,points1)) # True
print(exists(in_unit_circle,points1)) # True
print("================================")

points2 = [(0.25,-1), (0.9,1.1), (0.1,-0.1)]
print(forall(in_unit_circle,points2)) # False
print(exists(in_unit_circle,points2)) # True
```