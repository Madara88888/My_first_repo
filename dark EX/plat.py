import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 40

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Платформер с рандомными платформами")
clock = pygame.time.Clock()

# Загрузка изображений
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill(BLUE)
coin_image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE // 2))
coin_image.fill(YELLOW)
enemy_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
enemy_image.fill(RED)
platform_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
platform_image.fill(GREEN)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False

    def update(self):
        self.velocity.y += self.gravity
        self.rect.y += self.velocity.y

        # Ограничение падения
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.on_ground = True
            self.velocity.y = 0

        # Движение влево и вправо
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Ограничение выхода за границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False

# Класс платформы
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = platform_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Класс монетки
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.direction = 1
        self.speed = 2

    def update(self):
        self.rect.x += self.direction * self.speed
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.direction *= -1

# Функция для генерации платформ
def generate_platforms():
    platforms = pygame.sprite.Group()
    # Начальная платформа
    start_platform = Platform(0, HEIGHT - TILE_SIZE)
    platforms.add(start_platform)
    # Генерация остальных платформ
    prev_x = 0
    prev_y = HEIGHT - TILE_SIZE
    for _ in range(10):  # Количество платформ
        x = prev_x + random.randint(TILE_SIZE * 2, TILE_SIZE * 4)  # Расстояние по X
        y = prev_y - random.randint(TILE_SIZE, TILE_SIZE * 3)  # Расстояние по Y
        if x > WIDTH - TILE_SIZE:
            x = WIDTH - TILE_SIZE
        if y < 0:
            y = TILE_SIZE
        platform = Platform(x, y)
        platforms.add(platform)
        prev_x, prev_y = x, y
    return platforms

# Группы спрайтов
all_sprites = pygame.sprite.Group()
platforms = generate_platforms()
all_sprites.add(platforms)
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Создание монеток
for platform in platforms:
    if random.random() < 0.5:  # 50% шанс появления монетки на платформе
        coin = Coin(platform.rect.centerx, platform.rect.top - TILE_SIZE // 2)
        all_sprites.add(coin)
        coins.add(coin)

# Создание врагов
for platform in platforms:
    if random.random() < 0.3:  # 30% шанс появления врага на платформе
        enemy = Enemy(platform.rect.centerx, platform.rect.top - TILE_SIZE)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Основной игровой цикл
running = True
score = 0
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Обновление спрайтов
    all_sprites.update()

    # Проверка столкновений игрока с платформами
    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        player.rect.bottom = hits[0].rect.top
        player.on_ground = True
        player.velocity.y = 0

    # Проверка сбора монеток
    coin_hits = pygame.sprite.spritecollide(player, coins, True)
    for coin in coin_hits:
        score += 1
        print(f"Счет: {score}")

    # Проверка столкновений с врагами
    enemy_hits = pygame.sprite.spritecollide(player, enemies, False)
    if enemy_hits:
        print("Игра окончена!")
        running = False

    # Отрисовка
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()