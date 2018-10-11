#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,random
kuan = 512
gao = 768
#定义子弹类
class Zidan():
    def __init__(self):
        self.zdtp = pygame.image.load("PlaneWar/res/bullet_10.png")
        #获取子弹的矩形对象
        self.zdtp_rect = self.zdtp.get_rect()
        #子弹是否是发射状态，true表示发射，false表示没有，默认没有，不绘制和处理碰撞
        self.fs = False
        self.speed = 4


    def move(self):
        #默认向上移动
        self.zdtp_rect.move_ip(0,-self.speed)
        #子弹飞到屏幕外面就将子弹状态设置为Fales
        if self.zdtp_rect[1] < 0 + -self.zdtp_rect[3]:
            self.fs = False

