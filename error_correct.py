from sys import stdin

def main():
    while True:
        try:
            line = stdin.readline().strip()
            if not line:
                break
            n = int(line)
            if n == 0:
                break
            matrix = []
            row = [0 for _ in range(n)]
            col = [0 for _ in range(n)]

            #matrix = [[ 0 for _ in range(n)]for _ in range(n)]
            for _ in range(n):
                line = stdin.readline().strip()
                matrix.append(list(map(int, line.split())))
            #print(matrix)
            for i in range(n):
                for j in range(n):
                    row[i] += matrix[i][j]
                    col[j] += matrix[i][j]

            corrupt = False
            r = -1 
            c = -1
            for i in range(n):
                if row[i] % 2:
                    if r != -1:
                        corrupt = True
                        break
                    else:
                        r = i
                if col[i] % 2:
                    if c != -1:
                        corrupt = True
                        break
                    else:
                        c = i
            
            if(corrupt == True):
                print("Corrupt")
                f.write("Corrupt\n")
            else:
                if(r * c == -1):
                    print("Corrupt")
                    f.write("Corrupt\n")
                elif(r == -1 and c == -1):
                    print("OK")
                    f.write("OK\n")
                else:
                    print("Change bit (" + str(r+1) + "," + str(c+1) + ")")
                    f.write("Change bit (" + str(r+1) + "," + str(c+1) + ")\n")

        except EOFError:
            break

f = open("test.txt", "w")
if __name__ == '__main__':
    main()