class Linear_probing:
    dic = dict()
    k = 0

    def add_to_hash (lines):
        dic = Linear_probing.dic
        k = Linear_probing.k
        ct = 0
       

        for i in range(0,len(lines)):
            dic[lines[i]] = None
        for lineEach in lines:
            asciiValue = 0
            r = 0
            for c in lineEach: #Her bir char değerini kontrol ediyoruz
                asciiValue += ord(c) #Char değerlerinin integer karşılıklarını teker teker topluyoruz
            r = asciiValue % k #Elde edilen toplam ascii değerlerinin tablo büyüklüğüne göre modu alınıyor
            # def remainder(rem,dict,asciiV): #Hash tablosunda kullanılmayan hash key bulunana kadar recursive bir fonksiyon çalıştırıyoruz.
            #     if rem not in dic.values() and (rem in range(0,len(lines))): #Hash key dolu değil ise kelimemiz bu hash key için atanıyor
            #         return rem
            #     else:   #Eğer hash key dolu ise kelimenin ascii toplamına 1 ekleyip işlemi baştan yapıyoruz(recursive)
            #         asciiV += 1 
            #         rem = asciiV % k
            #         return remainder(rem,dict,asciiV)
            dic[lineEach] = r  
            #dc[r].insert_at_end(lineEach)    
            #dic[lineEach] = remainder(r,dic,asciiValue) #hash tablomuzda kelimelere uygun hash key bulmak için kalan işlemini tekrarlayan fonksiyonu çağırıyoruz. 
        for key,value in dic.items():
            dc[value].insert_at_end(key)
        

    def distance (var):
        #print("\033[1;31;40m You have searched for the hash key ",var," which has ","hash value of ",Linear_probing.dic[var],".\033[0m" )
        #print("\033[1;31;40m The processing order of the input is " + str((Linear_probing.dic[var] - 0) + 1) + ".\033[0m")
        #print("Hash key for ",var," is ",Linear_probing.dic[var]," and its distance to its hash key is " + str((Linear_probing.dic[var] - 0) + 1))
        for i in range(0,len(dc)):
            dc[i].traverse_list(i,var)
        return 
    
    def display():

        #[ print("\033[1;31;40m Hash Key value of " , key , " is " , value,"\033[0m") for (key, value) in Linear_probing.dic.items()] 
        listofTuples = sorted(Linear_probing.dic.items() , key=lambda x: x[1]) #Sort hash table items in order to key values ->(x : X[1])
        #for elem in listofTuples :  #Printing sorted hash table in order to key values one by one
        #    print(elem[0] , " ::" , elem[1] ) 

        for hk, hv in listofTuples:
            if hk == listofTuples[-1][0]:
                print(hk,end="\n")
            else:
                print(hk,end=", ")
        for i in range(0,len(dc)):
            dc[i].traverse_list(i,None)
        #llist = LinkedList()
        #for key, value in listofTuples:
            #llist.insert_at_end(value)
        #llist.traverse_list()
        #[ print("Hash Key " , value+1 , ": " , key) for (key, value) in Linear_probing.dic.items()]
class Node: #Düğüm yapıları oluşturuldu.
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList: #LinkedList yapısı oluşturuldu ve listeyi yazdıran fonksiyon burada
    def __init__(self):
        self.start_node = None
        
    def traverse_list(self,HKNO,dist):
        temp = 0
        incr = 0
        if dist != None:
            if self.start_node is None:
                return
            else:
                #print("\n Linked List order is below: \n")
                n = self.start_node

                
                while n is not None:
                    
                    if n.item == dist:
                        print("Hash Key for "+ dist + " is " + str(HKNO)+" and its distance to its hash key is " + str(incr))
                        break
                    else:
                        incr += 1
                        n = n.ref
                        
                
        else:
            if self.start_node is None:
                return
            else:
                #print("\n Linked List order is below: \n")
                n = self.start_node
                print("Hash Key " + str(HKNO)+":",end=" ")
                while n is not None:
                    if n.ref is None:
                        print(n.item)
                    else:
                        print(n.item,end=",")

                    #if n.item==0:
                        #print("\033[1;31;40m (",n.item , " : ", word,")\033[0m",end=" " )
                    #else:
                        #print("\033[1;31;40m <=(attached to) ","(",n.item , " : ", word,")\033[0m",end=" " )
                    #print(word,end=", " )
                    #print(n.item , " : ", word ) #prints the linked list in order but the code above is more specific which shows connections between them
                    n = n.ref
                listofTuples = sorted(Linear_probing.dic.items() , key=lambda x: x[1])  
                # print("\n")
                # for i in range(0,len(dc)):  
                #     [ print("Hash Key " , vl+1 , ": " , ky) for (ky, vl) in listofTuples]
    def insert_at_end(self, data):
            new_node = Node(data)
            if self.start_node is None:
                self.start_node = new_node
                return
            n = self.start_node
            while n.ref is not None:
                n= n.ref
            n.ref = new_node;
    def clear(self):
        if self.start_node is None:
            #print("\033[1;33;40m Linked List has just cleared! \033[0m") #LinkedList temizlendi uyarısı
            return

        n = self.start_node
        while n is not None:
            n = n.ref
        n.ref = None

        
filepath = "test.txt" #işleme koyulacak metin dosyasının adresini tanımlıyoruz.
with open(filepath) as f:
    lines = [line.rstrip() for line in f]   

dc = []
linkedlist_number = None 



print("1- Add a text file to the hash table\n2- Search a word in the hash table\n3- Display the hash table\n4- Exit\n")
      
def main():

    while True:
        
        
        try:
            func = int(input("\nWhat you want to do: "))
            if func==1 or func==2 or func==3 or func==4:
                break
            else:
                print("Please enter an ID of functions you want to execute!")
        except:
            print("Please enter an ID of functions you want to execute!")
    if func==1:
        global dc
        global linkedlist_number
        
        Linear_probing.k = int(input("Enter the hash mode value:  "))
        
        dc = []
        linkedlist_number = Linear_probing.k
        while linkedlist_number!=0:
            dc.append(LinkedList())
            linkedlist_number = linkedlist_number - 1

        
        
        # while Linear_probing.k < len(lines): #To be able to add all elements in list, mod must be equal or higher than lenght of list
        #     print("Please enter a valid value.")
        #     Linear_probing.k = int(input("Enter the hash mode value:  "))
        #print("\033[1;31;40m Mod value is: ",Linear_probing.k,"\033[0m")
        Linear_probing.add_to_hash(lines) #Sınıfa ait add_to_hash fonksiyonu çağrılarak her kelime için hash key tanımlıyoruz.
        #print(Linear_probing.dic)
        return main()
    if func==2:
        if Linear_probing.k is 0:
            print("<<<Please determine mod first!>>>")
            return main()
        user = str(input("Enter the word you want to search:  "))
        while user not in Linear_probing.dic.keys(): #if user enter a key which doesn't exist in hash table, program will ask until the user enter a valid one.
            print("\nPlease enter a valid key which is included in the list!")
            user = str(input("Enter the word you want to search:  "))
        Linear_probing.distance(user)
        return main()
    if func==3:
        Linear_probing.display()
        return main()
    
    if func==4:
        #print("\033[1;31;40m Execution is running off..\033[0m")
        #print("\033[1;31;40m Done!\033[0m")
        print("The Program has been ended")
        
    

if __name__ == '__main__': #Kod dosyası çalıştırılınca ilk olarak çalışacak fonksiyonu tanımlıyoruz: "main()"
    main()