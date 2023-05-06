from pygame import *
from button import Button

WIDTH, HEIGHT = 600, 480
COLOR = (0, 250, 0)
FPS = 60

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, _image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

#class Player(GameSprite):
    #def update(self):
        #keys = key.get_pressed()
        #if keys[K_w] and self.rect.y < 5:
           # self.rect.y -= self.speed
        #if keys[K_s] and self.rect.y > 595:
            #self.rect.y -= self.speed

class Player(GameSprite):
    def __init__(self, _image, x=0, y=0, width=50, height=50, speed =5, Key_up=K_w, Key_down=K_s):
        super().__init__(_image, x, y, width, height)
        self.speed = speed
        self.Key_up = Key_up
        self.Key_down = Key_down
    def update(self):
        keys = key.get_pressed()
        if keys[self.Key_up]:
            self.rect.y -= self.speed
        if keys[self.Key_down]:
            self.rect.y += self.speed


mw = display.set_mode ((WIDTH, HEIGHT))
mw.fill(COLOR)
display.set_caption('Пинг понг')
clock = time.Clock()

btn_start = Button(y=150, width=150, height=40, text='Начать игру', font_size=24)
btn_exit = Button(y=270, width=150, height=40, text='Выход', font_size=24)   
btn_restart = Button(y=250, width=150, height=40, text='Перезапуск', font_size=24)
btn_credits = Button(y=210, width=150, height=40, text='Об авторе.', font_size=24)
btn_continuie = Button(y=220, width=150, height=40, text='Продолжить', font_size=24)
btn_exit_in_pause = Button(y=280, width=150, height=40, text='Выход', font_size=24)



player_1 = Player('Plat.png', 10, 200, 30, 90, 4)
player_2 = Player('Plat.png', 520, 200, 30, 90, 4, Key_up=K_k, Key_down=K_j)
Ball = Player('pngwing.com (1).png', 200, 200, 50, 50, 4)

speed_y = 3
speed_x = 3

def game_run():
    global speed_x, speed_y
    mw.fill(COLOR)
    player_1.update()
    player_2.update()
    Ball.rect.x += speed_x
    Ball.rect.y += speed_y

    if sprite.collide_rect(player_1, Ball) or sprite.collide_rect(player_2, Ball):
        speed_x *= -1
        speed_y *= 1

    if Ball.rect.y > HEIGHT - 50 or Ball.rect.y < 0:
        speed_y *= -1

    if Ball.rect.x < 0:
        print('Первый')

    if Ball.rect.x > WIDTH:
        print('Второй')

    player_1.reset()
    player_2.reset()
    Ball.reset()


def menu(events):
    mw.fill(COLOR)
    btn_start.update(events)
    btn_exit.update(events)
    btn_credits.update(events)
    btn_start.draw(mw)
    btn_exit.draw(mw)
    btn_credits.draw(mw)
    global stage
    if btn_start.is_clicked(events):
        stage = 'game'
    if btn_exit.is_clicked(events):
        stage = 'off'

def pause(events):
    mw.fill(COLOR)
    btn_continuie.update(events)
    btn_exit_in_pause.update(events)
    btn_continuie.draw(mw)
    btn_exit_in_pause.draw(mw)
    global stage
    if btn_continuie.is_clicked(events):
        stage = 'game'
    if btn_exit_in_pause.is_clicked(events):
        stage = 'menu'


stage = 'menu'
while stage != 'off':
    events = event.get()
    for e in events:
        if e.type == QUIT:
            stage = 'off'
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause'

    if stage == 'menu':
        menu(events)
    if stage == 'game':
        game_run()
    if stage == 'pause':
        pause(events)

    display.update()
    clock.tick(FPS)
