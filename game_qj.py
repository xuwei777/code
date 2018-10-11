#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,random,game_zd,game_dj,game_dt,game_wffj,time
kuan = 512
gao = 768
#定义的整体类
class Yxck(object):
    def __init__(self):
        pygame.init()
        #窗口标题
        pygame.display.set_caption("飞机大战")
        pygame.display.set_icon(pygame.image.load("PlaneWar/res/app.ico"))
        #加载背景音乐
        pygame.mixer_music.load("PlaneWar/res/bg2.ogg")
        #循环背景音乐
        pygame.mixer_music.play(-1)
        #停止背景音乐
        self.gameover_yy = pygame.mixer.Sound("PlaneWar/res/gameover.wav")
        #pygame.mixer_music.stop()
        #创建地图
        self.ck = pygame.display.set_mode([kuan,gao])
        self.du = game_dt.Du()
        #创建我放地方飞机
        self.yxfj = game_wffj.Yxfj()
        self.drfj = [game_dj.Drfj() for _ in range(5)]
        self.score = 0
        self.zdlb = [game_zd.Zidan() for _ in range(10)]
        for fs in self.drfj:
            self.zdfs = [fs for _ in self.zdlb]

    def txt(self,text,size,x,y):
        font = pygame.font.SysFont("SimHei",size)
        #rander（text（文本内容），antialias（抗锯齿），color（rgb），返回文字对象）
        textobj = font.render(text,1,(255,255,255))
        #设置文字矩形对象位置
        textect = textobj.get_rect()
        textect.move_ip(x,y)
        #在指定位置绘制文字对象
        self.ck.blit(textobj,textect)

    #处理各个矩形坐标
    def action(self):
        #地图自行滚动
        self.du.sudu()
        for zd in self.yxfj.zdlb:
            if zd.fs:
                zd.move()
        for dj in self.drfj:
            dj.move()
        # for dd in self.zdfs:
        #     dd.move()
            #time.sleep(2)

    #根据矩形坐标对图形进行绘制
    def huizhi(self):
        self.ck.blit(self.du.bj1,(0,self.du.bj1_y))
        self.ck.blit(self.du.bj2,(0,self.du.bj2_y))
        self.ck.blit(self.yxfj.fj1,(self.yxfj.fj1_rect[0],self.yxfj.fj1_rect[1]))
        for zd in self.yxfj.zdlb:
            if zd.fs:
                self.ck.blit(zd.zdtp,(zd.zdtp_rect[0],zd.zdtp_rect[1]))
        for dj in self.drfj:
            self.ck.blit(dj.djtp,(dj.djtp_rect[0],dj.djtp_rect[1]))
        for zd in self.zdlb:
            self.ck.blit(zd.zdtp,(zd.zdtp_rect[0],zd.zdtp_rect[1]))

        self.txt("得分：%s" % str(self.score),20,5,5)
    #处理事件
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameover()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameover()
                if event.key == pygame.K_SPACE:
                    self.yxfj.zd()
        lxaj = pygame.key.get_pressed()
        if lxaj[pygame.K_UP]:
            self.yxfj.move_s()
        if lxaj[pygame.K_DOWN]:
            self.yxfj.move_x()
        if lxaj[pygame.K_LEFT]:
            self.yxfj.move_z()
        if lxaj[pygame.K_RIGHT]:
            self.yxfj.move_y()


    # 窗口刷新
    def update(self):
        pygame.display.update()

    def gameover(self):
        sys.exit()
        pygame.quit()

    def bzjc(self):
        for zd in self.yxfj.zdlb:
            if zd.fs:
                for fj in self.drfj:
                    #判断子弹是否和某个敌机发生碰撞
                    if pygame.Rect.colliderect(zd.zdtp_rect, fj.djtp_rect):
                        #如果发生碰撞，则让敌机回到开始位置
                        fj.reset()
                        #子弹也设置为false
                        zd.fs = False
                        self.score += 1
                        #同时跳出循环，不再和后面的敌机检测
                        break
    #判断英雄飞机和敌机碰撞
    def wfbz(self):
        for fj in self.drfj:
            if pygame.Rect.colliderect(self.yxfj.fj1_rect,fj.djtp_rect):
                return True
            return False

    #等待用户输入 如果是回车则进入游戏主循环
    def yhsr(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameover()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.gameover()
                    if event.key == pygame.K_RETURN:
                        return

    #游戏开始界面
    def game_begin(self):
        #  绘制初始的地图
        self.ck.blit(self.du.bj2, (0, self.du.bj2_y))
        self.ck.blit(self.yxfj.fj1, (kuan / 2 - self.yxfj.fj1_rect[2] / 2, gao - self.yxfj.fj1_rect[3] - 20))
        # 绘制文字
        self.txt("飞机大战", 40, kuan / 2 - 80, gao /3)
        self.txt("按下enter开始，esc退出.", 25, kuan /2 - 120, gao /2)
        self.update()
        #input()
        # 等待用户输入
        self.yhsr()
    def game_again(self):
        #停止游戏音乐
        pygame.mixer_music.stop()
        self.gameover_yy.play()
        self.txt("你的飞机被撞毁了，得分为%s,按下enter继续" % self.score,20,20,gao / 3)
        self.update()
        self.yhsr()
        self.gameover_yy.stop()
        #     # 游戏主循环
    def run(self):
        self.game_begin()
        while True:
            # 1 处理矩形坐标的位置
            self.action()
            # 2 根据矩形坐标绘制元素
            self.huizhi()
            # 3 处理事件情况
            self.event()
            # 4 判断子弹和敌机碰撞
            self.bzjc()
            # 5判断英雄飞机和敌机的碰撞
            if self.wfbz():
                break
            # 5 刷新窗口
            self.update()
        self.game_again()
        #判断两个矩形是否相交，相交返回true，否则返回false
        #flag =

def main():
    while True:
        game = Yxck()
        game.run()
if __name__ == "__main__":
    main()