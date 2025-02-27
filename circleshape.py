import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def collides_with(self, other):
        if not isinstance(other, CircleShape): 
            return False  # Immediately return False if 'other' is not a CircleShape 
        distance = self.position.distance_to(other.position)
        combined_radius = self.radius + other.radius
        return distance <= combined_radius 
    
