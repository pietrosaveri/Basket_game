import pygame
import random
import math

# Window size
WINDOW_WIDTH  =1000
WINDOW_HEIGHT = 400
FPS           = 60

# background colours
INKY_GREY    = ( 128, 128, 128 )

# milliseconds since start
NOW_MS = 0

class ProjectileSprite( pygame.sprite.Sprite ):
    GRAVITY = -9.8  

    def __init__( self, bitmap, velocity=0, angle=0 ):
        pygame.sprite.Sprite.__init__( self )
        self.image       = bitmap
        self.rect        = bitmap.get_rect()
        self.start_x     = WINDOW_WIDTH // 2
        self.start_y     = WINDOW_HEIGHT - self.rect.height
        self.rect.center = ( ( self.start_x, self.start_y ) )
        # Physics
        self.setInitialVelocityRadians( velocity, angle )

    def setInitialVelocityRadians( self, velocity, angle_rads ):
        global NOW_MS
        self.start_time = NOW_MS
        self.velocity   = velocity
        self.angle      = angle_rads 

    def update( self ):
        global NOW_MS
        if ( self.velocity > 0 ):
            time_change = ( NOW_MS - self.start_time ) / 150.0  # Should be 1000, but 100 looks better
            if ( time_change > 0 ):

                # re-calcualte the velocity
                half_gravity_time_squared = self.GRAVITY * time_change * time_change / 2.0
                displacement_x = self.velocity * math.sin(self.angle) * time_change 
                displacement_y = self.velocity * math.cos(self.angle) * time_change + half_gravity_time_squared

                # reposition sprite
                self.rect.center = ( ( self.start_x + int( displacement_x ), self.start_y - int( displacement_y ) ) )

                # Stop at the bottom of the window
                if ( self.rect.y >= WINDOW_HEIGHT - self.rect.height ):
                    self.rect.y = WINDOW_HEIGHT - self.rect.height
                    self.velocity = 0
                    #self.kill()

### MAIN
pygame.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
WINDOW  = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), SURFACE )
pygame.display.set_caption("Projectile Motion Example")

# Load resource image(s)
sprite_image = pygame.image.load( "Padnp.png" )#.convert_alpha()

# Make some sprites 
NOW_MS = pygame.time.get_ticks()
SPRITES = pygame.sprite.Group()   
for i in range( 20 ):
    speed = random.randrange( 10, 50 )
    angle = math.radians( random.randrange( -45, 45 ) )
    new_sprite = ProjectileSprite( sprite_image, speed, angle )
    SPRITES.add( new_sprite )


clock = pygame.time.Clock()
done  = False
while not done:
    NOW_MS = pygame.time.get_ticks()

    # Handle user-input
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            done = True
        elif ( event.type == pygame.KEYDOWN ):
            if ( event.unicode == '+' or event.scancode == pygame.K_PLUS ):
                # Pressing '+' adds a new projectile sprite
                speed = random.randrange( 10,100 )
                angle = math.radians( random.randrange( -45, 45 ) )
                new_sprite = ProjectileSprite( sprite_image, speed, angle )
                SPRITES.add( new_sprite )
            if event.key == pygame.K_n:
                for s in SPRITES:
                    s.start_time = NOW_MS
                    s.velocity = random.randrange( 10, 50 )

    # Handle continuous-keypresses
    keys = pygame.key.get_pressed()
    if ( keys[pygame.K_ESCAPE] ):
        # [Esc] exits too
        done = True

    # Repaint the screen
    WINDOW.fill( INKY_GREY )
    SPRITES.update()          # re-position the sprites
    SPRITES.draw( WINDOW )    # draw the sprites

    pygame.display.flip()
    # Update the window, but not more than 60fps
    clock.tick_busy_loop( FPS )

pygame.quit()