from sys import stdin
import sys
f = open("test.txt", "w")
def main():
    while True:
        try:
            
            is_jolly = True
            jump = [0 for _ in range(3001)]
            line = stdin.readline().strip()
            if not line:
                break
            num = list(map(int, line.rstrip().split()))
            length = num[0]
            num.pop(0)
            #print(num)
            for i in range(1, length):
                sub = abs(num[i]-num[i-1])
                
                if(sub >= length or sub <= 0 or jump[sub] == 1):
                    is_jolly = False
                if(sub < 3001):
                    jump[sub] = 1
           
            if(is_jolly):
                print('Jolly')
                f.write('Jolly\n')
            else:
                print('Not jolly')
                f.write('Not jolly\n')
            #print(num)
            #print(sub)

        except(EOFError):
            break
if __name__ == '__main__':
    main()