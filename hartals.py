from sys import stdin
def main():
    cases = int(stdin.readline().strip())
    for _ in range(cases):
        N = int(stdin.readline().strip())
        P = int(stdin.readline().strip())
        h = []
        hartal = []
        for i in range(N+1):
            hartal.append(0)
        count = 0
        for _ in range(P):
            h.append(int(stdin.readline().strip()))

        for i in range(P):
            tmp = h[i]
            while(h[i] <= N):
                try:
                    
                    hartal[h[i]] = 1
                    h[i] += tmp
                except IndexError:
                    break

        for i in range(1, N+1, 1):
            if(hartal[i] == 1 and i%7 != 0 and i%7 != 6):
                count += 1
		
        print(count)
        #f.write(str(count) + "\n")
        
#f = open("test.txt", "w")
if __name__ == '__main__':
    main()