from sys import stdin
import queue
import heapq
#f = open("test.txt", "w")
def main():
    while True:
        try:
            q = queue.Queue()
            stack = queue.LifoQueue()
            heap = []
            is_stack, is_q, is_heap = True, True, True
            line = stdin.readline().strip()
            if not line:
                break
            cases = int(line)
            data = [list(map(int,stdin.readline().strip().split())) for _ in range(cases)]
            #print(data)

            for i in range(cases):
                if data[i][0] == 1:
                    stack.put(data[i][1])
                    q.put(data[i][1])
                    heapq.heappush(heap, -data[i][1])
                elif data[i][0] == 2:
                    if(stack.empty()):
                        is_stack = False
                    if(q.empty()):
                        is_q = False
                    if(len(heap) <= 0):
                        is_heap = False

                    if(is_stack and stack.get() != data[i][1]):
                        is_stack = False
                    if(is_q and q.get() != data[i][1]):
                        is_q = False
                    if(is_heap and heapq.heappop(heap) != -data[i][1]):
                        is_heap = False

            if not is_stack and not is_q and not is_heap:
                print('impossible')
                #f.write('impossible\n')
            elif is_stack and not is_heap and not is_q:
                print('stack')
                #f.write('stack\n')
            elif is_heap and not is_stack and not is_q:
                print('priority queue')
                #f.write('priority queue\n')
            elif is_q and not is_stack and not is_heap:
                print('queue')
                #f.write('queue\n')
            else:
                print('not sure')
                #f.write('not sure\n')

        except(EOFError):
            break

if __name__ == '__main__':
    main()
