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

# 解析通话记录，重构通话列表
calls_incoming,calls_answering,calls_time,calls_during = zip(*calls)
call_in = list(zip(calls_incoming,calls_during))
call_an = list(zip(calls_answering,calls_during))
call_total = call_in + call_an

# 定义函数
def number_time(calllist):
    calltime = {}
    for num,time in calllist:
        if num in calltime:
            calltime[num] = int(calltime[num]) + int(time)
        else:
            calltime[num] = int(time)
    return calltime

# 调用函数
c = number_time(call_total)
number = max(c,key=c.get)
time = c[number]

# 显示结果
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number,time))

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
