#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :统计空行.py
# @Time      :2020/11/30 19:50
# @Author    :maomao
f1 = open(r'F:\Users\zhengcy\PycharmProjects\untitled\hanshu\test.txt', 'r', encoding='utf-8')  # 打开要去掉空行的文件
f2 = open(r'F:\Users\zhengcy\PycharmProjects\untitled\hanshu\b.txt', 'w', encoding='utf-8')  # 生成没有空行的文件

for line in f1.readlines():
    if line == '\n':
        line = line.strip("\n")
    f2.write(line)
print('输出成功....')
f1.close()
f2.close()
