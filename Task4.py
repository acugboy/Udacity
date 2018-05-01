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

# 解析通话记录和短信记录，重构通信号码列表
calls_incoming,calls_answering,calls_time,calls_during = zip(*calls)
texts_incoming,texts_answering,texts_time = zip(*texts)
nums = list(set(calls_answering + texts_incoming + texts_answering))

#定义审核函数
def check_up(calls_in):
    l = []
    for c in calls_in:
        if c not in nums:
            l.append(c)
    return l

#调用函数
calls = list(set(calls_incoming))
numlist = check_up(calls)
numlist.sort()

#显示结果
print("These numbers could be telemarketers: ")
for i in numlist:
    print(i)






"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

