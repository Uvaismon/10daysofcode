from functools import cmp_to_key
from statistics import variance

def comparator(t1, t2):
    if t1.score > t2.score:
        return -1
    elif t1.score < t2.score:
        return 1
    else:
        return 0

class test_cases:

    def __init__(self, gpa, test_number):
        self.gpa = gpa
        self.test_number = test_number
        self.grades = []
        self.score = 0
        self.var = 0
        self.read()
        self.scoring()
        if self.var == 1:
            self.score = 0

    def read(self):
        inp = list(map(float, input().split()))
        if variance(inp) == 0:
            self.var = 1
        self.grades = [(i, inp.index(i)+1) for i in inp]
    
    def scoring(self):
        self.grades.sort()
        for i in range(len(self.grades)):
            if self.grades[i][1] == self.gpa[i][1]:
                self.score += 1
    

for _ in range(int(input())):
    intake = int(input())
    gpa = list(map(float, input().split()))
    gpa = [(i, gpa.index(i)+1) for i in gpa]
    tests = [test_cases(gpa, i+1) for i in range(5)]
    tests = sorted(tests, key=cmp_to_key(comparator))
    print(tests[0].test_number)