# -*- coding: UTF-8 -*-
# Time: 2023/6/5 23:38
# Author: Forsaken996
# @file: mahjong.py
# @software: PyCharm
# 模拟雀魂麻将，以便于进一步强化学习
from player import player


class mahjong_game:
    def __init__(self, model="三麻"):
        self.zc = []  # 座次
        if model == "三麻":
            self.players = [player for i in range(0, 3)]  # 三麻玩家
        elif model == "四麻":
            self.players = [player for i in range(0, 4)]  # 四麻玩家


if __name__ == '__main__':
    mahjong_game(model="三麻")
