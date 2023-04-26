from time import sleep
from random import choice, randint

minichars=list("""!'^+%&/("=?_-*|\}.:,;][{$#£><""")
vowels=list("EeIıOoİiÖöAaUuÜü")
text="pepared with python version 3.11\n" \
     "Using from library random and time.sleep modules\n" \
     " M   date:       \n" \
     " E   24.04.2023  \n" \
     " F   Pepared for \n" \
     " A   akakademi   \n" \
     " M   licence     \n" \
     " E               \n" \
     " X PRODUCT ...   \n" \
     "\n."
for q in list(text):
    print(q,end="",flush=True)
    sleep(0.03)
class create_nickName:
    def __init__(self, Min:int= 5, Liste:list=list):
        """
        :type Liste: list of words
        :type Min: int for minimum words length
        """
        if type(Liste) != list: raise TypeError("Liste must to be a word list")
        print("This py is preparing a nickname with your words\n.")
        sleep(1)
        while True:
            a=input(".\nset minimum count of character:")
            try:a=int(a)
            except:
                print("please type just integer")
                continue
            if a<=0 or a>250:
                print("please type acceptable integer")
                continue
            Min=a+0
            break
        sleep(0.2)
        print(".\n.\n.\nif you would like add words or numbers to list write it and press enter\n"
              "for each words. else or to run out just press enter idly.\n.\n.")
        innput=" "
        sleep(0.5)
        while True:
            innput=input("Would you want to add word to the list (count= "+str(len(Liste))+"):")
            if innput=="":
                if len(Liste)==0:print("WHAT YOU WANTT!!!...\n")
                else :
                    print("quitting adding...")
                    break
            else: Liste.append(innput)
        print("Starting randomize this",len(Liste),"words...")
        self.Liste,self.Numbers=[],[]
        for q in Liste:
            try: self.Numbers.append(int(q) )
            except: self.Liste.append(q)
        self.minichars=minichars
        self.text=[]   # the result
        defs=[self.first_char,self.just_consonant, self.add_word, self.add_word, self.add_number,self.add_minichar]  # defs for randomize words
        ##################################  ORGANIZED DATAS

        while True:
            self.text = []
            sira=[randint(0,defs.__len__()-1)]
            for q in range(100):
                c = randint(0,defs.__len__()-1)
                if c!=sira[-1]: sira.append(c)
            for q in sira:
                if len("".join(self.text))> Min:break
                self.text.append(str(defs[q]()))
            self.text="".join(self.text)
            print(self.text,flush=True)
            sleep(0.5)

    def first_char(self):
        a=randint(1,2)
        if a==1:   return choice(self.Liste)[0].lower()
        elif a==2: return choice(self.Liste)[0].upper()
        else: print("first_char unexpected random")
    def just_consonant(self):
        a = randint(1, 3)
        if a==1:   return "".join([ (q if q not in vowels else "") for q in choice(self.Liste) ]).lower()
        elif a==2: return "".join([(q if q not in vowels else "") for q in choice(self.Liste)]).title()
        elif a==3: return "".join([(q if q not in vowels else "") for q in choice(self.Liste)]).upper()
        else: print("Just_consonant unexpected random")

    def add_word(self):
        a = randint(1, 2)
        if a==1:   return choice(self.Liste).lower()
        elif a==2: return choice(self.Liste).title()
        elif a==3: return choice(self.Liste).upper()
        else: print("add_word unexpected random")
    def add_number(self): return choice(self.Numbers)
    def add_minichar(self): return choice(self.minichars)

words=[] # if you want to enter words before starting
create_nickName(Min=8, Liste=words)
