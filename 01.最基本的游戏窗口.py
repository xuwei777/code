#!/usr/bin/env python
#_*_ coding:utf-8 _*
__author__ = "xuwei"
import pygame,sys,random
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
        self.zdlb = [Zidan() for _ in range(10)]
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
        #每张图的y轴在自增
        self.bj1_y += self.speed
        self.bj2_y += self.speed

#定义的整体类
class Yxck(object):
    def __init__(self):
        pygame.init()
        self.bt = pygame.display.set_caption("飞机大战")
        self.tb = pygame.display.set_icon(pygame.image.load("PlaneWar/res/app.ico"))
        self.ck = pygame.display.set_mode([kuan,gao])
        self.du = Du()
        self.yxfj = Yxfj()
        self.drfj = [Drfj() for _ in range(5)]
    #处理各个矩形坐标
    def action(self):
        #地图自行滚动
        self.du.sudu()
        for zd in self.yxfj.zdlb:
            if zd.fs:
                zd.move()
        for dj in self.drfj:
            dj.move()
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
    #游戏主循环
    def run(self):
        while True:
            #1 处理矩形坐标的位置
            self.action()
            #2 根据矩形坐标绘制元素
            self.huizhi()
            #3 处理事件情况
            self.event()
            #4 刷新窗口
            self.update()

    def gameover(self):
        sys.exit()
        pygame.quit()



def main():
    game = Yxck()
    game.run()
if __name__ == "__main__":
    main()