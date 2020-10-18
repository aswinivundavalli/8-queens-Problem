N = 8


class Queens:
    def __init__(self, n=N):
        self.n = n            # no.of queens
        self.reset()          # initial state,no queens on board

    def reset(self):
        n = self.n
        self.y = [None] * n             # Where is the queen in column x
        self.row = [0] * n              # Is row[y] safe?
        self.up = [0] * (2*n-1)         # Is upward diagonal[x-y] safe?
        self.down = [0] * (2*n-1)       # Is downward diagonal[x+y] safe?
        self.nfound = 0                 # Instrumentation

    def solve(self, x=0):               # Recursive solver
        for y in range(self.n):         # x-column,y-row
            if self.safe(x, y):
                self.place(x, y)
                if x+1 == self.n:
                    self.display()
                else:
                    self.solve(x+1)
                self.remove(x, y)

    def safe(self, x, y):
        return not self.row[y] and not self.up[x-y] and not self.down[x+y]

    def place(self, x, y):
        self.y[x] = y
        self.row[y] = 1
        self.up[x-y] = 1
        self.down[x+y] = 1

    def remove(self, x, y):
        self.y[x] = None
        self.row[y] = 0
        self.up[x-y] = 0
        self.down[x+y] = 0
    silent = 0                          # If true, count solutions only

    def display(self):
        self.nfound = self.nfound + 1
        if self.silent:
            return
        print ('___'*2*(self.n-1))
        for y in range(self.n-1, -1, -1):
            print ('|',end =" "),
            for x in range(self.n):
                if self.y[x] == y:
                    print ("_Q_|",end =" "),
                else:
                    print ("___|",end =" "),
            print ()
        print ('___'*2*(self.n-1))

def main():
    silent = 0
    n = N
    q = Queens(n)
    q.silent = silent
    q.solve()
    print ("Found", q.nfound, "solutions.")

if __name__ == "__main__":
    main()
