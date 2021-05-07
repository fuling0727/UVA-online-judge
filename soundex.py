from sys import stdin
def findSound(word):
    if(word == 'B' or word == 'F' or word == 'P' or word == 'V'):
        return 1
    if(word == 'C' or word == 'G' or word == 'J' or word == 'K' or word == 'Q' or word == 'S' or word == 'X' or word == 'Z'):
        return 2
    if(word == 'D' or word == 'T'):
        return 3
    if(word == 'L'):
        return 4
    if(word == 'M' or word == 'N'):
        return 5
    if(word == 'R'):
        return 6
    return 0
def main():
    while True:
        try:
            line = stdin.readline().strip()
            if not line:
                break

            word = [c for c in line]
            #print(word)
            last = -1
            output = ''
            for i in range(len(word)):
                num = findSound(word[i])
                if num == 0:
                    last = num
                    continue
                if num != last:
                    output += str(num)
                
                last = num

            print(output)
            f.write(output + "\n")

        except EOFError:
            break
f = open("test.txt", "w")
if __name__ == '__main__':
    main()