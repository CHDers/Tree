'''
🚀🚀🚀🚀🚀🚀:
Descripttion: Yanjun Hao的代码
version: 1.0.0
Author: Yanjun Hao
Date: 2023-06-26 22:51:09
LastEditors: Yanjun Hao
LastEditTime: 2023-06-26 22:53:45
'''
# 显示文件夹树状目录
import os
import os.path

def dfs_showdir(path, depth):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        if '.git' not in item:
            print("|      " * depth + "+--" + item)
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                dfs_showdir(newitem, depth +1)


if __name__ == '__main__':
    path = "./"             # 文件夹路径
    dfs_showdir(path, 0)  # 显示文件夹的树状结构