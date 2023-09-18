import pygame as pg


class Tank(pg.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pg.image.load('Tank (уменьш.).png')
        self.image_copy = self.image
        self.rect = self.image.get_rect()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += 1
            self.image = pg.transform.rotate(self.image_copy, 270)
        elif keys[pg.K_a]:
            self.rect.x -= 1
            self.image = pg.transform.rotate(self.image_copy, 90)
        elif keys[pg.K_w]:
            self.rect.y -= 1
            self.image = self.image_copy
        elif keys[pg.K_s]:
            self.rect.y += 1
            self.image = pg.transform.rotate(self.image_copy, 180)

    def update(self, screen):
        screen.blit(self.image, self.rect)
        self.move()


class Tank2(Tank):
    def init(self):
        super().init()

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.rect.x += 1
            self.image = pg.transform.rotate(self.image_copy, 270)
        elif keys[pg.K_LEFT]:
            self.rect.x -= 1
            self.image = pg.transform.rotate(self.image_copy, 90)
        elif keys[pg.K_UP]:
            self.rect.y -= 1
            self.image = self.image_copy
        elif keys[pg.K_DOWN]:
            self.rect.y += 1
            self.image = pg.transform.rotate(self.image_copy, 180)