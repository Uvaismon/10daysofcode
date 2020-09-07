from functools import cmp_to_key
from statistics import mean, variance

def comparator(t1, t2):
    if t1.score > t2.score:
        return 1
    elif t1.score < t2.score:
        return -1
    else:
        return 0

class test_cases:

    def __init__(self, gpa, test_number):
        self.gpa = gpa
        self.test_number = test_number
        self.grades = list(map(float, input().split()))
        self.score = 0
        if variance(self.grades) == 0 and variance(self.gpa) != 0:
            self.score = float('inf')
        else:
            self.scoring()

    def scoring(self):
        for i in range(len(self.grades)):
            self.grades[i] = (self.grades[i] - mean(self.grades)) / (max(self.grades) - min(self.grades))
        diff = []
        for i in range(len(self.grades)):
            diff.append((self.gpa[i] - self.grades[i]) ** 2)
        self.score = mean(diff)
    
for _ in range(int(input())):
    intake = int(input())
    gpa = list(map(float, input().split()))
    for i in range(intake):
        gpa[i] = (gpa[i] - mean(gpa)) / (max(gpa) - min(gpa))
    test = [test_cases(gpa, i+1) for i in range(5)]
    test = sorted(test, key=cmp_to_key(comparator))
    print(test[0].test_number)