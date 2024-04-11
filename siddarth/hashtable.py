#skilltest no.2
def display_hash(hashtable):
    for i in range(len(hashtable)):
        print(i,end=" ")
        for j in hashtable[i]:
            print("-->",end=" ")
            print(j,end=" ")
        print()
HashTable=[[]for _ in range(10)] 

def hashing(keyvalue):
    return keyvalue%len(HashTable)
def insert(Hashtable,keyvalue,value):
    hash_key=hashing(keyvalue)
    HashTable[hash_key].append(value)

insert(HashTable, 10 , 'Allahabad')
insert(HashTable, 25 , 'Mumbai')
insert(HashTable, 20 , 'Mathura')
insert(HashTable, 9  , 'Delhi')
insert(HashTable, 21 , 'Punjab')
insert(HashTable, 21 , 'Noida')
display_hash(HashTable)