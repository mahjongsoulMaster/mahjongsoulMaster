# -*- coding: UTF-8 -*-
# Time: 2023/6/5 23:50
# Author: Forsaken996
# @file: player.py
# @software: PyCharm
# 模拟玩家  条t、饼b、万w、红宝牌0t、0b、0w、东南西北中发白、(0-6)z
class player:
    def __init__(self):
        self.sp = []  # 手牌  ['']
        self.mp = []  # 鸣牌，包括吃、碰、大明杠
        self.ps = []  # 牌河
        self.bb = 0  # 三麻拔北数量


if __name__ == '__main__':
    tags = {}
    for i in range(1, 10):
        tags.update({f"{i}t": f"{i}条"})
    for i in range(1, 10):
        tags.update({f"{i}b": f"{i}饼"})
    for i in range(1, 10):
        tags.update({f"{i}w": f"{i}万"})
    tags['0t'] = '红宝5条'
    tags['0b'] = '红宝5饼'
    tags['0w'] = '红宝5万'
    tags['0z'] = '东'
    tags['1z'] = '南'
    tags['2z'] = '西'
    tags['3z'] = '北'
    tags['4z'] = '中'
    tags['5z'] = '发'
    tags['6z'] = '白'
    print(tags)
    pp = []  # 四麻牌山
    for p in tags:
        if p[0] is '5' and p is not '5z':
            for i in range(0, 3):
                pp.append(p)
            pp.append(f"0{p[1]}")
        elif p is '0t' or p is '0b' or p is '0w':
            continue
        else:
            for i in range(0, 4):
                pp.append(p)
    print(pp)
    print(len(pp))
    ps = []  # 三麻牌山
    for p in tags:
        if p[1] is 'w' and p[0] is not '1' and p[0] is not '9':
            continue
        if p[0] is '5' and p is not '5z':
            for i in range(0, 3):
                ps.append(p)
            ps.append(f"0{p[1]}")
        elif p is '0t' or p is '0b' or p is '0w':
            continue
        else:
            for i in range(0, 4):
                ps.append(p)
    print(ps)
    print(len(ps))