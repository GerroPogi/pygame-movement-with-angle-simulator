import pygame,numpy
pygame.init()
class Player:
    speed=1
    angle=0.0
    directions=pygame.Vector2()
    keys=pygame.key.get_pressed()
    position=(300,300)
    #Picture angle
    pangle=0
    def __init__(self):
        # Define and resize picture
        self.picture=self.picture2=pygame.transform.scale(pygame.image.load("arrow.png"),numpy.divide(pygame.image.load("arrow.png").get_size(),3)).convert_alpha()
        # Get the surface
        self.win=pygame.display.get_surface()
    def run(self):
        self.keys=pygame.key.get_pressed()
        # Input handling
        if self.keys[pygame.K_SPACE]:
            self.directions=self.defineDirection(self.angle)
        else:
            self.directions.x=0
            self.directions.y=0
        if self.keys[pygame.K_RIGHT]:
            self.angle-=1
            self.pangle-=1
        elif self.keys[pygame.K_LEFT]:
            self.angle+=1
            self.pangle+=1
        if self.directions.magnitude()!=0:
            self.directions=self.directions.normalize()
        self.pangle=self.pangle if self.pangle<180 or self.pangle>-180 else self.pangle-180 if self.pangle>180 else self.pangle+180
        self.turn(self.pangle)
        self.position+=self.directions
        self.move(self.picture2,self.position2)
    # Turning image function with self.picture2 the rotated picture and self.position2 readjusting it to be at the center.
    def turn(self,angle):
        self.picture2=pygame.transform.rotate(self.picture,angle)
        self.position2=self.picture2.get_rect(center=self.position)
    def move(self,surface:pygame.Surface,pos:tuple):
        self.win.blit(surface, pos)
    # Moving sprite according to angle
    def defineDirection(self, angle:float):
        # Finding the x side or adjacent side of the triangle to make it move according to angle.
        # Also checks if angle exceeds the Y axis, if so, then positive, otherwise negative.
        adjacent=self.speed if 180>=self.normalize_angle(angle+90)>=0 else -self.speed
        # After finding the value of the adjacent, using the formula of finding the y or opposite:
        # We use the formula a=tan(theta)*adjacent
        opposite=numpy.tan(numpy.radians(angle))*-adjacent
        # Returns Vector2 object to add to the current position
        return pygame.Vector2(adjacent,opposite)
    # Function that gives the angle standard form ex: -1 so 359, -90 so 270, 420 so 60
    def normalize_angle(self, angle:float)-> float:
        if angle>360:
            return self.normalize_angle(angle-360)
        elif angle<0:
            return self.normalize_angle(angle+360)
        return angle

# Main fucntion

def main():
    WIDTH,HEIGHT=1000,600
    win=pygame.display.set_mode((WIDTH,HEIGHT))
    run=True
    player=Player()
    clock=pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        win.fill((100,100,100))
        player.run()
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()
