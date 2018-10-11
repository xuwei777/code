#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,random
kuan = 512
gao = 768
#定义的地图类
class Du(object):
    def __init__(self):
        #设置滚动地图并导入地图资源文件
        self.num = str(random.randint(1,5))
        self.bj1 = pygame.image.load("PlaneWar/res/img_bg_level_" + self.num + ".jpg")
        self.bj2 = pygame.image.load("PlaneWar/res/img_bg_level_" + self.num + ".jpg")
        self.bj1_y = -gao
        self.bj2_y = 0
        self.speed = 1
    def sudu(self):
        if self.bj1_y >= 0:
            self.bj1_y = -gao
        if self.bj2_y >= gao:
            self.bj2_y = 0
        self.bj1_y += self.speed
        self.bj2_y += self.speed