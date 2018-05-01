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

# 第一部分
# 解析通话记录，重构通话列表
calls_incoming,calls_answering,calls_time,calls_during = zip(*calls)
call_total = list(zip(calls_incoming,calls_answering))

# 定义查找被呼号码函数
def find_an(call_list):
    l = []
    for inc,ans in call_list:
        if '(080)' in inc:
            if ')' in ans:
                l.append(ans[:ans.find(')')+1])
            elif ' ' in ans:
                l.append(ans[:4])
            elif ans[:3] == '140':
                l.append('140')
    return l

# 调用函数
c = find_an(call_total)
c = list(set(c))
c.sort()

# 显示结果
print("The numbers called by people in Bangalore have codes:")
for i in c:
    print(i)

# 第二部分
#定义计算占比函数
def ratio(call_list):
    l = find_an(call_list)
    n = l.count('(080)')
    return n/len(l)

#调用函数
r = ratio(call_total)

#显示结果
print("\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(r,2)))



"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
