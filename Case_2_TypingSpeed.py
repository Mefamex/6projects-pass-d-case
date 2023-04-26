# -*- coding:utf-8 -*-
from time import sleep, time
from random import randint
import msvcrt
from os import system
import threading
def printt(*args,end="\n"):
    textt,slep="".join([str(q) for q in args[:-1]]),args[-1]
    for qq in textt:
        print(qq,flush=True,end="")
        sleep(slep)
    print(end=end,flush=True)
text="\n M   date:       \n" \
     " E   25.04.2023  \n" \
     " F   Pepared for \n" \
     " A   altinkariyer\n" \
     " M   akaeskisehir\n" \
     " E   licence     \n" \
     " X               \n" \
     " PRODUCT ...     \n" \
     "          .      \n" \
     "          .      \n" \
     "          .      \n" \
     "\npepared with python version 3.11\n" \
     "Using modules from library: \n" \
     "---> msvcrt        (for listening keyboard)\n" \
     "---> random.randint\n" \
     "---> threading\n" \
     "---> time.sleep, time  \n\n" \
     "Now we will test your sentence typing speed\n" \
     "No difficulty level.\n.\n"
printt(text,0.03)

minichars=list("""!'^+%&/("=?_- *|\};.,:][{$#£><""")


class create_nickName:
    global printt
    def __init__(self, Liste:list=list):
        """
        :type Liste: list of words
        """
        self.Liste=Liste
        printt("Now we will test your keyboard typing speed\nPressing the spacebar moves to the next word.",
               "\nNo difficulty level but...",0.01)
        printt("I checking the list of sentences. | \b\b/ \b\b- \b\b\ \b\b| \b\b/ \b\b- \b\b\ \b\b| \b\b/ \b\b- "
               "\b\b\ \b\b| \b\b/ \b\b- \b\b\ \b\b| \b\b/ \b\b- \b\b\ \b\b",0.01)
        printt("...............\r",0.1)
        self.add_typed=""
        self.Liste="".join(self.Liste)
        for minis in minichars:self.Liste=self.Liste.replace(minis," ")
        self.Liste=self.Liste.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")
        printt("We have ",len(self.Liste)," words and average letters of words is ",
               str(len("".join(self.Liste))/len(self.Liste))[:5],0.02)
        while True:
            while True:
                try:
                    self.Length=int(input("How long do you want a sentence (1 - "+str(len(self.Liste)-2)+"):"))
                except:
                    print("please just integer for Length.\n.")
                    continue
                if self.Length<=0 or self.Length >len(self.Liste)-2:
                    print("please set Length between 1 and 100...\n.")
                else:break
            print("Length of sentences set ",self.Length," words.\nLets start!")
            self.startt()

    def startt(self):
        print("press enter when you ready\r",flush=True,end="")
        input()
        print("\nA sentence for you for testing your writing test is:\n  ",end="",flush=True)
        starting_with=randint(0,len(self.Liste)-(self.Length+1))
        sentence=self.Liste[ starting_with : starting_with+self.Length ]
        printt(" ".join(sentence),0.1/self.Length)
        sleep(2)
        print("starting...")
        printt("3, 2, 1 :",0.333)
        self.Write_check(sentence)

    def check_input(self): self.add_typed=msvcrt.getwch()

    def Write_check(self,textt):
        pressed,word_trues,word_false,typed,self.add_typed,b,start_t=0,0,0,"","","",time()
        t1 = threading.Thread(target=self.check_input, name='t1')
        t1.start()
        for q in textt:
            system("cls")
            print(" ".join([ "[ "+qq+" ]" if qq == q else qq for qq in textt ]))
            while True:
                if int((time()-start_t)*4)%2==0:b="_"
                else:b=" "
                print(" {:<6} - {} - {}        \r ".format(str(time()-start_t)[:6],q,typed+b),flush=True,end="")
                if not t1.is_alive():
                    t1 = threading.Thread(target=self.check_input, name='t1')
                    t1.start()
                if self.add_typed == " ":
                    typed=typed.replace(" ","")
                    if typed==q:word_trues+=1
                    else:word_false+=1
                    typed,self.add_typed="",""
                    break
                elif len(self.add_typed) != 0:
                    if self.add_typed=='\x08':typed=typed[:-1]
                    elif self.add_typed=='\r':pass
                    else:
                        typed+=self.add_typed
                        pressed+=1
                    self.add_typed = ""
                else:sleep(0.054321)
        printt("                                                              \nTrue words: ",
               word_trues,"\nFalse words: ",word_false,"\nword accuracy: ",str(100*word_trues/len(textt))[:6],
               "\nseconds per words: ",str((time()-start_t)/len(textt))[:6] ,"\nstroke count: ", pressed,"\nin time: ",
               str(time()-start_t)[:6],"\nstroke per second: ",str(pressed/(time()-start_t))[:6],"\nstroke accuracy: %",
               str(100*len("".join(textt))/pressed)[:6],0.02)
        del t1
        input("\n press enter to new challenge")
        system("cls")

                
