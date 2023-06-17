import pygame
import modules.screen as scrn




WIN = (0, 255, 0)
JUST =(255, 0, 0)



def draw_X(x=0, y=0,color=JUST):
    pygame.draw.line(
        surface=scrn.screen,
        color=color,
        start_pos=(x, y),
        end_pos=(x+70, y+70),
        width=5
    )
    pygame.draw.line(
        surface=scrn.screen,
        color=color,
        start_pos=(x+70,y),
        end_pos=(x, y+70),
        width=5
    )
def draw_O(x=0,y=0,color=JUST):
    pygame.draw.circle(
        surface= scrn.screen,
        color=color,
        center=(x+35, y+35),
        radius=36,
        width=5
    )



# while True:
    # draw_X(x=245)
    # draw_O(x=215)
    # for event in pygame.event.get():
        # if event.type == pygame.QUIT:
            # exit()
    # pygame.display.flip()