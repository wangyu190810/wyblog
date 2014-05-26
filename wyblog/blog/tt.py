#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: tt.py
#Author: wangyu190810
#E-mail: wo190810401@gmail.com
#Date: 2014-05-15
#Description: 


wordlist=open('bb.txt','r')
def word():

    while True:
        aa=wordlist.readline()
        bb=len(aa)
        if not wordlist.readline():
            break

        print bb
        cc = aa[bb-8:bb]
        print ",".join(cc)
word()

