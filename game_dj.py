#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,random,game_zd,time
kuan = 512
gao = 768
#定义的敌机类
class Drfj():
    def __init__(self):
        self.num = str(random.randint(1,7))
        self.djtp = pygame.image.load("PlaneWar/res/img-plane_" + self.num + ".png")
        #敌机的矩形位置
        self.djtp_rect = self.djtp.get_rect()
        #敌机的默认出现位置
        self.djtp_rect[0] = random.randint(0,kuan - self.djtp_rect[2])
        self.djtp_rect[1] = -self.djtp_rect[3]
        #敌机的移动速度
        self.spped = random.randint(2,4)
        self.zdlb = [game_zd.Zidan() for _ in range(10)]

    def move(self):
        #敌机的直线移动
        self.djtp_rect.move_ip(0,self.spped)
        #只要飞机不到达屏幕下方，就将飞机放回屏幕上面
        if self.djtp_rect[1] >= gao:
            self.reset()

    def reset(self):
        #重新定义飞机的移动位置
        self.djtp_rect[0] = random.randint(0, kuan - self.djtp_rect[2])
        self.djtp_rect[1] = -self.djtp_rect[3]
        self.spped = random.randint(2,4)

    def djfs(self):
        for zd in self.zdlb:
            if not zd.fs:
                zd.zdtp_rect[0] = self.djtp_rect[0] + self.djtp_rect[2] / 2 - zd.zdtp_rect[2] / 2
                zd.zdtp_rect[1] = self.djtp_rect[1] - self.djtp_rect[3]
                zd.fs = True
                break