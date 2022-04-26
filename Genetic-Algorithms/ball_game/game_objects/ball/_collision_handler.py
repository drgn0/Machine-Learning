from pygame.sprite import spritecollide 


class CollisionHandler:
    def __init__(self, parent):
        self.parent = parent 

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
            balls = self.parent.get_alive_balls() 
            for ball in spritecollide(obstacle, balls, dokill = False):
                balls.remove(ball) 
                
    
    def collision_with_walls(self):
        for wall in self.walls:
            balls = self.parent.get_alive_balls() 
            for ball in spritecollide(wall, balls, dokill = False):
                balls.remove(ball) 
    
    def collision_with_ground(self):
        for ball in spritecollide(self.ground, self.parent.get_alive_balls(), dokill = False):
            ball.jump() 
    