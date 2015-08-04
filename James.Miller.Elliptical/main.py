###############################################
# Name: James Miller
# Class: CMPS 4663 Cryptography
# Date: 2 August 2015
# Program 3 - Elliptical Points
###############################################
import argparse
import sys
from Elliptical import Elliptical

def main():
    parser = argparse.ArgumentParser()
    #Minor change to automatically allow for the coords to be floating points.
    parser.add_argument("-a", type=float, dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", type=float,dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",type=float,dest="x1", help="")
    parser.add_argument("-y1",type=float,dest="y1", help="")
    parser.add_argument("-x2",type=float,dest="x2", help="")
    parser.add_argument("-y2",type=float,dest="y2", help="")

    args = parser.parse_args()

    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)

    Ell = Elliptical(args.x1,args.x2,args.y1,args.y2,args.a,args.b)
    slope = Ell.getslope(Ell.x1,Ell.x2,Ell.y1,Ell.y2)
    xr,yr = Ell.getPoints(slope,Ell.x1,Ell.x2,Ell.y2)
    curve = Ell.curve(Ell.x1,Ell.x2,Ell.y1,Ell.y2,xr,yr,slope,Ell.a,Ell.b)

if __name__ == '__main__':
    main()
