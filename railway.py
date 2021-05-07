from sys import stdin
import queue

def main():
    while True:
        try:
            n = int(stdin.readline().strip())
            if not n:
                break
            
            while True:
                try:
                    q = queue.Queue()
                    stack = queue.LifoQueue()
                    line = stdin.readline().strip()
                    if not line or line == '0':
                        break
                    a = list(map(int, line.split()))
                    for i in a:
                        q.put(i)
                    for i in range(1, n+1, 1):
                        stack.put(i)
                        while(stack.empty()==False and q.queue[0] == stack.queue[stack.maxsize-1]):
                            q.get()
                            stack.get()
                    if stack.empty():
                        print('Yes')
                        f.write('Yes\n')
                    else:
                        print('No')
                        f.write('No\n')
                    #print(a)

                except EOFError:
                    break
            print()
            f.write('\n')

        except Exception:
            break


f = open("demofile3.txt", "w")
if __name__ == '__main__':
    main()