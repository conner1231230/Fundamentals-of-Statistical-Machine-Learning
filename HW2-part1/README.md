# HW2-Part1
###  Problem 1.
Two Normal Distributions
Consider a single scalar feature 𝑥, and two classes c0, c1;
each with equal prior probability: P[c0] = P[c1] = $\frac{1}{2}$.
Thus,
$$P[c1|𝑥] = \frac{P[c1]P[x|c1]}{P[𝑥]} = \frac{P[𝑥|c1]}{2P[𝑥]} \propto P[𝑥|c1]$$
Assume the probability distribution of a feature 𝑥 depends only on the class.
In particular;$x~N(-1,0)$ for class c0, and x~N(+1, 0) for class c1.

Let 𝑅(𝑥) denote the probability of P[𝑥|c1] as a function of 𝑥,

Question:

Derive 𝑅(𝑥) and express it as:
1. the (sigmoid) logistic function. 𝑅(𝑥) = 𝜎(?).
2. Softmax (multinomial logistic function). [1 − 𝑅(𝑥), 𝑅(𝑥)] = softmax(?, ?)
Discuss how the form of 𝑅(𝑥) relates to logistic regression.

### Problem 2.
Question:

Prove the following theorem.

Theorem 1: A general property of the logistic function is:

$∀𝑎$ $\underset{b}{\text{argmax}}$ $𝑏𝜎(𝑎 + 𝑏) 𝜎(𝑎 − 𝑏) = 0$

Where 𝜎(𝑥) denotes the logistic function: 1/(1 + exp(−𝑥))

In other words if 𝑎 is a fixed constant and we are free to optimize 𝑏
to maximize: 𝜎(𝑎 + 𝑏) 𝜎(𝑎 − 𝑏), we should set 𝑏 to zero.
Prove this theorem and give an interpretation in terms of log odds ratio and probability
