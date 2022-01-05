from itertools import permutations
from art import *
from termcolor import colored
import os


def rand_char(word,infile,l):
    with open(infile,"w") as f:
        for y in permutations(word,l):
            line="".join(y)
            f.write(line+"\n")
            


if __name__=='__main__':
    word=""
    perm=list()
    tprint("WINK","rnd-xlarge")
    try:
        print(colored('[1] For random generated strings with given character: ','green'))
        print(colored('[2] Some information is known about the target: ','green'))
        choice=int(input('[+]Enter: '))
        if choice==1:
            l=int(input('[+]Enter the length of word: '))
            while True:
                al=str(input('[+]Enter the alphanumeric characters else leave blank: '))
                num=str(input('[+]Enter the numbers from 0-9 to be used else leave blank: '))
                special=str(input('[+]Enter the special characters used else leave blank: '))
                if al==None and num==None and special==None:
                    print(colored('[-]Come\'on you can\'t just generate with no characters','red'))
                else:
                    word=al+num+special
                    print(word)
                    fil=str(input('[+]Enter the file to write the generated words: '))
                    rand_char(word,fil,l)
                    print(colored('[+]Generated','green'))
                    break
                
    except Exception as e:
        print('Don\'t fuck around!!')
                
