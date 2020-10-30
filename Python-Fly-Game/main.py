#-*- coding:utf-8 -*-
from __future__ import division
import pygame
import time
import sys
from pygame.locals import *
import hero
import enemy
import bullet
import supply
import random


pygame.init()
pygame.mixer.init()

#创建一个窗口，用来显示内容
bg_size = width,height = 470,690
screen = pygame.display.set_mode(bg_size,0,32)
#添加标题
pygame.display.set_caption("飞机大战")
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
# 载入游戏音乐
pygame.mixer.music.load("./sound/game_music.mp3")
pygame.mixer.music.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("./sound/enemy1_down.ogg")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("./sound/enemy2_down.ogg")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("./sound/enemy3_down.ogg")
enemy3_down_sound.set_volume(0.4)
enemy3_fly_sound = pygame.mixer.Sound("./sound/effcet_ui_feijishengji.ogg")
enemy3_fly_sound.set_volume(0.2)
hero_down_sound = pygame.mixer.Sound("./sound/game_over.ogg")
hero_down_sound.set_volume(0.5)
upgrade_sound = pygame.mixer.Sound("./sound/excellent.ogg")
upgrade_sound.set_volume(0.3)
bomb_sound = pygame.mixer.Sound("./sound/bomb_sound.ogg")
bomb_sound.set_volume(0.3)
supply_sound = pygame.mixer.Sound("./sound/supply_sound.ogg")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("./sound/get_bomb_sound.ogg")
get_bomb_sound.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("./sound/bullet.ogg")
bullet_sound.set_volume(0.1)
# 创建一个和窗口大小图片，用来充当背景
background = pygame.image.load("./images/background.png")

def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def add_speed(target,inc):
    for each in target:
        each.speed += inc

