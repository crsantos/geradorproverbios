#!/usr/bin/env python
# encoding: utf-8
"""
proverbios.py

Created by Carlos Ricardo on 2011-07-17.
Copyright (c) 2011 . All rights reserved.
"""

def main():
    
    first_sentence= " debaixo dos lençóis,"
    second_sentence=" entre as pernas."
    f=open('lista_proverbios.txt')
    
    for p in f.readlines():
        print p.split(',')[0].decode('utf-8')+ first_sentence.decode('utf-8')+p.split(',')[1].decode('utf-8')+second_sentence.decode('utf-8')+"\n"
    
if __name__ == '__main__':
    main()
