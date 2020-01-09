import pandas as pd
import numpy as np
from pandas import DataFrame
from pandas import Series
def read_file(dataset_path):
    seqs_by_student = {}
    student, problem, is_correct=[],[],[]
    num_skills = 0
    with open(dataset_path, 'r') as f:
        for line in f:
            fields = line.strip().split()
            student1, problem1, is_correct1 = int(fields[0]), int(fields[1]), int(fields[2])
            student.append(student1)
            problem.append(problem1)
            is_correct.append(is_correct1)
            # num_skills = max(num_skills, problem)
            # seqs_by_student[student] = seqs_by_student.get(student, []) + [[problem, is_correct]]
    return student, problem, is_correct
student, problem, is_correct=read_file("../data/assistments.txt")
df1 = DataFrame({"stu":student,"pro":problem,"is_cor":is_correct})
print(df1)
#df1 = df1.drop(["stu"],axis=1)
traindata = DataFrame.sample(df1,frac=0.8,random_state=123)
valdata1 = DataFrame.sample(df1,frac=0.2,random_state=123)
traindata.to_csv("../data/train_seq.txt",columns=["stu",'pro','is_cor'],index=False,header=False,sep = ' ')
valdata1.to_csv("../data/valdata1_seq.txt",columns=['stu','pro','is_cor'],index=False,header=False,sep = ' ')