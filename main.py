from turtle import Screen
from player import Player
from barriers import Barriers
from invaders import Invaders
from projectiles import Projectiles
from scoreboard import ScoreBoard
import time

ENEMY_SHOT_FREQ = [20, 10, 5]

screen = Screen()
screen.title("Space Invaders")
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.colormode(255)
screen.tracer(0)

player = Player()
barriers = Barriers()
invaders = Invaders()
projectiles = Projectiles(player, invaders)
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(fun=player.move_left, key="Left")
screen.onkeypress(fun=player.move_right, key="Right")
screen.onkey(fun=projectiles.player_shoot, key="space")

loops = 0
game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    loops += 1

    scoreboard.update_score()

    # Win and Lose Conditions
    if len(invaders.invaders) == 0:
        scoreboard.is_winning()
        game_over = True

    if scoreboard.lives < 1 or invaders.is_invaded():
        scoreboard.game_over()
        game_over = True

    # Determines the amount of missiles Invaders fire and missile movement
    if loops <= 150:
        if loops % ENEMY_SHOT_FREQ[0] == 0:
            projectiles.invader_shoot()
    elif loops <= 300:
        if loops % ENEMY_SHOT_FREQ[1] == 0:
            projectiles.invader_shoot()
    else:
        if loops % ENEMY_SHOT_FREQ[2] == 0:
            projectiles.invader_shoot()
    projectiles.move_missile()

    # Default to move right unless direction is changed from bump wall function
    if invaders.direction == "right":
        invaders.move_right()
    else:
        invaders.move_left()

    # Detects if invaders bump into the right or left wall
    if invaders.bump_right_wall():
        invaders.direction = "left"
    elif invaders.bump_left_wall():
        invaders.direction = "right"

    # Detects if Player or Invader Missiles Hit Barrier
    for barrier in barriers.barriers:
        for player_shot in projectiles.player_missiles:
            if barrier.distance(player_shot) < 15:
                projectiles.hit_target(player_shot)
                barriers.destroy_barrier(barrier)
        for invader_shot in projectiles.invader_missiles:
            if barrier.distance(invader_shot) < 15:
                projectiles.hit_target(invader_shot)
                barriers.destroy_barrier(barrier)

    # Detects if Player is Hit by Invader Missiles
    for shot in projectiles.invader_missiles:
        if player.distance(shot) < 15:
            scoreboard.lives -= 1
            player.reset_pos()
            projectiles.hit_target(shot)

    # Detects if Invader is Hit by Player Missiles
    for shot in projectiles.player_missiles:
        for invader in invaders.invaders:
            if shot.distance(invader) < 15:
                scoreboard.score += 30
                invaders.invader_destroyed(invader)
                projectiles.hit_target(shot)

    # Detects if Player and Invader Missiles Collide
    for player_shot in projectiles.player_missiles:
        for invader_shot in projectiles.invader_missiles:
            if player_shot.distance(invader_shot) < 10:
                projectiles.hit_target(player_shot)
                projectiles.hit_target(invader_shot)

screen.exitonclick()
