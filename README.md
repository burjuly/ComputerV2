# About project

Computor-v2 is an instruction interpreter that, like a shell, retrieves user inputs for advanced
computations.

This project is about making you discover or rediscover certain aspects of mathematics:
+ The complex numbers
+ The reals
+ Matrices
+ The theory of functions


# Mandatory part

+ Support for the following mathematical types:
  + Rational numbers
  + Complex numbers (with rational coefficients)
  + Matrices
  + Polynomial equations of degrees less than or equal to 2

+ Assignment of an expression to a variable by type inference
+ Reassignment of an existing variable with an expression of another type
+ Assignment of a variable to another variable (existing or not)
+ Resolution of a mathematical expression with or without defined variable (s)
+ Resolution of an equation of degree less than or equal to 2
+ Operations between types, as much as possible
+ Exit the program itself (by keyword, signal, keyboard shortcut ...)

## Rational numbers:
```
$./computorv2
> varA = 2
2
> varB = 4.242
4.242
> varC = -4.3
```

## Imaginary numbers
```
$./computorv2
> varA = 2*i + 3
3 + 2i
> varB = -4i - 4
-4 - 4i
>
```

## Functions
```
$./computorv2
> funA(x) = 2*x^5 + 4x^2 - 5*x + 4
2 * x^5 + 4 * x^2 - 5*x + 4
> funB(y) = 43 * y / (4 % 2 * y)
43 * y / (4 % 2 * y)
> funC(z) = -2 * z - 5
-2 * z - 5
>
```

Your program must be able to reassign a variable and change the type of variable by
inference in a way that:

```
$./computorv2
> x = 2
2
> y = x
2
> y = 7
7
> y = 2 * i - 4
-4 + 2i

```

It will also have to be able to reassign the result of a computation to a variable so that:
```
$./computorv2
> varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)
27
> varB = 2 * varA - 5 %4
53
> funA(x) = varA + varB * 4 - 1 / 2 + x
238.5 + x
> varC = 2 * varA - varB
1
> varD = funA(varC)
239.5
>
```

# Computational part
```
$./computorv2
> a = 2 * 4 + 4
12
> a + 2 = ?
14
>
```
It will have to manage image computation:
```
$./computorv2
> funA(x) = 2 * 4 + x
8 + x
> funB(x) = 4 -5 + (x + 2)^2 - 4
(x + 2)^2 - 5
> funC(x) = 4x + 5 - 2
4 * x + 3
> funA(2) + funB(4) = ?
41
> funC(3) = ?
15
```

```
$./computorv2
> funA(x) = x^2 + 2x + 1
x^2 + 2x + 1
> y = 0
0
> funA(x) = y ?
x^2 + 2x + 1 = 0
Une solution sur R :
-1
>
```

# Syntax part
Rational or imaginary
```
$./computorv2
> varA = 2
2
> varB= 2 * (4 + varA + 3)
18
> varC =2 * varB
36
> varD = 2 *(2 + 4 *varC -4 /3)
289.333333333
>
```

Matrices
```
$./computorv2
> matA = [[1,2];[3,2];[3,4]]
[ 1 , 2 ]
[ 3 , 2 ]
[ 3 , 4 ]
> matB= [[1,2]]
[ 1 , 2 ]
>
```
Functions
```
$./computorv2
> funA(b) = 2*b+b
2 * b + b
> funB(a) =2 * a
2 * a
> funC(y) =2* y + 4 -2 * 4+1/3
2 * y + 4 - 8 + 0.333333...
> funD(x) = 2 *x
2
```
# Bonus part

