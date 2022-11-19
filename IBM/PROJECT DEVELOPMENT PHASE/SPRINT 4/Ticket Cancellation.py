from pickle import load,dump
import time
import random
import os
class tickets:
    def _init_(self):
        self.no_ofac1stclass=0
        self.totaf=0
        self.no_ofac2ndclass=0
        self.no_ofac3rdclass=0
        self.no_ofsleeper=0
        self.no_oftickets=0
        self.name=''
        self.age=''
        self.resno=0
        self.status=''    
    def ret(self):
        return(self.resno)
    def retname(self):
        return(self.name)
    def display(self):
        f=0
        fin1=open("tickets.dat","rb")
        if not fin1:
            print "ERROR"
        else:
            print
            n=int(raw_input("ENTER PNR NUMBER : "))
            print "\n\n"
            print ("FETCHING DATA . . .".center(80))
            time.sleep(1)
            print
            print('PLEASE WAIT...!!'.center(80))
            time.sleep(1)
            os.system('cls')
            try:
                while True:
                    tick=load(fin1)
                    if(n==tick.ret()):
                        f=1
                        print "="*80
                        print("PNR STATUS".center(80))
                        print"="*80
                        print
                        print "PASSENGER'S NAME :",tick.name
                        print
                        print "PASSENGER'S AGE :",tick.age
                        print
                        print "PNR NO :",tick.resno
                        print
                        print "STATUS :",tick.status
                        print
                        print "NO OF SEATS BOOKED : ",tick.no_oftickets
                        print
            except:
                pass
            fin1.close()
            if(f==0):
                print
                print "WRONG PNR NUMBER..!!"
                print              
    def pending(self):
         self.status="WAITING LIST"
         print "PNR NUMBER :",self.resno
         print
         time.sleep(1.2)
         print "STATUS = ",self.status
         print
         print "NO OF SEATS BOOKED : ",self.no_oftickets
         print
    def confirmation (self):
        self.status="CONFIRMED"
        print "PNR NUMBER : ",self.resno
        print
        time.sleep(1.5)
        print "STATUS = ",self.status
        print
    def cancellation(self):
        z=0
        f=0
        fin=open("tickets.dat","rb")
        fout=open("temp.dat","ab")
        print
        r= int(raw_input("ENTER PNR NUMBER : "))
        try:
            while(True):
                tick=load(fin)
                z=tick.ret()
                if(z!=r):
                    dump(tick,fout)
                elif(z==r):
                     f=1
        except:
            pass
        fin.close()
        fout.close()
        os.remove("tickets.dat")
        os.rename("temp.dat","tickets.dat")
        if (f==0):
            print
            print "NO SUCH RESERVATION NUMBER FOUND"
            print
            time.sleep(2)
            os.system('cls')      
        else:
            print
            print "TICKET CANCELLED"
            print"RS.600 REFUNDED...."
    def reservation(self):
        trainno=int(raw_input("ENTER THE TRAIN NO:"))
        z=0
        f=0
        fin2=open("tr1details.dat")
        fin2.seek(0)
        if not fin2:
            print "ERROR"
        else:          
            try:
                while True:
                    tr=load(fin2)
                    z=tr.gettrainno()
                    n=tr.gettrainname()
                    if (trainno==z):
                        print
                        print "TRAIN NAME IS : ",n
                        f=1
                        print
                        print "-"*80
                        no_ofac1st=tr.getno_ofac1stclass()
                        no_ofac2nd=tr.getno_ofac2ndclass()
   …
