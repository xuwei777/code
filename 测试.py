#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame
pygame.init()
#创建界面窗口，设置界面的宽400，高600
pygame.display.set_mode([400,600])
#设置窗口标题
pygame.display.set_caption("飞机大战")
#导入图片资源文件
fjtp1 = pygame.image.load("app.ico")
#将图片对象设置为窗口图标
pygame.display.set_icon(fjtp1)
input()
