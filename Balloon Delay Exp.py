import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
# Images. Balloon = blue, explosion = orange.
BALLOON_IMAGE = pg.Surface((50, 50), pg.SRCALPHA)
pg.draw.circle(BALLOON_IMAGE, pg.Color('steelblue2'), (25, 25), 25)
EXPLOSION_IMAGE = pg.Surface((80, 80), pg.SRCALPHA)
pg.draw.circle(EXPLOSION_IMAGE, pg.Color('sienna1'), (40, 40), 40)


class Balloon(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = BALLOON_IMAGE
        self.rect = self.image.get_rect(center=pos)
        self.timer = 3

    def update(self, dt):
        self.timer -= dt


class Explosion(pg.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = EXPLOSION_IMAGE
        self.rect = self.image.get_rect(center=pos)
        self.timer = 1

    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.kill()


balloons = pg.sprite.Group(Balloon((300, 300)))
all_sprites = pg.sprite.Group(balloons)

done = False

while not done:
    dt = clock.tick(30) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            balloon = Balloon(event.pos)
            balloons.add(balloon)
            all_sprites.add(balloon)

    all_sprites.update(dt)
    for balloon in balloons:
        if balloon.timer <= 0:
            balloon.kill()
            all_sprites.add(Explosion(balloon.rect.center))

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)

    pg.display.flip()
