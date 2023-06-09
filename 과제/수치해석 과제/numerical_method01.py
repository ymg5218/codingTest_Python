# # -*- coding: utf-8 -*-
# """numerical_method01.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1N-bQZG5OA1vpc6Iq29Ogr81tW0YGXwq4

## 이분법(Bisection Method)


# from numpy import zeros, sign

# def bisection(f, a, b, n):
#   c = zeros(n)
#   for i in range(n):
#     c[i] = (a+b)/2.0
#     if sign(f(c[i])) == sign(n):
#       a = c[i]
#     else:
#       b = c[i]
#   return c

# def f(x):
#   return 2*x**3 - 3*x - 4

# a = - 2.0
# b = 3.0
# n = 7

# xb = bisection(f, a, b, n)

# print('%5s %8s' % ('k', 'c'))
# for k in range(n):
#   print('%5d %9.4f' % (k+1, xb[k]))

## 고정점 방법(Fixed Point Method)

# from numpy import zeros
# import math

# def fixedpoint(g, x0, n):
#   x = zeros(n)
#   errs = zeros(n)
#   x[0] = x0
#   for i in range(n-1):
#     x[i+1] = g(x[i])
#   return x

# def g(x):
#   return 2*x**3 - 3*x - 4

# x0 = 0.0
# n = 7
# xf = fixedpoint(g, x0, n)

# print('%5s %8s' % ('k', 'x'))
# for k in range(n):
#   print('%5d %9.4f' % (k+1, xf[k]))

# """## Newton-Rapson Method"""

# from numpy import zeros

# def newton(f, df, x0, n):
#   x = zeros(n)
#   x[0] = x0
#   for k in range(n-1):
#     x[k+1] = x[k] - f(x[k])/df(x[k])
#   return x

# def f(x):
#   return -x**2 + 6.0 * x - 5.0

# def df(x):
#   return -2.0 * x + 6.0

# x0 = -2.0
# n = 7
# xn = newton(f, df, x0, n)

# print('%5s %8s' % ('k', 'x'))
# for k in range(n):
#   print('%5d %9.4f' % (k+1, xn[k]))

# """## 할선법(Secent Method)"""

# from numpy import zeros

# from re import X
# def secent(f, x0, x1, n):
#   xs = zeros(n)
#   for k in range(n):
#     x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
#     x0 = x1
#     x1 = x2
#     xs[k] = x2
#   return xs

# def f(x):
#   return -x**2 + 6.0*x - 5.0

# x0 = -2.0
# x1 = 3.0
# n = 7

# xs = secent(f, x0, x1, n)

# print('%5s %8s' % ('k', 'x'))
# for k in range(n):
#   print('%5d %9.4f' % (k+1, xs[k]))

# """## 크래머방법(Cramer Method)"""

# from numpy import array, zeros

# from numpy.linalg import det

# def cramer(A, b):
#   n = len(b)
#   detsub = zeros((n))
#   x = zeros((n))
#   detA = det(A)
#   for i in range(n):
#     A_temp = A.copy()
#     A_temp[:,i] = b
#     detsub[i] = det(A_temp)
#     x[i] = detsub[i]/detA
#   return detsub, x

# A = array([[5, -1, 1], [-1, 3, -1], [1, -1, 4]])

# b = array([6, 2, 11])

# detsub, x = cramer(A, b)

# print('det(A) = %8.4f' % det(A))
# print('det(A1) = %8.4f' % detsub[0])
# print('det(A2) = %8.4f' % detsub[1])
# print('det(A3) = %8.4f' % detsub[2])
# print('x1 = %8.4f' % x[0])
# print('x2 = %8.4f' % x[1])
# print('x3 = %8.4f' % x[2])

# """## 가우스 소거법(Gauss Elimination Method)"""

# from numpy import array, zeros, append

# import numpy as np

# from IPython.core.interactiveshell import py3compat
# def gausselim(A, b):
#   augA = np.c_[A, b]
#   p1 = augA[1, :] - augA[0, :] * (augA[1, 0]/augA[0, 0])
#   p2 = augA[2, :] - augA[0, :] * (augA[2, 0]/augA[0, 0])
#   temp = append(augA[0, :], p1)
#   augA1 = append(temp, p2).reshape(3, 4)
#   p3 = augA1[2, :] - augA1[1, :] * (augA1[2, 1]/augA1[1, 1])
#   augA2 = augA1.copy()
#   augA2[2] = p3
#   A = augA2[:, 0:3]
#   b = augA2[:, -1]
#   print('A = ', A)
#   print('b = ', b)
#   x = zeros((3))
#   x[2] = b[2]/A[2, 2]
#   x[1] = (b[1] - A[1, 2] * x[2])/A[1, 1]
#   x[0] = (b[0] - A[0, 2] * x[2] - A[0, 1] * x[1])/A[0, 0]
#   return x

# A = array([[5, -1, 1], [-1, 3, -1], [1, -1, 4]])

# b = array([6, 2, 11])

# xg = gausselim(A, b)

# print('x1 = %8.4f' % xg[0])
# print('x2 = %8.4f' % xg[1])
# print('x3 = %8.4f' % xg[2])

# """## LU 분해법(LU Decomposition)"""

# from numpy import array, sqrt, zeros, set_printoptions

# def LUdecom(A, b):
#   # Lower triangular matrix
#   el = zeros((3, 3))
#   el[0, 0] = sqrt(A[0, 0])
#   el[1, 0] = A[1, 0]/el[0, 0]
#   el[1, 1] = sqrt(A[1, 1] - el[1, 0]**2)
#   el[2, 0] = A[2, 0]/el[0, 0]
#   el[2, 1] = (A[2, 1] - el[2, 0] * el[1, 0])/el[1, 1]
#   el[2, 2] = sqrt(A[2, 2] - el[2, 0]**2 - el[2, 1]**2)
#   # Forward substitution for y
#   y = zeros((3))
#   y[0] = b[0]/el[0, 0]
#   y[1] = (b[1] - el[1, 0] * y[0])/el[1, 1]
#   y[2] = (b[2] - el[2, 0] * y[0] - el[2, 1] * y[1])/el[2, 2]
#   # Backward substitution for x
#   x = zeros((3))
#   elT = el.T
#   x[2] = y[2]/elT[2, 2]
#   x[1] = (y[1] - elT[1, 2] * x[2])/elT[1, 1]
#   x[0] = (y[0] - elT[0, 1] * x[1] - elT[0, 2] * x[2])/elT[0, 0]
#   return el, y, x

# A = array([[5, -1, 1], [-1, 3, -1], [1, -1, 4]])

# b = array([6, 2, 11])

# el, y, xc = LUdecom(A, b)

# set_printoptions(precision = 4)

# print('L = ', el)
# print('y = ', y)
# print('x1 = %8.4f' % xc[0])
# print('x2 = %8.4f' % xc[1])
# print('x3 = %8.4f' % xc[2])

# #EOF