def main():
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    #初始化英雄飞机
    heroPlan = hero.Hero(bg_size)
    #用于切换图片
    switch_image = True
    #用于延迟
    delay = 100
    #中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    hero_destroy_index = 0

    #初始化敌机
    enemies = pygame.sprite.Group()
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)

    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(heroPlan.rect.midtop))

    # 生成超级子弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 8
    for i in range(BULLET2_NUM // 2):
        bullet2.append(bullet.Bullet2((heroPlan.rect.centerx-25,heroPlan.rect.centery)))
        bullet2.append(bullet.Bullet2((heroPlan.rect.centerx+20,heroPlan.rect.centery)))

    #统计分数
    score = 0
    score_font =pygame.font.Font("font/font.otf",36)

    #设置难度级别
    level = 1

    #全屏炸弹
    bomb_image = pygame.image.load("images/bomb.png")
    bomb_rect = bomb_image.get_rect()
    bomb_font = pygame.font.Font("font/font.otf",48)
    bomb_num = 3

    #每30秒发放一个不补给包
    bullet_supply = supply.Bullet_Supply(bg_size)
    bomb_supply = supply.Bomb_Supply(bg_size)
    SUPPLY_TIME = USEREVENT
    pygame.time.set_timer(SUPPLY_TIME,30 * 1000)

    #超级子弹定时器
    DOUBLE_BULLET_TIME = USEREVENT + 1

    #标志是否使用超级子弹
    is_double_bullet = False

    #标志是否暂停游戏
    paused = False
    paused_nor_image = pygame.image.load("images/paused_nor.png")
    paused_pressed_image = pygame.image.load("images/paused_pressed.png")
    resume_nor_image = pygame.image.load("images/resume_nor.png")
    resume_pressed_image = pygame.image.load("images/resume_pressed.png")
    paused_rect = paused_nor_image.get_rect()
    paused_rect.left,paused_rect.top = width - paused_rect.width - 10 ,10
    paused_image = paused_nor_image

    #生命数量
    life_image = pygame.image.load("images/life.png")
    life_rect = life_image.get_rect()
    life_num = 3

    #解除英雄机无敌状态定时器
    INVINCIBLE_TIME = USEREVENT + 2

    #用于阻止重复打开记录文件
    recorded = False

    #游戏结束画面
    gameover_font = pygame.font.Font("font/font.otf",48)
    restart_image = pygame.image.load("images/restart_nor.png")
    restart_rect = restart_image.get_rect()
    quit_image = pygame.image.load("images/quit_nor.png")
    quit_rect = quit_image.get_rect()

    #主流程
    while True:
        # 设置需要显示的背景图
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME,30*1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_pressed_image
                    else:
                        paused_image = paused_pressed_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = paused_nor_image
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if bomb_num:
                        bomb_num -= 1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom > 0:
                                each.active = False
            elif event.type == SUPPLY_TIME:
                supply_sound.play()
                if random.choice([True,False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()
            elif event.type == DOUBLE_BULLET_TIME:
                is_double_bullet = False
                pygame.time.set_timer(DOUBLE_BULLET_TIME,0)
        #根据用户的得分增加难度
        if level == 1 and score > 5000:
            level = 2
            upgrade_sound.play()
            #增加3架小型敌机，2架中型敌机，1架大型敌机
            add_small_enemies(small_enemies,enemies,3)
            add_mid_enemies(mid_enemies,enemies,2)
            add_big_enemies(big_enemies,enemies,1)
            #提高小型机的速度
            add_speed(small_enemies,1)
        elif level == 2 and score > 30000:
            level = 3
            upgrade_sound.play()
            # 增加5架小型敌机，3架中型敌机，2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提高小型机的速度
            add_speed(small_enemies, 1)
            add_speed(mid_enemies, 1)
        elif level == 3 and score > 60000:
            level = 4
            upgrade_sound.play()
            # 增加5架小型敌机，3架中型敌机，2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提高小型机的速度
            add_speed(small_enemies, 1)
            add_speed(mid_enemies, 1)
        elif level == 4 and score > 100000:
            level = 5
            upgrade_sound.play()
            # 增加5架小型敌机，3架中型敌机，2架大型敌机
            add_small_enemies(small_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 3)
            add_big_enemies(big_enemies, enemies, 2)
            # 提高小型机的速度
            add_speed(small_enemies, 1)
            add_speed(mid_enemies, 1)
            add_speed(big_enemies, 1)
        elif event.type == INVINCIBLE_TIME:
            heroPlan.invincible = False
            pygame.time.set_timer(INVINCIBLE_TIME,0)


        if life_num and not paused:
            #检测用户的键盘操作
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                heroPlan.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                heroPlan.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                heroPlan.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                heroPlan.moveRight()

            # 绘制超级子弹补给并检测是否获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image, bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply, heroPlan):
                    get_bomb_sound.play()
                    #发射超级子弹
                    is_double_bullet =True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME,18 * 1000)
                    bullet_supply.active = False

            #绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,heroPlan):
                    get_bomb_sound.play()
                    if bomb_num < 3:
                        bomb_num += 1
                    bomb_supply.active = False

            # 发射子弹
            if not (delay % 10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets = bullet2
                    bullets[bullet2_index].reset((heroPlan.rect.centerx-25,heroPlan.rect.centery))
                    bullets[bullet2_index+1].reset((heroPlan.rect.centerx+20,heroPlan.rect.centery))
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM
                else:
                    bullets = bullet1
                    bullets[bullet1_index].reset(heroPlan.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM
            #检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemy_hit = pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                if enemy_hit:
                    b.active = False
                    for e in enemy_hit:
                        if e in mid_enemies or e in big_enemies:
                            e.hit = True
                            e.energy -= 1
                            if e.energy == 0:
                                e.active = False
                        else:
                            e.active = False


            #绘制大型敌机
            for each in big_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit = False
                    else:
                        if switch_image:
                            screen.blit(each.image1,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)

                    #绘制血槽
                    pygame.draw.line(screen,BLACK,\
                                     (each.rect.left,each.rect.top - 5),\
                                     (each.rect.right,each.rect.top - 5),\
                                     2)
                    #当生命大于20%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.BigEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen,energy_color,\
                                     (each.rect.left,each.rect.top - 5),\
                                     (each.rect.left + each.rect.width * energy_remain,each.rect.top - 5),\
                                     2)

                    #即将出场，播放音效
                    if each.rect.bottom == -50:
                        enemy3_fly_sound.play(-1)
                else:
                    #毁灭
                    if not (delay % 3):
                        if e3_destroy_index == 0:
                            enemy3_down_sound.play()
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                        e3_destroy_index = (e3_destroy_index + 1) % 6
                        if e3_destroy_index == 0:
                            enemy3_fly_sound.stop()
                            score += 10000
                            each.reset()

            #中型敌机
            for each in mid_enemies:
                if each.active:
                    each.move()
                    if each.hit:
                        screen.blit(each.image_hit,each.rect)
                        each.hit = False
                    else:
                        screen.blit(each.image,each.rect)

                    #绘制血槽
                    pygame.draw.line(screen,BLACK,\
                                     (each.rect.left,each.rect.top - 5),\
                                     (each.rect.right,each.rect.top - 5),\
                                     2)
                    #当生命大于20%显示绿色，否则显示红色
                    energy_remain = each.energy / enemy.MidEnemy.energy
                    if energy_remain > 0.2:
                        energy_color = GREEN
                    else:
                        energy_color = RED
                    pygame.draw.line(screen,energy_color,\
                                     (each.rect.left,each.rect.top - 5),\
                                     (each.rect.left + each.rect.width * energy_remain,each.rect.top - 5),\
                                     2)

                else:
                    #毁灭
                    if not (delay % 3):
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                        e2_destroy_index = (e2_destroy_index + 1) % 4
                        if e2_destroy_index == 0:
                            enemy2_down_sound.play()
                            score += 6000
                            each.reset()
            #小型敌机
            for each in small_enemies:
                if each.active:
                    each.move()
                    screen.blit(each.image,each.rect)
                else:
                    #毁灭
                    if not (delay % 5):
                        if e1_destroy_index == 0:
                            enemy1_down_sound.play()
                        screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

            #检测敌我飞机是否碰撞
            enemies_down = pygame.sprite.spritecollide(heroPlan,enemies,False,pygame.sprite.collide_mask)
            if enemies_down and not heroPlan.invincible:
                heroPlan.active = False
                for e in enemies_down:
                    e.active = False

            #绘制英雄飞机
            if heroPlan.active:
                if switch_image:
                    screen.blit(heroPlan.image1,heroPlan.rect)
                else:
                    screen.blit(heroPlan.image2,heroPlan.rect)
            else:
                #毁灭
                hero_down_sound.play()
                if not (delay % 3):
                    screen.blit(heroPlan.destroy_images[hero_destroy_index],heroPlan.rect)
                    hero_destroy_index = (hero_destroy_index + 1) % 4
                    if hero_destroy_index == 0:
                        life_num -= 1
                        heroPlan.reset()
                        pygame.time.set_timer( INVINCIBLE_TIME,3 * 1000)

            #绘制剩余生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,(width-10-(i+1)*life_rect.width,height-10-life_rect.height))

            #绘制全屏炸弹数量
            bomb_text = bomb_font.render("x %d" % bomb_num,True,RED)
            text_rect = bomb_text.get_rect()
            screen.blit(bomb_image,(10,height - 10 - bomb_rect.height))
            screen.blit(bomb_text,(20 + bomb_rect.width,height - 5 - text_rect.height))

            #绘制得分
            score_text = score_font.render("Scroe : %s" % str(score),True,WHITE)
            screen.blit(score_text,(10,5))

        #绘制游戏结束画面
        elif life_num == 0:
            #背景音乐停止
            pygame.mixer.music.stop()
            #停止全部音效
            pygame.mixer.stop()
            #停止发放补给
            pygame.time.set_timer(SUPPLY_TIME,0)

            if not recorded:
                recorded = True
                #读取历史最高得分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())
                #如果玩家得分高于历史最高得分，则存档
                if score > record_score:
                    with open("record.txt","w") as f:
                        f.write(str(score))

            #绘制游戏结束画面
            record_score_text = score_font.render("Best : %d" % record_score,True,WHITE)
            screen.blit(record_score_text,(50,50))

            gameover_text1 = gameover_font.render("Your Score",True,(255,255,255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left,gameover_text1_rect.top = (width - gameover_text1_rect.width) //2,\
                                                               (height -gameover_text1_rect.height) // 2 - 50
            screen.blit(gameover_text1,gameover_text1_rect)

            gameover_text2 = gameover_font.render(str(score),True,(255,255,255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left,gameover_text2_rect.top = (width - gameover_text2_rect.width) //2,\
                                                               gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2,gameover_text2_rect)

            restart_rect.left,restart_rect.top = (width - restart_rect.width) // 2,(gameover_text2_rect.bottom + 50)
            screen.blit(restart_image,restart_rect)

            quit_rect.left, quit_rect.top = (width - quit_rect.width) // 2, restart_rect.bottom + 10
            screen.blit(quit_image,quit_rect)

            #检测用户的鼠标操作
            #如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                #获取鼠标坐标
                pos = pygame.mouse.get_pos()
                #如果用户点击“重新开始，重新开始游戏”
                if restart_rect.left < pos[0] < restart_rect.right and restart_rect.top < pos[1] < restart_rect.bottom:
                    #调用main()函数，重新开始游戏
                    main()
                #如果用户点击“结束游戏”
                elif quit_rect.left < pos[0] < quit_rect.right and quit_rect.top < pos[1] < quit_rect.bottom:
                    pygame.quit()
                    sys.exit()




        #绘制暂停按钮
        screen.blit(paused_image,paused_rect)
        # 显示需要显示的内容
        # pygame.display.update()
        pygame.display.flip()
        clock.tick(60)
        #切换图片
        if not (delay % 5):
            switch_image = not switch_image
        delay -= 1
        if not delay:
            delay = 100
        #增加延时，解决cup占用率较高的问题
        time.sleep(0.01)

if __name__ == '__main__':
    main()

