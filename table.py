import pygame
import modules.path_to_file as m_path

table=pygame.image.load(m_path.find_path_to_file("images/table.png"))
table = pygame.transform.scale(table,(285,285))
# X_O = pygame.image.l