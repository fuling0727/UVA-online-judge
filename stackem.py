from sys import stdin
from itertools import islice
suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def covert2d(l, n):
    tmp = []
    for i in range(n):
        tmp.append(l[i*52:(i+1)*52])
    return tmp

def execute():
    global shuffle, k
    tmp = list(range(1, 53))
    for i in k:
        tmp2 = list(tmp)
        for a, b in enumerate(shuffle[i-1]):
            tmp2[a] = tmp[b-1]
        tmp = tmp2
    return tmp

def main():
    cases = int(stdin.readline().strip())
    stdin.readline()
    for c in range(cases):
        
        line = stdin.readline().strip()
        if not line:
            continue
        shuffle_num = int(line)
        global card, shuffle
        shuffle = []
        card = [i for i in range(1, 53, 1)]
        while(len(shuffle) < shuffle_num*52):
            shuffle.extend(list(map(int, stdin.readline().strip().split())))
        #print(cards)
        shuffle = covert2d(shuffle, shuffle_num)
        print(shuffle)
        print(card)
        global k
        k = []
        while True:
            try:
                tmp = int(stdin.readline().strip())
                k.append(tmp)
            except Exception:
                break
        
        
        
        output = execute()
        for i in range(52):
            tmp = output[i]-1
            print(value[tmp%13] + " of " + suit[tmp//13])
            f.write(value[tmp%13] + " of " + suit[tmp//13] + '\n')
        if(c < cases-1):
            print()
            f.write('\n')

        #print(k)
f = open("test.txt", "w")
if __name__ == '__main__':
    main()