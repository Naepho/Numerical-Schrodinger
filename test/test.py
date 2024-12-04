#!/usr/bin/env python

from solver import solver

def V(x, y, z):
    return x*y*z

def main():
    sol = solver(V)

if __name__=="__main__":
    main()