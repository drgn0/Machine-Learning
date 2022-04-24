import pygame 

import game_objects.ball.Physics as Physics 


from GameData import get_score 


class Ball(pygame.sprite.Sprite):
    MAX_VELOCITY = pygame.Vector2(5, 25)
    image = pygame.image.load("Assets/ball.png").convert_alpha()
    
    def __init__(self):
        super().__init__() 

        self.score = 0 
        self.is_visible = True 
        self.is_alive = True 
        self.jump_timer = 0  # can only jump when it's 0 

    def get_network(self):
        return self.network_handler.network 
        
    def update(self):
        # called every frame. 
        if not self.is_alive:
            print('updating dead ball  ?')
            return 
        self.score = get_score() 
        self.update_jump_timer() 
        Physics.update_ball(self)

    def set_velocity(self, new_vel):
        self.velocity = clamp_vector2(new_vel, self.MAX_VELOCITY)
    
    def jump(self):
        if not self.can_jump():
            return 
        self.set_jump_timer() 
        
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

