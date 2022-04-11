from pygame.sprite import Group 

def get_factory():
    from ._obstacle_factory import ObstacleFactory
    return ObstacleFactory() 



'''
Classes having access to ObstacleHandler.obstacles Group:
    CollisionHandler 
    NetworkHandler 
(only read access..  (hopefully)) 


TODO:  Something called Interface Pattern  ? 

'''

class ObstacleHandler:
    factory = get_factory() 

    def __init__(self, ground):
        # takes ground as argument just to get initial position for obstacles 
        self.factory.set_initial_pos(ground.rect.topright) 

        self.obstacles = Group([])
        self.spawn_obstacle() 

    
    def get_obstacles(self):
        return self.obstacles 

    def spawn_obstacle(self):
        obstacle = self.factory.make_obstacle() 
        self.obstacles.add(obstacle)
    
    def despawn_obstacles(self):
        # despawns out of bound obstacles 
        for obstacle in self.obstacles:
            if obstacle.rect.right < 0:
                self.obstacles.remove(obstacle) 

    def update(self):
        self.obstacles.update() 

        self.despawn_obstacles()  # TODO:  you don't have to check it every frame. 
    
    def draw(self, window):
        self.obstacles.draw(window) 

