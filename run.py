from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_x, pl_y, pl_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (w, h))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 520:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 520:
            self.rect.y += self.speed

init()
font.init()

mw = display.set_mode((600, 500))
mw.fill((255, 0, 255))
clock = time.Clock()
finish = False
game = True

p1 = Player('left1.png', 30, 200, 15, 20, 150)
p2 = Player('left1.png', 520, 200, 15, 20, 150)
ball = GameSprite('ball.png', 200, 200, 15, 50, 50)
font1 = font.Font(None, 30)
font1 = font.Font(None, 30)
lose_left = font1.render('Левый игрок проиграл!', True, (255, 0, 0))
lose_right = font1.render('Правй игрок проиграл игрок проиграл!', True, (255, 0, 0))
back = (255, 255, 0)
speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False   
    if not finish:
        mw.fill(back)
        p1.update_l()
        p2.update_r()
       
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1
        
        if ball.rect.x > 600:
            finish = True
            mw.blit(lose_left, (200, 200))
            game = True
        p1.reset()
        p2.reset()
        ball.reset()








    display.update()
    clock.tick(30)