giving_sentence=['Yazılım değişik ve çeşitli görevler yapma amaçlı tasarlanmış elektronik aygıtların birbirleriyle '
                 'haberleşebilmesini ve uyumunu sağlayarak görevlerini ya da kullanılabilirliklerini geliştirmeye '
                 'yarayan makine komutlarıdır.Yazılım, elektronik aygıtların belirli bir işi yapmasını sağlayan '
                 'programların tümüne verilen isimdir. Bir başka deyişle, var olan bir problemi çözmek amacıyla '
                 'bilgisayar dili kullanılarak oluşturulmuş anlamlı anlatımlar bütünüdür. Yazılım için çeşitli '
                 'diller mevcuttur. Bilgisayarın kendisinin işletilmesini sağlayan, işletim sistemi, derleyiciler, '
                 'çeşitli donatılar gibi yazılımlardır.Çekirdek işletim sisteminin en temel parçasıdır. Burada '
                 'çekirdek ile ilgili farklı yaklaşımlar olduğunu yani yazılım karar verme ve Programlama paradigması '
                 'mevcut olsa da bir işletim sistemi çekirdeğinin esas görevi Bilgisayar Donanımı ile kullanıcıya ve '
                 'kullanıcıya yazılım veya donanım üreten üreticilere Arayüz oluşturmak ve kaynakların yönetilmesi ile'
                 ' ilgili birimleri idare etmektir. Bu kullanıcıların işlerine çözüm sağlayan örneğin çek, senet, stok'
                 ' kontrol, bordro, kütüphane kayıtlarını tutan programlar, bankalardaki müşterilerin para hesaplarını '
                 'tutan programlar gibi yazılımlardır.Bütün sistem programları içinde en temel yazılım işletim '
                 'sistemidir ki, bilgisayarın bütün donanım ve yazılım kaynaklarını kontrol ettiği gibi, kullanıcılara'
                 ' ait uygulama yazılımlarının da çalıştırılmalarını ve denetlenmelerini sağlar.Sistem yazılımı '
                 'çeşitli bağımsız donanım bileşenlerinin uyum içinde çalışmalarından sorumludur.Sistem yazılımı '
                 'bilgisayar donanımının işletilmesi ve uygulama yazılımının çalıştırılması için bir platform sağlamak'
                 ' için tasarlanmış bir bilgisayar yazılımıdır.En temel sistem yazılımı türleri şunlardır. Bilgisayar '
                 'BIOSu ve aygıt yazılımı.. Bilgisayara bağlı veya bilgisayar içindeki donanımı çalıştırmak ve kontrol '
                 'etmek için gereken temel işlevselliği sağlar.İşletim sistemi .. Bilgisayar parçalarının hafıza ile'
                 ' diskler arasında veri alışverişi veya monitöre görüntü sağlamak gibi görevleri uygulayarak birlikte '
                 'çalışmasına olanak sağlar. Ayrıca üst düzey sistem yazılımı ve uygulama yazılımlarının çalıştırılması'
                 ' için bir platform oluşturur. Yardımcı yazılım .. Bilgisayarın analiz edilmesine, yapılandırılmasına,'
                 ' yönetilmesine ve optimize edilmesine yardımcı olur.Ayrıca sistem yazılımı terimi, bazı yayınlarda'
                 ' yazılım geliştirme araçlarını tanımlamak için de kullanılır. Bilgisayar alıcıları nadiren sahip '
                 'olduğu işletim sistemini öncelikli olarak dikkate alarak bir bilgisayar alırlar. Fakat cep telefonu'
                 ' gibi aygıtları satın alan kişiler için bu durumun tersi geçerli olabilir. Çünkü iPhone örneğinde '
                 'olduğu gibi bu tür aygıtların sistem yazılımlarının, son kullanıcı tarafından değiştirilmesi oldukça'
                 ' zordur. Ayrıca sistem yazılımı genellikle dahili ya da önceden yüklenmiş şekilde, yararlı ve hatta'
                 ' gerekli bir altyapı kodu olarak görev yapar. Sistem yazılımının dışında, kullanıcıların dokümanlar'
                 ' oluşturmasına, oyun oynamasına, müzik dinlemesine ya da İnternet\'te gezinmesine olanak sağlayan'
                 ' yazılımlara uygulama yazılımı denir. Eğer elektronik bir donanım yapılıyorsa ihtiyaca göre en uygun'
                 ' performanslı ve en uygun fiyatlı işlemci ve donanımlar seçilmelidir. İşlemciler günümüzde 50 TLden'
                 ' başlayıp binlerce liraya kadar çıkabilmektedir. Bu yüzden doğru işlemci seçimi çok önemlidir.'
                 ' Ardından bu işlemcinin desteklediği dil ve dile uygun derleyici belirlenmelidir. Her işlemcinin'
                 ' her dile ait desteği olmadığı için, desteklediği diller arasındaki seçim bu dillerin sağladığı'
                 ' hız ve kolaylığa göre olmalıdır. Eğer bilgisayar için bir yazılım yapılıyorsa öncelikle hangi'
                 ' işletim sistemi için yazılım yapılacağı seçilir. Ardından hangi programlama dilinin kullanılacağı'
                 ' belirlenir. Bunun akabinde derleyici yardımı ile yazılan kodlar makine diline çevrilir. Yazılan'
                 ' dile uyumlu bir derleyici kullanılması bu yüzden zorunludur. Bilgisayarda dil ve derleyici uyumu '
                 'elektronik cihazlara göre daha çeşitli ve kolay erişilebilir olduğu için kısa bir araştırma ile'
                 ' ihtiyaçlar kolaylıkla bulunabilir. Burada önemli olan programı hangi işletim sistemi için'
                 ' derleyeceğinizdir.']

create_nickName(Liste=giving_sentence)
