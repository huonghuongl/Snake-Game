import sys
import pygame 
import time
from random import randint
import os
import json
WIDTH = 1500
HEIGHT = 755
COLOR = '#000000'
MOUSE_LEFT = 0
MOUSE_MIDDLE = 1
MOUSE_RIGHT = 2
BG_IMG = 'Little-Big-Snake-640.jpg'
THEME_IMG = 'theme.png'
# Khởi tạo Pygame và các cấu hình ban đầu
pygame.init()
pygame.font.init()
pygame.mixer.init()
eat = pygame.mixer.Sound("eat.MP3")
eat.set_volume(0.5)
lose = pygame.mixer.Sound("game over.MP3")
lose.set_volume(0.5)
ruong = pygame.mixer.Sound("ruong.MP3")
ruong.set_volume(0.5)
sound_played = False
pygame.display.set_caption('Rắn Săn Mồi')
music_volume = 0.5
sound_volume = 0.5
# Hình ảnh và màu sắc
display = pygame.display.set_mode((WIDTH, HEIGHT))
eagle = pygame.image.load('ai-generated-majestic-haast-s-eagle-on-transparent-background-png (1).webp').convert_alpha()
eagle = pygame.transform.scale(eagle, (100, 100))
eagle_x_pos = 0
lung = pygame.image.load('honey-badger-mat-ong-lung-compressor.png').convert_alpha()
lung = pygame.transform.scale(lung, (50, 50))
lung_y_pos = 800
lung2 = pygame.image.load('lung_2.png.png').convert_alpha()
lung2 = pygame.transform.scale(lung2, (50, 50))
lung2_y_pos = 800
food_img = pygame.image.load('apple.png').convert_alpha()
food_img = pygame.transform.scale(food_img, (15,15))
food2_img = pygame.image.load('golden-apple.png').convert_alpha()
food2_img = pygame.transform.scale(food2_img, (15,15))
head1_images = {
    "up": pygame.image.load("snake (2) - Copy.png").convert_alpha(),
    "down": pygame.image.load("snake (1) - Copy.png").convert_alpha(),
    "left": pygame.image.load("snake (1).png").convert_alpha(),
    "right": pygame.image.load("snake (3) - Copy.png").convert_alpha(),
}
head1_images["up"] = pygame.transform.scale(head1_images["up"], (15, 15))
head1_images["down"] = pygame.transform.scale(head1_images["down"], (15, 15))
head1_images["left"] = pygame.transform.scale(head1_images["left"], (15, 15))
head1_images["right"] = pygame.transform.scale(head1_images["right"], (15, 15))
tail1_images = {
    "up": pygame.image.load("last_tail - Copy.png").convert_alpha(),
    "down": pygame.image.load("last_tail - Copy (3).png").convert_alpha(),
    "left": pygame.image.load("last_tail - Copy (4).png").convert_alpha(),
    "right": pygame.image.load("last_tail.png").convert_alpha(),
}
tail1_images["up"] = pygame.transform.scale(tail1_images["up"], (15, 15))
tail1_images["down"] = pygame.transform.scale(tail1_images["down"], (15, 15))
tail1_images["left"] = pygame.transform.scale(tail1_images["left"], (15, 15))
tail1_images["right"] = pygame.transform.scale(tail1_images["right"], (15, 15))
head2_images = {
    "up": pygame.image.load("snake2 - Copy.png").convert_alpha(),
    "down": pygame.image.load("snake2 - Copy (2).png").convert_alpha(),
    "left": pygame.image.load("snake2 - Copy (3).png").convert_alpha(),
    "right": pygame.image.load("snake2.png").convert_alpha(),
    
}
head2_images["up"] = pygame.transform.scale(head2_images["up"], (15, 15))
head2_images["down"] = pygame.transform.scale(head2_images["down"], (15, 15))
head2_images["left"] = pygame.transform.scale(head2_images["left"], (15, 15))
head2_images["right"] = pygame.transform.scale(head2_images["right"], (15, 15))
tail2_images = {
    "up": pygame.image.load("last_tail2.png").convert_alpha(),
    "down": pygame.image.load("last_tail2 - Copy (3).png").convert_alpha(),
    "left": pygame.image.load("last_tail2 - Copy.png").convert_alpha(),
    "right": pygame.image.load("last_tail2 - Copy (4).png").convert_alpha(),
}
tail2_images["up"] = pygame.transform.scale(tail2_images["up"], (15, 15))
tail2_images["down"] = pygame.transform.scale(tail2_images["down"], (15, 15))
tail2_images["left"] = pygame.transform.scale(tail2_images["left"], (15, 15))
tail2_images["right"] = pygame.transform.scale(tail2_images["right"], (15, 15))
body1_images = {
    "horizontal": pygame.image.load("body.png").convert_alpha(),
    "vertical": pygame.image.load("body - Copy (2).png").convert_alpha(),
    "turn_upleft": pygame.image.load("curve - Copy (2).png").convert_alpha(),
    "turn_downleft": pygame.image.load("curve - Copy.png").convert_alpha(),
    "turn_upright": pygame.image.load("curve.png").convert_alpha(),
    "turn_downright": pygame.image.load("curve - Copy (3).png").convert_alpha(),
}
body1_images["horizontal"] = pygame.transform.scale(body1_images["horizontal"], (15, 15))
body1_images["vertical"] = pygame.transform.scale(body1_images["vertical"], (15, 15))
body1_images["turn_upleft"] = pygame.transform.scale(body1_images["turn_upleft"], (15, 15))
body1_images["turn_downleft"] = pygame.transform.scale(body1_images["turn_downleft"], (15, 15))
body1_images["turn_uprightl"] = pygame.transform.scale(body1_images["turn_upright"], (15, 15))
body1_images["turn_downright"] = pygame.transform.scale(body1_images["turn_downright"], (15, 15))
body2_images = {
    "horizontal": pygame.image.load("body2.png").convert_alpha(),
    "vertical": pygame.image.load("body2 - Copy - Copy.png").convert_alpha(),
    "turn_upleft": pygame.image.load("curve2 - Copy - Copy - Copy.png").convert_alpha(),
    "turn_downleft": pygame.image.load("curve2 - Copy.png").convert_alpha(),
    "turn_upright": pygame.image.load("curve2.png").convert_alpha(),
    "turn_downright": pygame.image.load("curve2 - Copy - Copy.png").convert_alpha(),
}
body2_images["horizontal"] = pygame.transform.scale(body2_images["horizontal"], (15, 15))
body2_images["vertical"] = pygame.transform.scale(body2_images["vertical"], (15, 15))
body2_images["turn_upleft"] = pygame.transform.scale(body2_images["turn_upleft"], (15, 15))
body2_images["turn_downleft"] = pygame.transform.scale(body2_images["turn_downleft"], (15, 15))
body2_images["turn_uprightl"] = pygame.transform.scale(body2_images["turn_upright"], (15, 15))
body2_images["turn_downright"] = pygame.transform.scale(body2_images["turn_downright"], (15, 15))
pause_img = pygame.image.load("pause-button.png").convert_alpha()
pause_img = pygame.transform.scale(pause_img, (30, 40))
resume_img = pygame.image.load("play-button.png").convert_alpha()
resume_img = pygame.transform.scale(resume_img, (30, 40))
reboot_img = pygame.image.load("pngegg.png").convert_alpha()
reboot_img = pygame.transform.scale(reboot_img, (50,50))
setting_img = pygame.image.load("pngegg (1).png").convert_alpha()
setting_img = pygame.transform.scale(setting_img, (50,50))
home_img = pygame.image.load("kindpng_822678.png").convert_alpha()
home_img = pygame.transform.scale(home_img, (50,50))
back_img = pygame.image.load("icons8-left-3-50.png").convert_alpha()
back_img = pygame.transform.scale(back_img, (50,50))
chest = None
chest_timer = time.time()
chest_img = pygame.image.load('chest.png').convert_alpha()
chest_img = pygame.transform.scale(chest_img, (15,15))
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
# Các biến game
running = True
in_menu = True
direct = "right"
direction = "left"
food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
clock = pygame.time.Clock()
snakes = [[5, 10], [6, 10], [7, 10]]
players = [[WIDTH // 15 - 5,HEIGHT // 15 - 10], [WIDTH // 15 - 6, HEIGHT // 15 - 10], [WIDTH // 15 - 7, HEIGHT // 15 - 10]]
stop = False
scorepl1 = 0 #Điểm của Player 1
scorepl2 = 0 #Điểm của Player 2
font = pygame.font.Font("SupportSports-E4Xvl.ttf", 40)
snake_head_rect = head1_images[direct].get_rect(topleft=(snakes[-1][0] * 15, snakes[-1][1] * 15))
player_head_rect = head2_images[direction].get_rect(topleft=(players[-1][0] * 15, players[-1][1] * 15))
# File lưu trữ high score
HIGH_SCORE_FILE = "high_scores.json"
def load_high_scores():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return json.load(file)
    return {"player1": 0, "player2": 0, "player3": 0}
def save_high_scores(high_scores):
    with open(HIGH_SCORE_FILE, "w") as file:
        json.dump(high_scores, file)
class UIComponent:
    def __init__(self, app):
        self.app = app
        self.surface = app.surface
    def update(self):
        pass
    def draw(self):
        pass
    def eventHandling(self, e):
        pass
class DifficultySettings:
    EASY = {
        "snake_speed": 0.05,
        "lung_speed": 10,
        "eagle_speed": 5,
        "chest_appearance": True,
    }
    NORMAL = {
        "snake_speed": 0.03,
        "lung_speed": 15,
        "eagle_speed": 10,
        "chest_appearance": True,
    }
    HARD = {
        "snake_speed": 0.015,
        "lung_speed": 20,
        "eagle_speed": 15,
        "chest_appearance": True,
    }
    INSANE = {
        "snake_speed": 0.005,
        "lung_speed": 20,
        "eagle_speed": 15,
        "chest_appearance": False,
    }
    IMPOSSIBLE = {
        "snake_speed": 0.0025,
        "lung_speed": 25,
        "eagle_speed": 20,
        "chest_appearance": False,
    }
    current0_settings = EASY
    @staticmethod
    def set_difficulty(difficulty):
        if difficulty == "Easy":
            DifficultySettings.current_settings = DifficultySettings.EASY
        elif difficulty == "Normal":
            DifficultySettings.current_settings = DifficultySettings.NORMAL
        elif difficulty == "Hard":
            DifficultySettings.current_settings = DifficultySettings.HARD
        elif difficulty == "Insane":
            DifficultySettings.current_settings = DifficultySettings.INSANE
        elif difficulty == "Impossible":
            DifficultySettings.current_settings = DifficultySettings.IMPOSSIBLE
class Backgroundsettings:
    Bgr1 = {"Bgr": 'bgr1.jpg'}
    Bgr2 = {"Bgr": 'bgr2.jpg'}
    Bgr3 = {"Bgr": 'bgr3.jpg'}
    Bgr4 = {"Bgr": 'bgr4.jpg'}
    Bgr5 = {"Bgr": 'bgr5.jpg'}
    Bgr6 = {"Bgr": 'bgr6.jpg'}
    Bgr7 = {"Bgr": 'bgr7.jpg'}
    current1_settings = Bgr1
    @staticmethod
    def set_Background(background):
        if background == "Bgr1":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr1
        elif background == "Bgr2":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr2
        elif background == "Bgr3":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr3
        elif background == "Bgr4":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr4
        elif background == "Bgr5":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr5
        elif background == "Bgr6":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr6
        elif background == "Bgr7":
            Backgroundsettings.current1_settings = Backgroundsettings.Bgr7
class Soundsettings:
    Sound1 = {"Sound": 'nhacchill.MP3'}
    Sound2 = {"Sound": '1127.MP3'}
    Sound3 = {"Sound": '1127(2).MP3'}
    Sound4 = {"Sound": '1127(1).MP3'}
    current2_setting = Sound1
    @staticmethod
    def set_Sound(Sound):
        if Sound == "Sound1":
            Soundsettings.current2_setting = Soundsettings.Sound1
        elif Sound == "Sound2":
            Soundsettings.current2_setting = Soundsettings.Sound2
        elif Sound == "Sound3":
            Soundsettings.current2_setting = Soundsettings.Sound3
        elif Sound == "Sound4":
            Soundsettings.current2_setting = Soundsettings.Sound4
class Menu(UIComponent):
    HOME = 'home'
    OPTIONS = 'option'
    INSTRUCT = 'instruct'
    def __init__(self, app):
        super().__init__(app)
        self.scene = Menu.HOME
        self.theme = pygame.image.load(THEME_IMG).convert_alpha()
        self.theme.set_alpha(140)  # 1 - 255
        self.app.game_mode = "1 Player"
        amthanh = Soundsettings.current2_setting["Sound"]
        pygame.mixer.music.load(amthanh)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        self.UIComponents = {
            Menu.HOME: [
                Text(self.app, text="Snake game", pos=(900, 320), size=150),
                Button(self.app, pos=(200, 300), text="START", font_size=35, onclick={self.start_game}),
                Button(self.app, pos=(200, 400), text="OPTION", font_size=35, onclick=[self.changeOptionScene]),
                Button(self.app, pos=(200, 500), text="QUIT", font_size=35, onclick=[Menu.quit]),
                Button(self.app, pos=(200, 100), text="INSTRUCT", font_size=35, onclick=[self.instruct_game]),
            ],
            Menu.OPTIONS: [
                Text(self.app, "OPTION", pos=(WIDTH // 2, 50), size=35),
                ToggleSetting(self.app, "Display mode", ["Windowed", "Fullscreen", "Borderless"],pos=(100,140), offset=310),
                ToggleSetting(self.app, "Game mode", ["1  Player", "2  Player"],pos=(WIDTH // 2 + 100, 450), offset=310),
                ToggleSetting(self.app, "Background", ["Bgr1", "Bgr2", "Bgr3", "Bgr4", "Bgr5", "Bgr6", "Bgr7"],
                              pos=(100, 400), offset=310),
                ToggleSetting(self.app, "Sound", ["Sound1", "Sound2", "Sound3", "Sound4"],pos=(100, 450), offset=310),
                SliderSetting(self.app, "Music", pos=(WIDTH // 2 + 100, 140), offset=180, value=music_volume * 100, is_music=True),
                SliderSetting(self.app, "Sound", pos=(WIDTH // 2 + 100, 190), offset=180, value=sound_volume * 100, is_music=False),
                ToggleSetting(self.app, "Choose difficulty", ["Easy", "Normal", "Hard", "Insane", "Impossible"],
                              pos=(WIDTH // 2 + 100, 400), offset=310),
                Button(self.app, pos=(100, 600), text="BACK", font_size=35, topleft=True,
                       onclick=[self.changeHomeScene]),
            ],
            Menu.INSTRUCT:[
                Text(self.app, "INSTRUCT", pos=(WIDTH // 2, 50), size=35),
                Text(self.app, "1. You can use the keys a,w,s,d to move Player 1, use the arrow keys to move Player 2", pos=(603,100), size=25),
                Text(self.app, "2. Eat foods to grow longer and increase your score: ", pos=(395,140), size=25),
                Text(self.app, "+ Red apple (1 body segmaent and 1 point)", pos=(320,180), size=25),
                Text(self.app, "+ Gold apple (1 body segmaent and 2 point)", pos=(327,220), size=25),
                Text(self.app, "3. Collecting gold chests will randomly reduce your body by 1 to 5 pieces", pos=(531,260), size=25),
                Text(self.app, "4. You will lose:", pos=(138,300), size=25),
                Text(self.app, "+ caught by an eagle", pos=(181,340), size=25),
                Text(self.app, "+ Caught by badgers", pos=(177,380), size=25),
                Text(self.app, "+ Attack your own body", pos=(198,420), size=25),
                Text(self.app, "+ Cross the border", pos=(168,460), size=25),
                Text(self.app, "5. 2 players will not be able to attack each other", pos=(368,500), size=25),
                Button(self.app, pos=(100, 600), text="BACK", font_size=35, topleft=True,
                       onclick=[self.changeHomeScene]),
            ]
        }
    def instruct_game(self):
        self.scene = Menu.INSTRUCT
    def change_difficulty(self, difficulty):
        DifficultySettings.current0_settings = difficulty
        self.apply_difficulty_settings()
    def apply_difficulty_settings(self):
        settings = DifficultySettings.current_settings
        self.snake_speed = settings["snake_speed"]
        self.eagle_speed = settings["eagle_speed"]
        self.player_lives = settings["player_lives"]
    def change_background(self, background):
        Backgroundsettings.current1_settings = background
        self.apply_background_settings
    def apply_background_settings(self):
        settings = Backgroundsettings.current1_settings
        self.backgr = settings["Bgr"]
    def change_Sound(self, Sound):
        Soundsettings.current2_setting = Sound
        self.apply_Sound_settings
    def apply_Sound_settings(self):
        settings = Soundsettings.current2_setting
        self.amthanh = settings["Sound"]
    def start_game(self):
        self.run_game()
    def run_game(self):
        global eagle_x_pos, food, stop, scorepl1, scorepl2, snakes, players, direct, direction, sound_played, lung_y_pos, lung2_y_pos
        game_pause = False
        stop = False
        game_setting = False
        food2 = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
        food2_timer = 5
        eagle_move = DifficultySettings.current0_settings["eagle_speed"]
        lung_move = DifficultySettings.current0_settings["lung_speed"]
        snake_speed = DifficultySettings.current0_settings["snake_speed"]
        lung_y_pos = 800
        lung2_y_pos = 0
        pause_button_rect = pygame.Rect(WIDTH // 2, 10, pause_img.get_width(), pause_img.get_height())
        resume_button_rect = pygame.Rect(WIDTH // 2, 10, resume_img.get_width(), resume_img.get_height())
        reboot_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2, reboot_img.get_width(), reboot_img.get_height())
        setting_button_rect = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2, setting_img.get_width(), setting_img.get_height())
        home_button_rect = pygame.Rect(WIDTH // 2 + 70, HEIGHT // 2, home_img.get_width(), home_img.get_height())
        back_button_rect = pygame.Rect(WIDTH // 2 - 375, HEIGHT // 2 + 188.5, home_img.get_width(), home_img.get_height())
        music_slider = SliderSetting(self.app, "Music", pos=(WIDTH // 2 - 250, HEIGHT // 2 - 77.5), offset=180, value=music_volume * 100, is_music=True)
        sound_slider = SliderSetting(self.app, "Sound", pos=(WIDTH // 2 - 250, HEIGHT // 2 + 22.5), offset=180, value=sound_volume *100, is_music=False)
        backgr = Backgroundsettings.current1_settings["Bgr"]
        bg = pygame.image.load(backgr).convert()
        bg = pygame.transform.scale2x(bg)
        pygame.display.set_icon(bg)
        amthanh = Soundsettings.current2_setting["Sound"]
        pygame.mixer.music.load(amthanh)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        reduced_for_pl1 = False
        reduced_for_pl2 = False
        initial_snake_speed = snake_speed
        high_score_pl1 = 0
        high_score_pl2 = 0
        high_score_pl3 = 0
        #khoi tao ruong
        chest = None
        chest_timer = 0
        chest_duration = 10
        chest_cooldown = 10
        last_chest_time = 0
        # Khởi tạo điểm cao từ file
        high_scores = load_high_scores()
        high_score_pl1 = high_scores["player1"]
        high_score_pl2 = high_scores["player2"]
        high_score_pl3 = high_scores["player3"]
        while running:
            clock.tick(60)
            display.blit(bg, (0, 0))
            # Di chuyển đại bàng
            eagle_x_pos -= eagle_move
            eagle_rect = display.blit(eagle, (eagle_x_pos + WIDTH, HEIGHT // 2))
            lung_y_pos -= lung_move
            lung_rect = display.blit(lung, (WIDTH // 1.5, lung_y_pos + (HEIGHT + 245)))
            lung2_y_pos += lung_move
            lung2_rect = display.blit(lung2, (WIDTH // 3, lung2_y_pos -300))
            if lung_y_pos <= -(HEIGHT + 245):
                lung_y_pos = 0
            if lung2_y_pos >= + (HEIGHT + 245):
                lung2_y_pos = 0
            if eagle_x_pos <= -WIDTH:
                eagle_x_pos = 0
            #kiem tra thoi gian da troi qua 20 giay de hien thi ruong
            if chest is None and time.time() - last_chest_time > chest_cooldown:
                chest = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                chest_timer = time.time()
                last_chest_time = time.time()
            #kiem tra neu ruong hien thi qua lau
            if chest and time.time() - chest_timer > chest_duration:
                 chest = None
                 last_chest_time = time.time()
            #hien thi ruong neu co
            if chest:
                display.blit(chest_img, (chest[0] * 15, chest[1] *15))
            #kiem tra giua ran va ruong
            if chest and snakes[-1][0] == chest[0] and snakes[-1][1] == chest[1]:
                ruong.play()
                #giam tu 1 den 5 doan cua than ran neu va cham
                body_length = len(snakes) - 1
                reduction = randint(1,5)
                if body_length > reduction:
                    del snakes[:reduction]
                chest = None
            #va cham  giua ran 2 va ruong
            if chest and players[-1][0] == chest[0] and players[-1][1] == chest[1]:
                ruong.play()
                #giam tu 1 den 5 doan cua than ran neu va cham
                body_length = len(players) - 1
                reduction = randint(1,5)
                if body_length > reduction:
                    del players[:reduction]
                chest = None
            # Xử lý thức ăn không trùng với thân rắn
            for snake in snakes:
                if food[0] == snake[0] and food[1] == snake[1]:
                    food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
            for player in players:
                if food[0] == player[0] and food[1] == player[1]:
                    food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
            if self.app.game_mode == "1 Player":
                # Vẽ rắn 1
                for i in range(1,len(snakes)):
                    if i == 0:  # Vẽ đầu rắn
                        display.blit(head1_images[direct], (snakes[i][0] * 15, snakes[i][1] * 15))
                    elif i == len(snakes) - 1:  # Đảm bảo có ít nhất 2 đoạn
                        tail1_segment = snakes[0]        # Đoạn đuôi
                        next_to_tail1_segment = snakes[1]  # Đoạn liền kề với đuôi
                        # Xác định hướng di chuyển của đoạn đuôi
                        dx_tail1 = next_to_tail1_segment[0] - tail1_segment[0]
                        dy_tail1 = next_to_tail1_segment[1] - tail1_segment[1]
                        # Chọn hình ảnh đuôi phù hợp
                        if dx_tail1 == 1 and dy_tail1 == 0:  # Đuôi hướng sang phải
                            tail1_image = tail1_images["right"]
                        elif dx_tail1 == -1 and dy_tail1 == 0:  # Đuôi hướng sang tráisadads
                            tail1_image = tail1_images["left"]
                        elif dy_tail1 == 1 and dx_tail1 == 0:  # Đuôi hướng xuống
                            tail1_image = tail1_images["down"]
                        elif dy_tail1 == -1 and dx_tail1 == 0:  # Đuôi hướng lên
                            tail1_image = tail1_images["up"]
                        # Vẽ đuôi
                        display.blit(tail1_image, (tail1_segment[0] * 15, tail1_segment[1] * 15))
                        #print(f"Đuôi: {tail1_segment}, Đoạn liền kề: {next_to_tail1_segment},Hướng: dx={dx_tail1}, dy={dy_tail1}")
                    else:  # Vẽ thân rắn
                        prev1_segment = snakes[i - 1]
                        curr1_segment = snakes[i]
                        next1_segment = snakes[i + 1]
                        # Tính hướng trước và sau
                        dx1, dy1 = curr1_segment[0] - prev1_segment[0], curr1_segment[1] - prev1_segment[1]
                        dx2, dy2 = next1_segment[0] - curr1_segment[0], next1_segment[1] - curr1_segment[1] 
                        # Xác định hình ảnh thân
                        if dx1 == dx2 == 0 and dy1 == dy2:  # Thân thẳng ngang
                            body1_image = body1_images["vertical"]
                        elif dy1 == dy2 == 0 and dx1 == dx2:  # Thân thẳng dọc
                            body1_image = body1_images["horizontal"]
                        else:
                            if (dx1, dy1) == (1, 0) and (dx2, dy2) == (0, -1):  # Phải -> Lên
                                body1_image = body1_images["turn_upright"]
                            elif (dx1, dy1) == (1, 0) and (dx2, dy2) == (0, 1):  # Phải -> Xuống
                                body1_image = body1_images["turn_downright"]
                            elif (dx1, dy1) == (-1, 0) and (dx2, dy2) == (0, -1):  # Trái -> Lên
                                body1_image = body1_images["turn_upleft"]
                            elif (dx1, dy1) == (-1, 0) and (dx2, dy2) == (0, 1):  # Trái -> Xuống
                                body1_image = body1_images["turn_downleft"]
                            elif (dx1,dy1) == (0, -1) and (dx2,dy2) == (1, 0):  #lên -> phải
                                body1_image = body1_images["turn_downleft"]
                            elif (dx1,dy1) == (0, -1) and (dx2,dy2) == (-1, 0):  #lên -> trái
                                body1_image = body1_images["turn_downright"]
                            elif (dx1,dy1) == (0, 1) and (dx2,dy2) == (1, 0):  #xuống -> phải
                                body1_image = body1_images["turn_upleft"]
                            elif (dx1,dy1) == (0, 1) and (dx2,dy2) == (-1, 0):  #xuống -> trái
                                body1_image = body1_images["turn_upright"]
                        # Vẽ hình ảnh thân
                        display.blit(body1_image, (curr1_segment[0] * 15, curr1_segment[1] * 15))
                # Vẽ đầu và đuôi rắn 1
                snake_head_rect = display.blit(head1_images[direct], (snakes[-1][0] * 15, snakes[-1][1] * 15))
                # Ran dam dau vao tuong chet
                if snakes[-1][0] <= -1 or snakes[-1][0] >= WIDTH // 15 or snakes[-1][-1] <= -1 or snakes[-1][-1] >= HEIGHT // 15:
                        pygame.mixer.music.pause()
                        stop = True
                # Rắn tự đụng chính mình
                for i in range(len(snakes) - 1):
                    body1_rect = pygame.Rect(snakes[i][0] * 15, snakes[i][1] * 15, 15, 15)
                    if snake_head_rect.colliderect(body1_rect):
                        pygame.mixer.music.pause()
                        stop = True
                # Ran dam vao dai bang
                if eagle_rect.colliderect(snake_head_rect) or lung_rect.colliderect(snake_head_rect) or lung2_rect.colliderect(snake_head_rect):
                     pygame.mixer.music.pause()
                     stop = True
                for segment in snakes[:-1]:
                    snake_body_rect = pygame.Rect(segment[0]*15, segment[1]*15,15,15)
                    if eagle_rect.colliderect(snake_body_rect) or lung_rect.colliderect(snake_body_rect) or lung2_rect.colliderect(snake_body_rect):
                         pygame.mixer.music.pause()
                         stop = True
                # Hiển thị điểm
                display.blit(font.render("Your score: " + str(scorepl1), True, WHITE), (10, 10))
                #In ra thong bao khi con ran chet
                if stop:
                    if scorepl1 > high_score_pl1:
                        high_score_pl1 = scorepl1
                        high_scores["player1"] = high_score_pl1
                        save_high_scores(high_scores)
                    text_gameover = font.render("You are loser" , True, RED)
                    text_scorepl1 = font.render("Your score: " + str(scorepl1), True, WHITE)
                    text_high_score_pl1 = font.render("High score: " + str(high_score_pl1), True, WHITE)
                    text_presSpace = font.render("Press Space to continue", True, WHITE)
                    display.blit(text_gameover, (WIDTH // 2 - 165, HEIGHT // 2 - 127.5)) 
                    display.blit(text_scorepl1, (WIDTH // 2 - 120, HEIGHT // 2 - 72.5))
                    display.blit(text_high_score_pl1, (WIDTH // 2 - 120, HEIGHT // 2 -22.5))
                    display.blit(text_presSpace, (WIDTH // 2 - 260, HEIGHT // 2 + 27.5))
                    food = [WIDTH + 1000,HEIGHT + 1000]
                    chest = [WIDTH + 1000,HEIGHT + 1000]
                    food2 = [WIDTH + 1000,HEIGHT + 1000]
                    eagle_move = 0
                    lung_move = 0
                    eagle_x_pos = 0
                    lung_y_pos = 0
                    lung2_y_pos = -100
                    snakes = [[-10, 10], [-9, 10], [-8, 10]]
                    snake_speed = initial_snake_speed
                    if not sound_played:    
                        lose.play()
                        sound_played = True
            elif self.app.game_mode == "2 Player":
                # Vẽ rắn 1
                for i in range(1,len(snakes)):
                    if i == 0:  # Vẽ đầu rắn
                        display.blit(head1_images[direct], (snakes[i][0] * 15, snakes[i][1] * 15))
                    elif i == len(snakes) - 1:  # Đảm bảo có ít nhất 2 đoạn
                        tail1_segment = snakes[0]        # Đoạn đuôi
                        next_to_tail1_segment = snakes[1]  # Đoạn liền kề với đuôi
                        # Xác định hướng di chuyển của đoạn đuôi
                        dx_tail1 = next_to_tail1_segment[0] - tail1_segment[0]
                        dy_tail1 = next_to_tail1_segment[1] - tail1_segment[1]
                        # Chọn hình ảnh đuôi phù hợp
                        if dx_tail1 == 1 and dy_tail1 == 0:  # Đuôi hướng sang phải
                            tail1_image = tail1_images["right"]
                        elif dx_tail1 == -1 and dy_tail1 == 0:  # Đuôi hướng sang tráisadads
                            tail1_image = tail1_images["left"]
                        elif dy_tail1 == 1 and dx_tail1 == 0:  # Đuôi hướng xuống
                            tail1_image = tail1_images["down"]
                        elif dy_tail1 == -1 and dx_tail1 == 0:  # Đuôi hướng lên
                            tail1_image = tail1_images["up"]
                        # Vẽ đuôi
                        display.blit(tail1_image, (tail1_segment[0] * 15, tail1_segment[1] * 15))
                    else:  # Vẽ thân rắn
                        prev1_segment = snakes[i - 1]
                        curr1_segment = snakes[i]
                        next1_segment = snakes[i + 1]
                        # Tính hướng trước và sau
                        dx1, dy1 = curr1_segment[0] - prev1_segment[0], curr1_segment[1] - prev1_segment[1]
                        dx2, dy2 = next1_segment[0] - curr1_segment[0], next1_segment[1] - curr1_segment[1] 
                        # Xác định hình ảnh thân
                        if dx1 == dx2 == 0 and dy1 == dy2:  # Thân thẳng ngang
                            body1_image = body1_images["vertical"]
                        elif dy1 == dy2 == 0 and dx1 == dx2:  # Thân thẳng dọc
                            body1_image = body1_images["horizontal"]
                        else:
                            if (dx1, dy1) == (1, 0) and (dx2, dy2) == (0, -1):  # Phải -> Lên
                                body1_image = body1_images["turn_upright"]
                            elif (dx1, dy1) == (1, 0) and (dx2, dy2) == (0, 1):  # Phải -> Xuống
                                body1_image = body1_images["turn_downright"]
                            elif (dx1, dy1) == (-1, 0) and (dx2, dy2) == (0, -1):  # Trái -> Lên
                                body1_image = body1_images["turn_upleft"]
                            elif (dx1, dy1) == (-1, 0) and (dx2, dy2) == (0, 1):  # Trái -> Xuống
                                body1_image = body1_images["turn_downleft"]
                            elif (dx1,dy1) == (0, -1) and (dx2,dy2) == (1, 0):  #lên -> phải
                                body1_image = body1_images["turn_downleft"]
                            elif (dx1,dy1) == (0, -1) and (dx2,dy2) == (-1, 0):  #lên -> trái
                                body1_image = body1_images["turn_downright"]
                            elif (dx1,dy1) == (0, 1) and (dx2,dy2) == (1, 0):  #xuống -> phải
                                body1_image = body1_images["turn_upleft"]
                            elif (dx1,dy1) == (0, 1) and (dx2,dy2) == (-1, 0):  #xuống -> trái
                                body1_image = body1_images["turn_upright"]
                        # Vẽ hình ảnh thân
                        snake_body_rect = display.blit(body1_image, (curr1_segment[0] * 15, curr1_segment[1] * 15))
                # Vẽ đầu và đuôi rắn 1
                snake_head_rect = display.blit(head1_images[direct], (snakes[-1][0] * 15, snakes[-1][1] * 15))
                # Vẽ rắn 2
                for i in range(1,len(players)):
                    if i == 0:  # Vẽ đầu rắn
                        display.blit(head2_images[direction], (players[i][0] * 15, players[i][1] * 15))
                    elif i == len(players) - 1:  # Vẽ đuôi rắn
                        tail2_segment = players[0]        # Đoạn đuôi
                        next_to_tail2_segment = players[1]  # Đoạn liền kề với đuôi
                        # Xác định hướng di chuyển của đoạn đuôi
                        dx_tail2 = next_to_tail2_segment[0] - tail2_segment[0]
                        dy_tail2 = next_to_tail2_segment[1] - tail2_segment[1]
                        # Chọn hình ảnh đuôi phù hợp
                        if dx_tail2 == 1 and dy_tail2 == 0:  # Đuôi hướng sang phải
                            tail2_image = tail2_images["right"]
                        elif dx_tail2 == -1 and dy_tail2 == 0:  # Đuôi hướng sang trái
                            tail2_image = tail2_images["left"]
                        elif dy_tail2 == 1 and dx_tail2 == 0:  # Đuôi hướng xuống
                            tail2_image = tail2_images["down"]
                        elif dy_tail2 == -1 and dx_tail2 == 0:  # Đuôi hướng lên
                            tail2_image = tail2_images["up"]
                        display.blit(tail2_image, (tail2_segment[0] * 15, tail2_segment[1] * 15))
                    else:  # Vẽ thân rắn
                        prev2_segment = players[i - 1]
                        curr2_segment = players[i]
                        next2_segment = players[i + 1]
                        # Tính hướng trước và sau
                        dx3, dy3 = curr2_segment[0] - prev2_segment[0], curr2_segment[1] - prev2_segment[1]
                        dx4, dy4 = next2_segment[0] - curr2_segment[0], next2_segment[1] - curr2_segment[1]
                        # Xác định hình ảnh thân
                        if dx3 == dx4 == 0 and dy3 == dy4:  # Thân thẳng doc
                            body2_image = body2_images["vertical"]
                        elif dy3 == dy4 == 0 and dx3 == dx4:  # Thân thẳng ngang
                            body2_image = body2_images["horizontal"]
                        else:
                            if (dx3, dy3) == (1, 0) and (dx4, dy4) == (0, -1):  # Phải -> Lên
                                body2_image = body2_images["turn_upright"]
                            elif (dx3, dy3) == (1, 0) and (dx4, dy4) == (0, 1):  # Phải -> Xuống
                                body2_image = body2_images["turn_downright"]
                            elif (dx3, dy3) == (-1, 0) and (dx4, dy4) == (0, -1):  # Trái -> Lên
                                body2_image = body2_images["turn_upleft"]
                            elif (dx3, dy3) == (-1, 0) and (dx4, dy4) == (0, 1):  # Trái -> Xuống
                                body2_image = body2_images["turn_downleft"]
                            elif (dx3,dy3) == (0, -1) and (dx4,dy4) == (1, 0):  #lên -> phải
                                body2_image = body2_images["turn_downleft"]
                            elif (dx3,dy3) == (0, -1) and (dx4,dy4) == (-1, 0):  #lên -> trái
                                body2_image = body2_images["turn_downright"]
                            elif (dx3,dy3) == (0, 1) and (dx4,dy4) == (1, 0):  #xuống -> phải
                                body2_image = body2_images["turn_upleft"]
                            elif (dx3,dy3) == (0, 1) and (dx4,dy4) == (-1, 0):  #xuống -> trái
                                body2_image = body2_images["turn_upright"]
                        # Vẽ hình ảnh thân
                        player_body_rect = display.blit(body2_image, (curr2_segment[0] * 15, curr2_segment[1] * 15))
                # Vẽ đầu và đuôi rắn 2
                player_head_rect = display.blit(head2_images[direction], (players[-1][0] * 15, players[-1][1] * 15))
                # Ran dam dau vao tuong chet
                if snakes[-1][0] <= -1 or snakes[-1][0] >= WIDTH // 15 or snakes[-1][-1] <= -1 or snakes[-1][-1] >= HEIGHT // 15:
                        pygame.mixer.music.pause()
                        stop = True
                #ran 2 dam vao tuong
                if players[-1][0] <= -1 or players[-1][0] >= WIDTH // 15 or players[-1][-1] <= -1 or players[-1][-1] >= HEIGHT // 15:
                        pygame.mixer.music.pause()
                        stop = True
                #Xử lí va chạm rắn 1
                for i in range(len(snakes) - 1):
                    body1_rect = pygame.Rect(snakes[i][0] * 15, snakes[i][1] * 15, 15, 15)
                    if snake_head_rect.colliderect(body1_rect):
                        pygame.mixer.music.pause()
                        stop = True
                if eagle_rect.colliderect(snake_head_rect) or lung_rect.colliderect(snake_head_rect) or lung2_rect.colliderect(snake_head_rect):
                     pygame.mixer.music.pause()
                     stop = True
                for segment in snakes[:-1]:
                    snake_body_rect = pygame.Rect(segment[0]*15, segment[1]*15,15,15)
                    if eagle_rect.colliderect(snake_body_rect) or lung_rect.colliderect(snake_body_rect) or lung2_rect.colliderect(snake_body_rect):
                         pygame.mixer.music.pause()
                         stop = True
                #Xử lí va chạm rắn 2
                for i in range(len(players) - 1):
                    body2_rect = pygame.Rect(players[i][0] * 15, players[i][1] * 15, 15, 15)
                    if player_head_rect.colliderect(body2_rect):
                        pygame.mixer.music.pause()
                        stop = True
                if eagle_rect.colliderect(player_head_rect) or lung_rect.colliderect(player_head_rect) or lung2_rect.colliderect(player_head_rect):
                     pygame.mixer.music.pause()
                     stop = True
                for segment in players[:-1]:
                    snake_body_rect = pygame.Rect(segment[0]*15, segment[1]*15,15,15)
                    if eagle_rect.colliderect(player_body_rect) or lung_rect.colliderect(player_body_rect) or lung2_rect.colliderect(player_body_rect):
                         pygame.mixer.music.pause()
                         stop = True
                # Hiển thị điểm
                display.blit(font.render("Player 1: " + str(scorepl1), True, WHITE), (10, 10))
                display.blit(font.render("Player 2: " + str(scorepl2), True, WHITE), (WIDTH - 250, 10)) 
                #In ra thong bao khi con ran chet
                if stop:
                    if scorepl1 > high_score_pl2:
                        high_score_pl2 = scorepl1
                        high_scores["player2"] = high_score_pl2
                    elif scorepl2 > high_score_pl3:
                        high_score_pl3 = scorepl2
                        high_scores["player3"] = high_score_pl3
                    save_high_scores(high_scores)
                    text_gameover = font.render("You are loser" , True, RED)
                    text_scorepl1 = font.render("Player 1: " + str(scorepl1), True, WHITE)
                    text_high_score_pl2 = font.render("High score pl1: " + str(high_score_pl2), True, WHITE)
                    text_scorepl2 = font.render("Player 2: " + str(scorepl2), True, WHITE)
                    text_high_score_pl3 = font.render("High score pl2: " + str(high_score_pl3), True, WHITE)
                    text_presSpace = font.render("Press Space to continue", True, WHITE)
                    display.blit(text_gameover, (WIDTH // 2 - 165, HEIGHT // 2 - 77.5)) 
                    display.blit(text_scorepl1, (WIDTH // 2 - 120, HEIGHT // 2 - 22.5))
                    display.blit(text_high_score_pl2, (WIDTH // 2 - 120, HEIGHT // 2 + 27.5))
                    display.blit(text_scorepl2, (WIDTH // 2 - 120, HEIGHT // 2 + 77.5))
                    display.blit(text_high_score_pl3, (WIDTH // 2 - 120, HEIGHT // 2 + 127.5))
                    display.blit(text_presSpace, (WIDTH // 2 - 260, HEIGHT // 2 + 177.5))
                    eagle_move = 0
                    lung_move = 0
                    eagle_x_pos = 0
                    lung_y_pos = 0
                    lung2_y_pos = -100
                    food = [WIDTH + 1000,HEIGHT + 1000]
                    chest = [WIDTH + 1000,HEIGHT + 1000]
                    food2 = [WIDTH + 1000,HEIGHT + 1000]
                    snakes = [[-10, 10], [-9, 10], [-8, 10]]
                    players = [[WIDTH // 15 + 10, 40], [WIDTH // 15 + 9, 40], [WIDTH // 15 + 8, 40]]
                    if not sound_played:    
                        lose.play()
                        sound_played = True
            # Vẽ thức ăn
            display.blit(food_img, (food[0] * 15,food[1] * 15))
            #khi dung game
            if game_pause:
                overlay = pygame.Surface((WIDTH,HEIGHT))
                overlay.set_alpha(140)
                overlay.fill((0, 0, 0))
                display.blit(overlay, (0, 0))
                display.blit(resume_img, (WIDTH // 2, 10))
                display.blit(reboot_img, (WIDTH // 2 - 100,HEIGHT // 2))
                display.blit(setting_img, (WIDTH // 2 - 15,HEIGHT // 2))
                display.blit(home_img, (WIDTH // 2 + 70,HEIGHT // 2))
                eagle_move = 0
                lung_move = 0
            else:
                if scorepl1 % 5 == 0 and scorepl1 != 0 and food2 is None:
                    food2= [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                    food2_timer = time.time()
                elif scorepl2 % 5 == 0 and scorepl2 != 0 and food2 is None:
                    food2= [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                    food2_timer = time.time()
                if food2 and time.time() - food2_timer > 5:
                    food2 = None
                display.blit(food_img, (food[0] * 15,food[1] * 15))
                if food2:
                    display.blit(food2_img, (food2[0] * 15,food2[1] * 15))
                display.blit(pause_img, (WIDTH // 2, 10))
                if scorepl1 % 10 == 0 and scorepl1 != 0:
                    if not reduced_for_pl1:
                        snake_speed = max(snake_speed - 0.01, 0.001)
                        reduced_for_pl1 = True
                elif scorepl2 % 10 == 0 and scorepl2 != 0:
                    if not reduced_for_pl2:
                        snake_speed = max(snake_speed - 0.01, 0.001)
                        reduced_for_pl2 = True
            #khi an cai dat
            if game_setting:
                overlay2 = pygame.Surface((WIDTH // 2 + 50, HEIGHT // 2 - 22.5))
                overlay2.set_alpha(1000)
                overlay2.fill((173, 255, 0))
                display.blit(overlay2, (WIDTH // 2 - 400, HEIGHT // 2 - 188.5))
                display.blit(back_img, (WIDTH // 2 - 375, HEIGHT // 2 + 188.5))
                music_slider.draw()
                sound_slider.draw()
                music_slider.update()
                sound_slider.update()
            #thiet lap con ran di chuyen
            if stop == game_pause == False:
                if direct == "up":
                    snakes.append([snakes[-1][0], snakes[-1][1] - 1])
                    snakes.pop(0)
                elif direct == "down":
                    snakes.append([snakes[-1][0], snakes[-1][1] + 1])
                    snakes.pop(0)
                elif direct == "left":
                    snakes.append([snakes[-1][0] - 1, snakes[-1][1]])
                    snakes.pop(0)
                elif direct == "right":
                    snakes.append([snakes[-1][0] + 1, snakes[-1][1]])
                    snakes.pop(0)
                eagle_move = DifficultySettings.current0_settings["eagle_speed"]
                lung_move = DifficultySettings.current0_settings["lung_speed"]
            time.sleep(snake_speed)
            #thiet lap ran 2 di chuyen
            if stop == game_pause == False:
                if direction == "up":
                    players.append([players[-1][0], players[-1][1] - 1])
                    players.pop(0)
                elif direction == "down":
                    players.append([players[-1][0], players[-1][1] + 1])
                    players.pop(0)
                elif direction == "left":
                    players.append([players[-1][0] - 1, players[-1][1]])
                    players.pop(0)
                elif direction == "right":
                    players.append([players[-1][0] + 1, players[-1][1]])
                    players.pop(0)
                eagle_move = DifficultySettings.current0_settings["eagle_speed"]
                lung_move = DifficultySettings.current0_settings["lung_speed"]
            time.sleep(snake_speed)
            # Kiểm tra va chạm với thức ăn
            if snakes[-1][0] == food[0] and snakes[-1][1] == food[1]:
                snakes.insert(0, [snakes[0][0], snakes[0][1]])
                eat.play()
                food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                scorepl1 += 1
            if food2 is not None and snakes[-1][0] == food2[0] and snakes[-1][1] == food2[1]:
                snakes.insert(0, [snakes[0][0], snakes[0][1]])
                eat.play()
                food2 = None
                scorepl1 += 2
            if players[-1][0] == food[0] and players[-1][1] == food[1]:
                players.insert(0, [players[0][0], players[0][1]])
                eat.play()
                food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                scorepl2 += 1
            if food2 is not None and players[-1][0] == food2[0] and players[-1][1] == food2[1]:
                players.insert(0, [players[0][0], players[0][1]])
                eat.play()
                food2 = None
                scorepl2 += 2
            # Xử lý sự kiện
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and direct != "down":
                        direct = "up"
                    elif event.key == pygame.K_s and direct != "up":
                        direct = "down"
                    elif event.key == pygame.K_a and direct != "right":
                        direct = "left"
                    elif event.key == pygame.K_d and direct != "left":
                        direct = "right" 
                    if event.key == pygame.K_UP and direction != "down":
                        direction = "up"
                    elif event.key == pygame.K_DOWN and direction != "up":
                        direction = "down"
                    elif event.key == pygame.K_LEFT and direction != "right":
                        direction = "left"
                    elif event.key == pygame.K_RIGHT and direction != "left":
                        direction = "right"  
                    elif event.key == pygame.K_SPACE and stop == True:
                        stop = False
                        scorepl1 = 0
                        scorepl2 = 0
                        snakes = [[5, 10], [6, 10], [7, 10]]
                        players = [[WIDTH // 15 - 5, HEIGHT // 15 - 10], [WIDTH // 15 - 6, HEIGHT // 15 - 10], [WIDTH // 15 - 7, HEIGHT // 15 - 10]]
                        direct = "right"
                        direction = "left"   
                        food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                        pygame.mixer.music.play()
                        lose.stop()
                        sound_played = False
                        eagle_x_pos = 0
                        lung_y_pos = 0
                        lung2_y_pos = -300
                        reduced_for_pl1 = False
                        reduced_for_pl2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pause_button_rect.collidepoint(event.pos) and not game_pause:
                        game_pause = True
                        pygame.mixer.music.pause()
                        eagle_move = 0
                    elif resume_button_rect.collidepoint(event.pos) and game_pause:
                        game_pause = False
                        game_setting = False
                        pygame.mixer.music.unpause()
                        eagle_move = 0
                        reboot_button_rect = pygame.Rect(WIDTH //2 - 100, HEIGHT // 2, reboot_img.get_width(), reboot_img.get_height())
                        setting_button_rect = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2, setting_img.get_width(), setting_img.get_height())
                        home_button_rect = pygame.Rect(WIDTH // 2 + 70, HEIGHT // 2, home_img.get_width(), home_img.get_height())
                    elif reboot_button_rect and reboot_button_rect.collidepoint(event.pos) and game_pause:
                        stop = False
                        scorepl1 = 0
                        scorepl2 = 0
                        snakes = [[5, 10], [6, 10], [7, 10]]
                        players = [[WIDTH // 15 - 5, HEIGHT // 15 - 10], [WIDTH // 15 - 6, HEIGHT // 15 - 10], [WIDTH // 15 - 7, HEIGHT // 15 - 10]]
                        direct = "right"
                        direction = "left"   
                        food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                        pygame.mixer.music.play()
                        lose.stop()
                        sound_played = False 
                        eagle_x_pos = 0
                        lung_y_pos = 0
                        lung2_y_pos = -200
                    elif home_button_rect and home_button_rect.collidepoint(event.pos) and game_pause: 
                        self.scene = Menu.HOME
                        stop = False
                        scorepl1 = 0
                        scorepl2 = 0
                        snakes = [[5, 10], [6, 10], [7, 10]]
                        players = [[WIDTH // 15 - 5, HEIGHT // 15 - 10], [WIDTH // 15 - 6, HEIGHT // 15 - 10], [WIDTH // 15 - 7, HEIGHT // 15 - 10]]
                        direct = "right"
                        direction = "left"   
                        food = [randint(1,WIDTH // 15 - 2), randint(1,HEIGHT // 15 - 2)]
                        pygame.mixer.music.play()
                        lose.stop()
                        sound_played = False 
                        eagle_x_pos = 0
                        lung_y_pos = 0
                        lung2_y_pos = -200
                        pygame.mixer.music.play()
                        return  
                    elif setting_button_rect and setting_button_rect.collidepoint(event.pos) and game_pause:
                        game_setting = True
                        reboot_button_rect = None
                        home_button_rect = None
                        setting_button_rect = None
                    elif back_button_rect and back_button_rect.collidepoint(event.pos) and game_pause:
                        game_setting = False
                        reboot_button_rect = pygame.Rect(WIDTH //2 - 100, HEIGHT // 2, reboot_img.get_width(), reboot_img.get_height())
                        setting_button_rect = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2, setting_img.get_width(), setting_img.get_height())
                        home_button_rect = pygame.Rect(WIDTH // 2 + 70, HEIGHT // 2, home_img.get_width(), home_img.get_height())
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                music_slider.eventHandling(event)
                sound_slider.eventHandling(event)
            pygame.display.flip()
    def draw(self):
        if self.scene == Menu.OPTIONS:
            self.surface.blit(self.theme, (0, 0))
        elif self.scene == Menu.INSTRUCT:
            self.surface.blit(self.theme, (0, 0))
        for component in self.UIComponents[self.scene]:
            component.draw()
    def update(self):
        for component in self.UIComponents[self.scene]:
            component.update()
    def eventHandling(self, e):
        for component in self.UIComponents[self.scene]:
            component.eventHandling(e)
    def changeHomeScene(self):
        self.scene = Menu.HOME
    def changeOptionScene(self):
        self.scene = Menu.OPTIONS
    @classmethod
    def quit(cls):
        pygame.quit()
        sys.exit(0)
class Text(UIComponent):
    def __init__(self, app, text: str, color=WHITE, pos: tuple[int, int] = (WIDTH // 2, HEIGHT // 2),
                 font="SupportSports-E4Xvl.ttf", size: int = 40, topleft=False):
        super().__init__(app)
        self.text = text
        self.color = color
        self.pos = pos
        self.font = pygame.font.Font(font, size)
        self.text_surf = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surf.get_rect()
        if topleft:
            self.text_rect.topleft = pos
        else:
            self.text_rect.center = pos
    def draw(self):
        self.surface.blit(self.text_surf, self.text_rect)
    def getRect(self):
        return self.text_rect
class Button(UIComponent):
    def __init__(self, app, pos: tuple[int, int], text: str, size: tuple[int, int] = (200, 60),
                 font_size: int = 60, onclick=None, topleft=False):
        super().__init__(app)
        self.functions = onclick
        self.w = size[0]
        self.h = size[1]
        self.x = pos[0] - self.w // 2 if not topleft else pos[0]
        self.y = pos[1] - self.h // 2 if not topleft else pos[1]
        self.hover_active = False
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.hover_rect = pygame.Rect(self.x - 5, self.y - 5, self.w + 10, self.h + 10)
        self.text = Text(self.app, text, pos=self.rect.center, size=font_size)
        self.hover_text = Text(self.app, text, pos=self.rect.center, size=font_size + 5)
    def update(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            self.hover_active = True
        else:
            self.hover_active = False
    def draw(self):
        if self.hover_active:
            pygame.draw.rect(self.surface, WHITE, self.hover_rect, 2, 20)
            self.hover_text.draw()
        else:
            pygame.draw.rect(self.surface, WHITE, self.rect, 2, 20)
            self.text.draw()
    def eventHandling(self, e):
        if e.type == pygame.MOUSEBUTTONUP:
            if self.hover_rect.collidepoint(pygame.mouse.get_pos()):
                for function in self.functions:
                    function()
class SliderSetting(UIComponent):
    def __init__(self, app, text, pos, offset=150, value=50, is_music=True):
        super().__init__(app)
        self.text = Text(app, text, pos=pos, size=30, topleft=True)
        self.start = pos[0] + offset
        self.width = 300
        self.end = self.start + self.width
        self.bar = pygame.Rect(self.start, pos[1] + 12, self.width, 10)
        self.rod = pygame.Rect(self.start + value * self.width / 100, pos[1] + 1, 10, 30)
        self.pressed = False
        self.is_music = is_music
    def update(self):
        x, y = mx, my = pygame.mouse.get_pos()
        if self.pressed:
            if mx < self.start:
                x = self.start
            elif mx > self.end - self.rod.width:
                x = self.end - self.rod.width
            self.rod.x = x
            #Tinh toan am luong tuong ung
            value = (self.rod.x - self.start) / self.width * 100
            if self.is_music:
                pygame.mixer.music.set_volume(value/100)
            else:
                eat.set_volume(value/100)
                lose.set_volume(value/100)
                ruong.set_volume(value/100)
    def draw(self):
        self.text.draw()
        pygame.draw.rect(self.surface, COLOR, self.bar)
        pygame.draw.rect(self.surface, "#27b8b3", self.rod)
    def eventHandling(self, e):
        mouse = pygame.mouse.get_pos()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.bar.collidepoint(mouse) or self.rod.collidepoint(mouse):
                self.pressed = True
        if e.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
class ToggleSetting(UIComponent):
    def __init__(self, app, text, options, pos, offset):
        super().__init__(app)
        self.text = Text(app, text, pos=pos, size=30, topleft=True)
        self.rect = pygame.Rect(pos[0] + offset, pos[1] + 3, 150, 30)
        self.left = pygame.transform.scale(pygame.image.load('left-arrow.png').convert_alpha(), (24, 24))
        self.left_rect = self.left.get_rect()
        self.left_rect.topleft = (self.rect.left - 24, self.rect.top)
        self.right = pygame.transform.scale(pygame.image.load('right-arrow.png').convert_alpha(), (24, 24))
        self.right_rect = self.right.get_rect()
        self.right_rect.topleft = (self.rect.right, self.rect.top)
        self.options = [
            Text(app, opt, WHITE, self.rect.center, size=25) for opt in options
        ]
        self.current = 0
        self.current1 = 0
    def eventHandling(self, e):
        global WIDTH, HEIGHT
        mouse = pygame.mouse.get_pos()
        original_width = 1500  
        original_height = 755
        if e.type == pygame.MOUSEBUTTONUP:
            if self.left_rect.collidepoint(mouse):
                self.current = (self.current + len(self.options) - 1) % len(self.options)
            elif self.right_rect.collidepoint(mouse):
                self.current = (self.current + 1) % len(self.options)
            #cap nhat cau hinh tro choi khi lua chon thay doi
            if self.text.text == "Choose difficulty":
                if self.options[self.current].text == "Easy":
                    DifficultySettings.current0_settings = DifficultySettings.EASY
                elif self.options[self.current].text == "Normal":
                    DifficultySettings.current0_settings = DifficultySettings.NORMAL
                elif self.options[self.current].text == "Hard":
                    DifficultySettings.current0_settings = DifficultySettings.HARD
                elif self.options[self.current].text == "Insane":
                    DifficultySettings.current0_settings = DifficultySettings.INSANE
                elif self.options[self.current].text == "Impossible":
                    DifficultySettings.current0_settings = DifficultySettings.IMPOSSIBLE
            elif self.text.text == "Game mode":
                if self.options[self.current].text == "1  Player":
                    self.app.game_mode = "1 Player"
                elif self.options[self.current].text == "2  Player":
                    self.app.game_mode = "2 Player"
            elif self.text.text == "Background":
                if self.options[self.current].text == "Bgr1":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr1
                elif self.options[self.current].text == "Bgr2":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr2
                elif self.options[self.current].text == "Bgr3":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr3
                elif self.options[self.current].text == "Bgr4":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr4
                elif self.options[self.current].text == "Bgr5":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr5
                elif self.options[self.current].text == "Bgr6":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr6
                elif self.options[self.current].text == "Bgr7":
                    Backgroundsettings.current1_settings = Backgroundsettings.Bgr7
            elif self.text.text == "Sound":
                if self.options[self.current].text == "Sound1":
                    Soundsettings.current2_setting = Soundsettings.Sound1
                elif self.options[self.current].text == "Sound2":
                    Soundsettings.current2_setting = Soundsettings.Sound2
                elif self.options[self.current].text == "Sound3":
                    Soundsettings.current2_setting = Soundsettings.Sound3
                elif self.options[self.current].text == "Sound4":
                    Soundsettings.current2_setting = Soundsettings.Sound4
            elif self.text.text == "Display mode":
                if self.options[self.current].text == "Windowed":
                    pygame.display.set_mode((original_width, original_height), pygame.RESIZABLE)
                    WIDTH, HEIGHT = original_width, original_height
                elif self.options[self.current].text == "Fullscreen":
                    screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
                    WIDTH, HEIGHT = screen_width, screen_height
                    pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
                elif self.options[self.current].text == "Borderless":
                    pygame.display.set_mode((original_width, original_height), pygame.NOFRAME)
                    WIDTH, HEIGHT = original_width, original_height
    def draw(self):
        self.text.draw()
        self.surface.blit(self.left, self.left_rect)
        self.surface.blit(self.right, self.right_rect)
        self.options[self.current].draw()