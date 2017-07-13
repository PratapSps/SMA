'''
Created on Jul 11, 2017

@author: Survya Pratap Singh
Wright State University
UID: U00803205
email: singh.survya@gmail.com
website: https://survya.com
'''
import re


# data="https:www.survya.com/spspratap"
# 
# list=(data.rsplit('/', 1))
# print(list[1])

# data=" Survya Pratap 252Singh 68 7th  OH 43201. Mob: 9375816431 | E-mail: singh.survya .sogeti@gmail.com.in Website:\xc2\xa0..."
# a="Survya Pratap"
# b="pratap.singh"
# c="sdfsdf"
# regrex=a+'|'+b+ \
#     c
# 
# 
# regular_expression = re.compile(regrex,re.IGNORECASE)
# result = re.search(regular_expression, data)
# if result:
#     print(result)

# regular_expression = re.compile(r"\(?"  # open parenthesis
#                                         r"(\d{3})?"  # area code
#                                         r"\)?"  # close parenthesis
#                                         r"[\s\.-]{0,2}?"  # area code, phone separator
#                                         r"(\d{3})"  # 3 digit exchange
#                                         r"[\s\.-]{0,2}"  # separator bbetween 3 digit exchange, 4 digit local
#                                         r"(\d{4})",  # 4 digit local
#                                         re.IGNORECASE)
# result = re.search(regular_expression, data)
# result = result.groups()
# result = "-".join(result)
# print(result)

# regular1=re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
# result = re.search(regular1, data)
# if result:
#     print(result.group(0))
# # result1 = result1.groups()
# # result1 = "-".join(result1)

dict={2:['sdfds']}
dict.update({2:['uiriwerwr']})
dict.update({3:['sdfhga']})
for d,c in dict.items():
    print(d)
    print(c[0])
