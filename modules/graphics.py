import pygame
import modules.screen as m_scrm


#
#WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
#KVADRAT=(0, 235, 255)
screen=m_scrm.screen
#

font = pygame.font.SysFont('Arial', 30)

objects = []
class Button():
    def __init__(self, x, y, width=70, height=70, buttonText='', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False

        self.fillColors = {
            'normal':'#00CCFF',
            'hover': '#3399CC',
            'pressed': '#003399',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
def myFunction():
    print('Button Pressed')
# (332,323) pos[0], pos[1] 
pygame . init()
def graphics():


    pygame.draw.circle(
        surface=screen,
        color=(0, 100, 150),
        center=(300, 300),
        radius=200
    )
    pygame.draw.circle(
        surface=screen,
        color=BLACK,
        center=(300, 300),
        radius=200,
        width=5
    )
    pygame.draw.circle(
        surface=screen,
        color=(0, 150, 200),
        center=(300, 275),
        radius=200
    )
    pygame.draw.circle(
        surface=screen,
        color=BLACK,
        center=(300, 275),
        radius=200,
        width=5
    )
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        rect=(150, 125, 300, 300),
        border_radius=5
        )
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(150, 125, 300, 300),
        border_radius=5
        )          
    Button(x =170, y=145)
    Button(x =265, y=145)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(265, 145, 70, 70),
        border_radius=5
        )           
    Button(x =360, y=145)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(360, 145, 70, 70),
        border_radius=5
    )            
    Button(x =170, y=235)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(170, 235, 70, 70),
        border_radius=5
        )            
    Button(x =265, y=235)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(265, 235, 70, 70),
        border_radius=5
        )     
    Button(x =360, y=235)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(360, 235, 70, 70),
        border_radius=5
    )
    Button(x =170, y=330)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(170, 330, 70, 70),
        border_radius=5
        )    
    Button(x =265, y=330)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(265, 330, 70, 70),
        border_radius=5
        )  
    Button(x =360, y=330)
    pygame.draw.rect(
        surface=screen,
        color=BLACK,
        width=5,
        rect=(360, 330, 70, 70),
        border_radius=5
        ) 



def reset():
    global screen
    pygame.draw.rect(
        surface=screen,
        color=(0,100,205),
        rect=(250,500,100,70),
        border_radius=5
    )
    pygame.draw.rect(
        surface=screen,
        color=(0,0,0),
        rect=(250,500,100,70),
        border_radius=5,
        width=5
    )
    text1 = font.render('Reset',True,(0,0,0))
    screen.blit(text1,(260,515))
    
pygame.init()

# game = True

# while game:

#     screen.fill((0, 0, 205))

#     #Button(x =100, y=100, onclickFunction= myFunction,buttonText='0',onePress= True)
#     # graphics()

#     print("5")
#     #m_O.O.blit_sprit(window_game= screen)
#     #m_X.X.blit_sprit(window_game= screen)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             graphics(pygame.mouse.get_pos())
#     for object in objects:
#         object.process()
#     pygame.display.flip()





