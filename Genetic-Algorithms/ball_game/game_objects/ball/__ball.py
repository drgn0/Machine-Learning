import pygame 

import game_objects.ball.Physics as Physics 





class Ball(pygame.sprite.Sprite):
    # MAX_IMPULSE = pygame.Vector2(4, 15) 
    MAX_VELOCITY = pygame.Vector2(5, 25)
    NETWORK_SIZE = (2, 4, 2) 
    def __init__(self):
        super().__init__() 

        self.jump_timer = 0  # can only jump when it's 0 

    def update(self):
        # called every frame. 
        self.update_jump_timer() 
        Physics.update_ball(self)

    def set_velocity(self, new_vel):
        self.velocity = clamp_vector2(new_vel, self.MAX_VELOCITY)
    
    def jump(self):
        if not self.can_jump():
            return 
        self.set_jump_timer() 
        
        # print('jumping.  current vel:', self.velocity) 

        desired_vel = self.network_handler.get_desired_vel() 
        self.set_velocity(desired_vel)

    def can_jump(self):
        return self.jump_timer == 0 
    
    def update_jump_timer(self):
        self.jump_timer = max(0, self.jump_timer - 1) 
    
    def set_jump_timer(self):
        # called when ball jumps 
        self.jump_timer = 5
    
        


def clamp_vector2(vector, limit):
    if isinstance(limit, int):
        limit = pygame.Vector2((limit, limit)) 
    
    return pygame.Vector2(
        clamp_int(vector.x, limit.x), 
        clamp_int(vector.y, limit.y) 
    )


def clamp_int(x, limit):
    if limit < 0:
        raise Exception
    if x > limit:
        return limit 
    if x < -limit:
        return -limit 
    return x 

