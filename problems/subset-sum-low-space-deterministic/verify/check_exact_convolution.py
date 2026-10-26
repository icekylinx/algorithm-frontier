#!/usr/bin/env python3
"""Exact fixed-point FFT reference and finite independent convolution checks.

No floating-point or transcendental-library function is used.  The
arbitrary-length error and bit-cost proof is in ../convolution.md.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def nearest(numerator: int, denominator: int) -> int:
    """Nearest integer, with exact ties rounded upward."""
    if denominator <= 0:
        raise ValueError('positive rounding denominator required')
    return (2*numerator+denominator)//(2*denominator)


def roots(length: int, precision: int) -> list[tuple[int,int]]:
    def atan(q: int) -> F:
        return sum((F((-1)**j,(2*j+1)*q**(2*j+1))
                    for j in range(precision)),F(0))
    pi = 16*atan(5)-4*atan(239)
    work = 1 << (precision+16)
    result = []
    for j in range(length//2):
        theta = 2*pi*j/length
        re,im = work,0
        for k in range(8*precision,0,-1):
            re,im = (work+nearest(-theta.numerator*im,theta.denominator*k),
                     nearest(theta.numerator*re,theta.denominator*k))
        result.append((nearest(re,1 << 16),nearest(im,1 << 16)))
    return result


def multiply(a: tuple[int,int],b: tuple[int,int],scale: int) -> tuple[int,int]:
    ar,ai = a
    br,bi = b
    return nearest(ar*br-ai*bi,scale),nearest(ar*bi+ai*br,scale)


def transform(values: list[tuple[int,int]],twiddles: list[tuple[int,int]],
              scale: int,inverse: bool = False) -> None:
    length = len(values)
    bits = length.bit_length()-1
    for i in range(length):
        reverse = int(f'{i:0{bits}b}'[::-1],2)
        if reverse > i:
            values[i],values[reverse] = values[reverse],values[i]
    width = 2
    while width <= length:
        stride = length//width
        for start in range(0,length,width):
            for j in range(width//2):
                root = twiddles[j*stride]
                if inverse:
                    root = root[0],-root[1]
                lo = values[start+j]
                hi = multiply(values[start+j+width//2],root,scale)
                values[start+j] = lo[0]+hi[0],lo[1]+hi[1]
                values[start+j+width//2] = lo[0]-hi[0],lo[1]-hi[1]
        width *= 2


def convolve(a: tuple[int,...],b: tuple[int,...],prepared=None) -> tuple[int,...]:
    if not a or not b:
        return ()
    if any(x not in (0,1) for x in a+b):
        raise ValueError('Boolean input required')
    length = 1 << (2*max(len(a),len(b))-1).bit_length()
    precision = 16+6*(length.bit_length()-1)
    scale = 1 << precision
    twiddles = roots(length,precision) if prepared is None else prepared
    left = [(x*scale,0) for x in a]+[(0,0)]*(length-len(a))
    right = [(x*scale,0) for x in b]+[(0,0)]*(length-len(b))
    transform(left,twiddles,scale)
    transform(right,twiddles,scale)
    for i in range(length):
        left[i] = multiply(left[i],right[i],scale)
    transform(left,twiddles,scale,inverse=True)
    if any(4*abs(im) >= scale*length for _,im in left):
        raise AssertionError('inverse imaginary remainder below one quarter')
    return tuple(nearest(re,scale*length) for re,_ in left[:len(a)+len(b)-1])


def verify() -> dict:
    prepared = {}
    counts = {'convolutions':0,'coefficients':0,'transform_lengths':0}
    cases = []
    for size in range(1,5):
        arrays = list(product((0,1),repeat=size))
        cases.extend(product(arrays,arrays))
    for size in (5,6,7,8,15,16,17,31,32):
        arrays = [tuple([0]*size),tuple([1]*size),tuple(i%2 for i in range(size)),
                  tuple(int(i in (0,size-1)) for i in range(size))]
        cases.extend(product(arrays,arrays))
    cases += [((1,),(1,0,1)),((0,1),(1,1,1,0,1)),((),(1,)),((1,),())]
    for a,b in cases:
        if a and b:
            length = 1 << (2*max(len(a),len(b))-1).bit_length()
            if length not in prepared:
                precision = 16+6*(length.bit_length()-1)
                prepared[length] = roots(length,precision)
            observed = convolve(a,b,prepared[length])
            expected = tuple(sum(a[i]*b[k-i] for i in range(len(a))
                                 if 0 <= k-i < len(b))
                             for k in range(len(a)+len(b)-1))
        else:
            observed,expected = convolve(a,b),()
        if observed != expected:
            raise AssertionError(f'exact coefficient mismatch for {a!r}, {b!r}')
        counts['convolutions'] += 1
        counts['coefficients'] += len(expected)
    counts['transform_lengths'] = len(prepared)
    return {'status':'PASS','checks':counts,
            'scope':'Exact fixed-point radix-two FFT with rationally constructed roots, compared with independent integer coefficient summation. Arbitrary-length error and resource bounds are mathematical lemmas, not inferred from these finite cases.'}


def main() -> None:
    if not __debug__:
        raise SystemExit('Run with assertions enabled (without -O or PYTHONOPTIMIZE).')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    receipt = verify()
    if args.output:
        args.output.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':
    main()
