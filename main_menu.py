#Main Menu#
import pygame
import main_game
import rps

class Button:
    def __init__(self,text,image, x, y, font, color):
        self.text_in = text
        self.font = font
        self.color = color
        self.text = self.font.render(self.text_in, True, self.color)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.text_rect = self.text.get_rect(center=(self.x,self.y))

    def buttonPosition(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode([screen_width, screen_height])
screen.fill((255,96,208))
pygame.display.set_caption("Connect 4")
font = pygame.font.Font(None,20)
clock = pygame.time.Clock()

pygame.mixer.music.load('lobby-classic-game.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

running = True

while running:

    c4_button = Button("Connect 4", pygame.image.load("button.png"), 390,395,pygame.font.SysFont("Helvetica",20), (255,255,255))

    quit_button = Button("Quit", pygame.image.load("button.png"), 390,475,pygame.font.SysFont("Helvetica",20), (255,255,255))

    buttons = [c4_button, quit_button]

    for b in buttons:
        screen.blit(b.image, b.rect)
        screen.blit(b.text ,b.text_rect)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if c4_button.buttonPosition(mouse):
                running = False
                rps.game_function()
                main_game.main()
                
            if quit_button.buttonPosition(mouse):
                running = False

        header = pygame.font.SysFont("Helvetica",100)
        text = "Connect 4"
        rule_display = header.render(text, True, (255,255,255))
        screen.blit(rule_display, (165,150))
        pygame.display.update()



