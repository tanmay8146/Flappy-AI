from tools import *
from flappy import *
import pygame

clearScreen()
print("Flappy-AI :: running on- "+showOS())
print("Developer :: "+devInfo())

bird = Bird(230, 350)
base = Base(730)
pipes = [Pipe(730)]

win = pygame.display.set_mode((GWIN_WIDTH, GWIN_HEIGHT))
clock = pygame.time.Clock()

score = 0       #Initial Score
run = True      #Initial State of Flappy

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    rem = []
    add_pipe = False
    for pipe in pipes:
        if pipe.collide(bird):
            pass
        if pipe.x + pipe.PIPE_TOP.get_width() < 0:
            rem.append(pipe)
        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            add_pipe = True
        pipe.move()

    if add_pipe:
        score += 1
        pipes.append(Pipe(600))
        pipe.move()
        print("current score: "+str(score))

    for r in rem:
        pipes.remove(r)

    if bird.y + bird.img.get_height() >= 730:
        pass
    base.move()
    draw_win(win, bird, pipes, base)
pygame.quit()
quit()