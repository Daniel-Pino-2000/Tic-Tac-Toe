from turtle import Screen, Turtle
from time import sleep

def create_matrix():
    '''
    This function creates a matrix of size 3x3.
    '''
    matrix = []
    for i in range(3):
        matrix.append([None] * 3)
    return matrix

def create_board():
    '''
    Draws the lines of the board.
    '''
    global turtle
    turtle.pencolor('brown')
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(1, 0)
    turtle.pendown()
    turtle.goto(1, 3)
    turtle.penup()
    turtle.goto(2, 0)
    turtle.pendown()
    turtle.goto(2, 3)
    turtle.penup()
    turtle.goto(0, 1)
    turtle.pendown()
    turtle.goto(3, 1)
    turtle.penup()
    turtle.goto(0, 2)
    turtle.pendown()
    turtle.goto(3, 2)

            
def draw_board(board):
    '''
    This function passes the values i and j to the draw_cell function'.
    '''
    for i in range(3):
        for j in range(3):
            draw_cell(board, i, j)

def draw_cell(tile, i, j):
    '''
    Draws the zeros and the crusses on the board.
    '''
    global turtle
    turtle.penup()
    
    if tile[i][j] == True:
        turtle.pencolor('blue')
        turtle.pensize(3)
        turtle.goto(j+.5, i+.2)
        turtle.pendown()
        turtle.circle(.3)
        
    elif tile[i][j] == False:
        turtle.pencolor('red')
        turtle.pensize(3)
        turtle.goto(j+.1, i+.1)
        turtle.pendown()
        turtle.goto(j+.9, i+.9)
        turtle.penup()
        turtle.goto(j+.9, i+.1)
        turtle.pendown()
        turtle.goto(j+.1, i+.9)
    turtle.pendown()

def draw_line(tile1, tile2):
    '''
    Draws the line when someone wins the game.
    '''
    turtle.pencolor('black')
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(tile1)
    turtle.pendown()
    turtle.goto(tile2)
    

def click(x, y):
    '''
    Gives the coordinates where the user clicked.
    '''
    global board, temporary1, temporary2
    [j, i] = [int(x), int(y)]
    if 0 <= i < len(board) and 0 <= j < len(board[0]):
        if board[i][j] == None:
            if temporary1 == None:
                temporary1 = [i, j]
                board[i][j] = True
            else:
                temporary2 = [i, j]
                board[i][j] = False
            draw_cell(board, i, j)
            if temporary2 != None:
                temporary1 = None 
                temporary2 = None
                
    if ending(board):
        sleep(3)
        screen.bye()

def ending(board):
    '''
    Ends the game when someone wins or draw.
    '''
    global turtle
    number = 0
    '''
    These are the conditions to win the game.
    '''
    if (board[2][0] != None) and ((board[2][0] == board[2][1]) and (board[2][1] == board[2][2])):
        draw_line((0, 2+.5), (3, 2+.5))
        return True
    
    elif (board[1][0] != None) and ((board[1][0] == board[1][1]) and (board[1][1] == board[1][2])):
        draw_line((0, 1+.5), (3, 1+.5))
        return True
    
    elif (board[0][0] != None) and ((board[0][0] == board[0][1]) and (board[0][1] == board[0][2])):
        draw_line((0, 0+.5), (3, 0+.5))
        return True
    
    elif (board[2][0] != None) and ((board[2][0] == board[1][0]) and (board[1][0] == board[0][0])):
        draw_line((0+.5, 3), (0+.5, 0))
        return True
    
    elif (board[2][1] != None) and ((board[2][1] == board[1][1]) and (board[1][1] == board[0][1])):
        draw_line((1+.5, 3), (1+.5, 0))
        return True
    
    elif (board[2][2] != None) and ((board[2][2] == board[1][2]) and (board[1][2] == board[0][2])):
        draw_line((2+.5, 3), (2+.5, 0))
        return True
    
    elif (board[2][0] != None) and ((board[2][0] == board[1][1]) and (board[1][1] == board[0][2])):
        draw_line((0, 3), (3, 0))
        return True
    
    elif (board[2][2] != None) and ((board[2][2] == board[1][1]) and (board[1][1] == board[0][0])):
        draw_line((3, 3), (0, 0))
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                number += 1
    
    if number == 9:
        print('Draws')
        return True
        

def main():
    global board, Zero, Cruss, temporary1, temporary2, screen, turtle
    
    board = create_matrix()
    Zero = True
    Cruz = False
    temporary1 = None
    temporary2 = None
    
    screen = Screen()
    screen.setup(10*50, 8*50)
    screen.screensize(10*50, 8*50)
    screen.setworldcoordinates(-.5, -.5, 3+.5, 3+.5)
    screen.delay(0)
    turtle = Turtle()
    turtle.hideturtle()
    
    create_board()
    draw_board(board)
    
    screen.onclick(click)
    screen.mainloop()

if __name__ == '__main__':
    main()