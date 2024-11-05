import pygame 

pygame.init()

width, height = 1400, 1000
wn = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo Pong")
run = True

#colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#for the ball
radius = 20
ball_x, ball_y = width/2 - radius, height/2 - radius
vel_x, vel_y = 1.0, 1.0  # Increased initial speed

#for the paddles
paddle_width, paddle_height = 30, 160
paddle_y = paddle_y1 = height/2 - paddle_height/2
paddle_x, paddle_X = 100 - paddle_width/2, width - (100 - paddle_width/2)
paddle_vel = paddle_vel1 = 0
paddle_speed = 1.5

# pontuações
score_font = pygame.font.SysFont("comicsans", 80)
player1_score = 0
player2_score = 0

def draw_scores():
    player1_text = score_font.render(f"{player1_score}", 1, WHITE)
    player2_text = score_font.render(f"{player2_score}", 1, WHITE)
    wn.blit(player1_text, (width // 4 - player1_text.get_width() // 2, 40))
    wn.blit(player2_text, (3 * width // 4 - player2_text.get_width() // 2, 40))

# loop principal do jogo
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    wn.fill(BLACK)
    draw_scores()

    #for the inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_vel = -paddle_speed
    elif keys[pygame.K_DOWN]:
        paddle_vel = paddle_speed
    else:
        paddle_vel = 0

    if keys[pygame.K_w]:
        paddle_vel1 = -paddle_speed
    elif keys[pygame.K_s]:
        paddle_vel1 = paddle_speed
    else:
        paddle_vel1 = 0

    #ball's movement controls            
    if (ball_y <= 0 + radius) or (ball_y >= height - radius):
        vel_y *= -1
    if (ball_x >= width - radius):
        player1_score += 1
        ball_x, ball_y = width/2 - radius, height/2 - radius
        vel_x, vel_y = 1.0, 1.0  # Reset to initial speed
        vel_x *= -1
    if (ball_x <= 0 + radius):
        player2_score += 1
        ball_x, ball_y = width/2 - radius, height/2 - radius
        vel_x, vel_y = 1.0, 1.0  # Reset to initial speed

    #paddle's movement controls
    if paddle_y >= height - paddle_height:
        paddle_y = height - paddle_height
    if paddle_y <= 0:
        paddle_y = 0
    if paddle_y1 >= height - paddle_height:
        paddle_y1 = height - paddle_height
    if paddle_y1 <= 0:
        paddle_y1 = 0

    if paddle_X <= ball_x <= paddle_X + paddle_width:
        if paddle_y <= ball_y <= paddle_y + paddle_height:
            ball_x = paddle_X
            vel_x *= -1
            # Increase speed on paddle hit
            vel_x = vel_x + (0.07 if vel_x > 0 else -0.07)
            vel_y = vel_y + (0.07 if vel_y > 0 else -0.07)
    
    if paddle_x <= ball_x <= paddle_x + paddle_width:
        if paddle_y1 <= ball_y <= paddle_y1 + paddle_height:
            ball_x = paddle_x + paddle_width
            vel_x *= -1
            # Increase speed on paddle hit
            vel_x = vel_x + (0.07 if vel_x > 0 else -0.07)
            vel_y = vel_y + (0.07 if vel_y > 0 else -0.07)

    #raw movements
    paddle_y += paddle_vel
    paddle_y1 += paddle_vel1
    ball_x += vel_x
    ball_y += vel_y
 
    #drawings
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(paddle_x, paddle_y1, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(paddle_X, paddle_y, paddle_width, paddle_height))

    pygame.display.update()

pygame.quit()