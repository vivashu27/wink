from itertools import permutations
from art import *
from termcolor import colored
import requests
import bs4.element
from bs4 import BeautifulSoup
import re

def rand_char(word,infile,l): #method to generate wordlist based on user given specific characters
    with open(infile,"w") as f:
        for y in permutations(word,l):
            line="".join(y)
            f.write(line+"\n")
            
def generate_org(o,u,e,l,f,p,fl): #generating wordlist based on organisation inofrmation/osint
    spec='0123456789@#$!^&*()'
    spec1='@#$!^&*'
    store=""
    scrap=list()
    with open(fl,"w") as t:
        for i in p:
            for j in permutations(spec1,4):
                specj="".join(j)
                t.write(i.replace(" ","").rstrip()+specj+"\n")
        for j in e:
            for i in permutations(spec1,4):
                specj="".join(i)
                t.write(j.replace(" ","").rstrip()+specj+"\n")
        for i in permutations(spec,4):
            specj="".join(i)
            t.write(o+specj+"\n"+l+specj+"\n"+f+specj+"\n")
        res=requests.get(u).text
        soup=BeautifulSoup(res,"html.parser")
        for nd in soup.findAll('p'):
            cont="".join(nd.findAll(text=True))
            store=store+cont
        temp=""
        for c in store:
            if not re.findall("[\s\.:,';(){}]+",c):
                temp+=c
            else:
                if len(temp)>=4:
                    t.write(temp+"\n")
                    temp=""
                
        print(colored("[+]Generated","green"))
    

if __name__=='__main__':
    word=""
    perm=list()
    tprint("WINK","rnd-xlarge")
    #try:
    print(colored('[1] For random generated strings with given character: ','green'))
    print(colored('[2] Some information is known about the target: ','green'))
    choice=int(input('[+]Enter: '))
    if choice==1:
        l=int(input('[+]Enter the length of word: '))
        while True:
            al=str(input('[+]Enter the alphanumeric characters to be used else leave blank: '))
            num=str(input('[+]Enter the numbers from 0-9 to be used else leave blank: '))
            special=str(input('[+]Enter the special characters used else leave blank: '))
            if al==None and num==None and special==None:
                print(colored('[-]Come\'on you can\'t just generate with no characters','red'))
            else:
                word=al+num+special
                fil=str(input('[+]Enter the file to write the generated words: '))
                rand_char(word,fil,l)
                print(colored('[+]Generated','green'))
                break
    elif choice==2:
        print(colored('[1] It is an company: ','green'))
        print(colored('[2] It is a person: ','green'))
        choice1=int(input('[+]Enter: '))
        if choice1==1:
            orgname=str(input('[+]Company name For eg->Amazon: '))
            url=str(input('[+]Any webpage dedicated to company: '))
            events=str(input('[+]Any big recent event/s hosted by this company/else ignore For eg-> ctf,webinar2022,cyber awareness: '))
            location=str(input('[+]Name of the City in which it is located/else ignore: '))
            famous=str(input('[+]Any famous person associated with the company/else ignore: '))
            product=str(input('[+]Any new/future product/s they are boasting about: For eg-> mars2022,anti gravity tesla: '))
            file=str(input('[+]Enter the file to write the generated output: '))
            orgname1=orgname.replace(" ","").rstrip()
            location1=location.rstrip()
            famous1=location.replace(" ","").rstrip()
            events1=events.split(",")
            product1=product.split(",")
            generate_org(orgname1,url,events1,location1,famous1,product1,file)
                
                
    #except Exception as e:
        #print(e)
        #print('Don\'t fool around!!')
                