GRAVITY = 0.2 

def update_ball(ball):
    # updates velocity and position of a ball 
    ball.velocity.y += GRAVITY 
    ball.rect.move_ip(ball.velocity)

def apply_impulse(ball, impulse):
    ball.velocity.x += impulse.x 
    ball.velocity.y -= impulse.y  # bcz direction is opposite 



