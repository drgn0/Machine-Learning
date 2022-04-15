from pygame.sprite import spritecollide 


class CollisionHandler:
    def __init__(self, balls):
        self.balls = balls 

        import GameData 
        self.ground = GameData.get_ground()  
        self.obstacles = GameData.get_obstacles() 
        self.walls = GameData.get_walls() 
    
    def update(self):
        self.collision_with_obstacles() 
        self.collision_with_walls() 

        self.collision_with_ground() 

    def collision_with_obstacles(self):
        for obstacle in self.obstacles:
            spritecollide(obstacle, self.balls, dokill = True) 
    
    def collision_with_walls(self):
        for wall in self.walls:
            spritecollide(wall, self.balls, dokill = True) 
    
    def collision_with_ground(self):
        for ball in spritecollide(self.ground, self.balls, dokill = False):
            ball.jump() 
    