#!/usr/bin/env python3
#-*- coding:utf-8 -*-

"""
# uso
$ mytrade 15.12 -queda 0.93
$ mytrade 20.8 12.34 45.2 -queda 2.0
$ mytrade 20.8 12.34 45.2 -queda 3.2

"""
import argparse
from decimal import Decimal


def queda(porcentagem, lst_acoes):
    porcentagem = Decimal(str(porcentagem))/Decimal('100.0')
    for i in lst_acoes:
        ni = Decimal(str(i))
        yield (ni-(ni*porcentagem))

def alta(porcentagem, lst_acoes):
    porcentagem = Decimal(str(porcentagem))/Decimal('100.0')
    for i in lst_acoes:
        ni = Decimal(str(i))
        yield (ni+(ni*porcentagem))


def printer(lst):
    # lst eh um interator de Decimal objets
    # e o metodo de format com float funciona do mesmo geito para Decimal
    for i in lst:
        print('{:.2f}'.format(i), end=' ')

def test():
    v = queda(0.7, [47.38])
    v = next(v)
    assert '47.05' == '{:.2f}'.format(v)

def main():
    parser = argparse.ArgumentParser(description='Cálculo porcentagem')
    
    parser.add_argument('acoes', metavar='valor', type=float, nargs='+',
                       help='valor das ações (73. 29.1 ... )')
    parser.add_argument('-queda', '--queda', type=float,
                       help='passa o valor da queda (ex. 3.0)')
    
    parser.add_argument('-alta', '--alta', type=float,
                        help='passa o valor da alta (ex. 6.7)')

    args = parser.parse_args()
    acoes = args.acoes
    if args.alta:
        valor = args.alta
        printer(alta(valor, acoes))
        
    elif args.queda:
        valor = args.queda
        printer(queda(valor, acoes))
    print()

if __name__ == '__main__':
    main()
