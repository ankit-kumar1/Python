"""input is passed as number of users, then username and marks for 3 subjects and finally the student whose average you want to display
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika"""

import math
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    avg=sum(student_marks[query_name])/len(student_marks[query_name])
    print('%.2f'%avg)
## result must be a float with 2 decimal places
