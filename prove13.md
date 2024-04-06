# CSE 280 Prove 13

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Spencer Damiano

**Section**: 208 02

**Teacher**: Macbeth

## Question 1

Ruth and Ed flip a coin to decide who will do the chores.  Whomever gets Tails has to clean the bathroom.  One day Ed complains that he loses too often.  So Ruth said, "OK, this time you flip two coins and I will flip one coin.  If you get more heads than I do, then I'll clean the bathroom.  Ed likes Ruth's display of generosity and says, "You're on!"  What is the probability that Ed will get more heads and thus not have to clean the bathroom.  Round your answer to the nearest hundreth.

Answer: .25 is the probability that you'll get two heads which would be the only way to get more heads then ruth. you have a 50% chance of having one heads and a 25% chance of having only tails. This is a bad deal for Ed

## Question 2
What is the probability of rolling the following scenarios given two fair 6 sided dice?  Round your answer to the nearest hundreth.

|Scenario|Probability|
|:-:|:-:|
|Rolling a sum of 7|0.17|
|Rolling two odd numbers|0.25|
|Rolling a sum at most 10|0.92|

## Question 3
A computer generates a random four-character string using the uppercase letters `A, B, C, ..., Z` with duplication allowed.  What is the probability that the random string contains no vowels `A, E, I, O, U`?  Round your answer to the nearest hundreth.

Answer: $\frac{21^4}{26^4}$ = .43

## Question 4
In a class of 11 boys and 9 girls, the teacher selects three students at random to write problems on the board.  What is the probability that all the students selected were girls?  Round your answer to the nearest hundreth.

Answer: $\frac{9}{20} * \frac{8}{19} * \frac{7}{18} = 0.07$

## Question 5
An urn contains five red balls and seven blue balls.  Four balls are drawn at random without replacement.  

**Part A**
What is the probability (to the nearest hundreth) that all four balls are red?

Answer: $\frac{5}{12} * \frac{4}{11} * \frac{3}{10} * \frac{2}{9} = 0.01$

**Part B**
What is the probability (to the nearest hundreth) that two of the balls are red and two are blue?

Answer: $\frac{c(5,2)}{c(7,2)} = 0.42$

## Question 6
Assume a pin number is 5 digits long consisting of digits 0 through 9.

**Part A**
How many pin numbers are there with no duplication of digits?

Answer: 30

**Part B**
How man pin numbers are there with duplication of digits?

Answer: 69,720

**Part C**
How many pin numbers are there that contain exactly 3 zeros with duplication of digits allowed?

Answer: 810

## Question 7
Student data shows that 80% of all students passed CSE 999.  Furthermore, 90% of all passing students missed no more than 2 days of class.  By contrast, 30% of non-passing students missed no more than 2 days of class.  What is the probability that a randomly chosen stundent passes CSE 999, given that they missed no more than 2 days of class?  Use Bayes Theorem to solve.

Answer: 0.92


