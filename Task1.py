"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# 解析通话记录和短信记录，重构号码列表
texts_incoming,texts_answering,texts_time = zip(*texts)
calls_incoming,calls_answering,calls_time,calls_during = zip(*calls)
tel_numbers =  texts_incoming + texts_answering + calls_incoming + calls_answering

#利用集合去重，并统计号码个数
count = len(set(tel_numbers))

#显示结果
print("There are {} different telephone numbers in the records.".format(count))

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
