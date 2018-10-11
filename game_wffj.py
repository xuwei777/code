#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,random,game_zd
kuan = 512
gao = 768

#定义的我方飞机类
class Yxfj(object):
    def __init__(self):
        self.fj1 = pygame.image.load("PlaneWar/res/hero.png")
        # 获取飞机矩形对象位置(0，0，宽，高)
        self.fj1_rect = self.fj1.get_rect()
        #初始化飞机的登场位置
        self.fj1_rect.move_ip(kuan / 2 - self.fj1_rect[2],gao - self.fj1_rect[3] -20)
        #飞机的移动速度
        self.speed = 3
        self.zdlb = [game_zd.Zidan() for _ in range(10)]
    def move_s(self):
        if self.fj1_rect[1] > 0:
            self.fj1_rect.move_ip(0,-self.speed)


    def move_x(self):
        if self.fj1_rect[1] < gao - self.fj1_rect[3]:
            self.fj1_rect.move_ip(0, self.speed)

    def move_z(self):
        if self.fj1_rect[0] > 0:
            self.fj1_rect.move_ip(-self.speed,0)

    def move_y(self):
        if self.fj1_rect[0] < kuan - self.fj1_rect[2]:
            self.fj1_rect.move_ip(self.speed,0)
    #按下空格键即可发射子弹
    def zd(self):
        for zd in self.zdlb:
            #如果子弹是没发射状态
            if not zd.fs:
                zd.zdtp_rect[0] = self.fj1_rect[0] + self.fj1_rect[2] / 2 - zd.zdtp_rect[2] / 2
                zd.zdtp_rect[1] = self.fj1_rect[1] - self.fj1_rect[3]
                zd.fs = True
                break