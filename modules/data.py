import pygame
import sys
import modules.screen as m_scr
import modules.graphics as m_grp
import modules.draw_O_X as m_draw
import modules.table as m_table

pygame.init()
turn = 1
list_cell=[
  2,2,2,
  2,2,2,
  2,2,2
]

win = False


def check_WIN(function, num):
    global list_cell, win
    if list_cell[0]==list_cell[1]==list_cell[2]==num:
        color = m_draw.WIN
        function(x = 170, y = 145, color=color)
        function(x = 265, y = 145, color=color)
        function(x = 360, y = 145, color=color)
        win = True
    elif list_cell[3]==list_cell[4]==list_cell[5]==num:
        color = m_draw.WIN
        function(x = 170, y = 235, color=color)
        function(x = 265, y = 235, color=color)
        function(x = 360, y = 235, color=color)
        win = True
    elif list_cell[6]==list_cell[7]==list_cell[8]==num:
        color = m_draw.WIN
        function(x = 170, y = 330, color=color)
        function(x = 265, y = 330, color=color)
        function(x = 360, y = 330, color=color)
        win = True
    elif list_cell[0]==list_cell[3]==list_cell[6]==num:
        color = m_draw.WIN
        function(x = 170, y = 145, color=color)
        function(x = 170, y = 235, color=color)
        function(x = 170, y = 330, color=color)
        win = True
    elif list_cell[1]==list_cell[4]==list_cell[7]==num:
        color = m_draw.WIN
        function(x = 265, y = 145, color=color)
        function(x = 265, y = 235, color=color)
        function(x = 265, y = 330, color=color)
        win = True
    elif list_cell[2]==list_cell[5]==list_cell[8]==num:
        color = m_draw.WIN
        function(x = 360, y = 145, color=color)
        function(x = 360, y = 235, color=color)
        function(x = 360, y = 330, color=color)
        win = True
    elif list_cell[0]==list_cell[4]==list_cell[8]==num:
        color = m_draw.WIN
        function(x = 170, y = 145, color=color)
        function(x = 265, y = 235, color=color)
        function(x = 360, y = 330, color=color)
        win = True
    elif list_cell[2]==list_cell[4]==list_cell[6]==num:
        color = m_draw.WIN
        function(x = 170, y = 330, color=color)
        function(x = 265, y = 235, color=color)
        function(x = 360, y = 145, color=color)
        win = True

# import threading;threading.Thread(target=lambda:check_WIN(),daemon=True) это сделал Илья Эпик
def reset():
    global list_cell, win
    m_grp.graphics()
    m_grp.screen.blit(m_table.table, (157, 133))
    list_cell = [2, 2, 2, 2, 2, 2, 2, 2, 2]
    win = False
# 🎁🎫(^◕.◕^)🔏⏰💼🗒
def who_turn(x, y):
    global turn
    if turn == 1:
        m_draw.draw_X(x, y)
    elif turn == 0:
        m_draw.draw_O(x, y)
    turn = not turn
    return not turn
def click_pos(coor):
    x = coor[0]
    y = coor[1]
    if not win:
        if 145 < y < 215:
            if 170 < x < 240 and list_cell[0]==2:
                list_cell[0]=who_turn(x = 170, y = 145)
            elif 265 < x < 335 and list_cell[1]==2:
                list_cell[1]=who_turn(x = 265, y = 145)
            elif 360 < x < 430 and list_cell[2]==2:
                list_cell[2]=who_turn(x = 360, y = 145)
        elif 235 < y < 305:
            if 170 < x < 240 and list_cell[3]==2:
                list_cell[3]=who_turn(x = 170, y = 235)
            elif 265 < x < 335 and list_cell[4]==2:
                list_cell[4]=who_turn(x = 265, y = 235)
            elif 360 < x < 430 and list_cell[5]==2:
                list_cell[5]=who_turn(x = 360, y = 235)
        elif 330 < y < 400:
            if 170 < x < 240 and list_cell[6]==2:
                list_cell[6]=who_turn(x = 170, y = 330)
            elif 265 < x < 335 and list_cell[7]==2:
                list_cell[7]=who_turn(x = 265, y = 330)
            elif 360 < x < 430 and list_cell[8]==2:
                list_cell[8]=who_turn(x = 360, y = 330)
        # if turn == 1:
        check_WIN(function=m_draw.draw_X, num=1)
        # elif turn == 0:
        check_WIN(function=m_draw.draw_O, num=0)
    if 500 < y < 575:
        if 250 < x < 350:
            reset()

    
    # if list_cell[0]==list_cell[1]==list_cell[2]==1:
    #     color = m_draw.WIN
    #     m_draw.draw_X(x = 170, y = 145, color=color)
    #     m_draw.draw_X(x = 265, y = 145, color=color)
    #     m_draw.draw_X(x = 360, y = 145, color=color)
    # elif list_cell[0]==list_cell[1]==list_cell[2]==1:
    #     color = m_draw.WIN
    #     m_draw.draw_X(x = 170, y = 145, color=color)
    #     m_draw.draw_X(x = 265, y = 145, color=color)
    #     m_draw.draw_X(x = 360, y = 145, color=color)
    # elif list_cell[0]==list_cell[1]==list_cell[2]==1:
    #     color = m_draw.WIN
    #     m_draw.draw_X(x = 170, y = 145, color=color)
    #     m_draw.draw_X(x = 265, y = 145, color=color)
    #     m_draw.draw_X(x = 360, y = 145, color=color)







