from sys import stdin

class contestant:
    def __init__(self, id, solve, time, result):
        self.id = id
        self.solve = solve
        self.time = time
        self.result = result

def main():
    cases = int(stdin.readline().strip())
    stdin.readline()
    incorrect = [0 for _ in range(101)]
    time = [0 for _ in range(101)]
    for _ in range(cases):
        contest = [contestant(0,0,0,0) for _ in range(101)]
        while True:
            try:
                line = stdin.readline().strip()
                if not line:
                    break
                team, s, t, result = line.split()
                team = int(team)
                s = int(s)
                t = int(t)
                print(team, s, t, result)
                contest[team].result = 1
                if result == 'I':
                    incorrect[team] += 1
                if result = 'C':
                    if time[team][s] == 0:
                        time[team][s] = t
                        contest[team].solve += 1
                        contest[team].time = contest[team].time + t + incorrect[team][s] * 20
                

            except Exception:
                break

            

f = open("demofile3.txt", "w")
if __name__ == '__main__':
    main()

