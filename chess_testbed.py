import turtle
import pygame
from pygame.locals import *
from chessboard import Square

#Turtle example of drawing a star__________________________________________________________
#
# star = turtle.Turtle()

# star.right(75) 
# star.forward(100) 
  
# for i in range(4): 
#     star.right(144) 
#     star.forward(100) 
      
# turtle.done() 
#_________________________________________________________________________________________


#4 Squares in the corners example from geeksforgeeks:_____________________________________
#
# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects
# class Square(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Square, self).__init__()
         
#         # Define the dimension of the surface
#         # Here we are making squares of side 25px
#         self.surf = pygame.Surface((25, 25))
         
#         # Define the color of the surface using RGB color coding.
#         self.surf.fill((0, 200, 255))
#         self.rect = self.surf.get_rect()
 
# # initialize pygame
# pygame.init()
 
# # Define the dimensions of screen object
# screen = pygame.display.set_mode((800, 600))
 
# # instantiate all square objects
# square1 = Square()
# square2 = Square()
# square3 = Square()
# square4 = Square()
 
# # Variable to keep our game loop running
# gameOn = True
 
# # Our game loop
# while gameOn:
#     # for loop through the event queue
#     for event in pygame.event.get():
         
#         # Check for KEYDOWN event
#         if event.type == KEYDOWN:
             
#             # If the Backspace key has been pressed set
#             # running to false to exit the main loop
#             if event.key == K_BACKSPACE:
#                 gameOn = False
                 
#         # Check for QUIT event
#         elif event.type == QUIT:
#             gameOn = False
 
#     # Define where the squares will appear on the screen
#     # Use blit to draw them on the screen surface
#     screen.blit(square1.surf, (40, 40))
#     screen.blit(square2.surf, (40, 530))
#     screen.blit(square3.surf, (730, 40))
#     screen.blit(square4.surf, (730, 530))
 
#     # Update the display using flip
#     pygame.display.flip()
#_________________________________________________________________________________________


#Rendering a square_______________________________________________________________________
# pygame.init()
# screen = pygame.display.set_mode((800,600))

# test_square = Square("White")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_BACKSPACE:
#                 running = False
#         elif event.type == QUIT:
#             running = False

#     screen.blit(test_square.surface, (40, 40))
#     pygame.display.flip()
#_________________________________________________________________________________________


# days = 10

# day_list = list(range(1, days+1))
# print(day_list)

# meetings = [[1,3],[5,7]]
# for meeting in meetings:
#     start, stop = meeting
#     print(start, stop)

def countDays(days: int, meetings: list[list[int]]) -> int:
        total_days = list(range(1, days+1))
        meeting_days = []
        for meeting in meetings:
            start, stop = meeting
            days = list(range(start, stop+1))
            meeting_days.extend(days)

        non_meeting_days = [i for i in total_days if i not in meeting_days]
        return len(non_meeting_days)


print(countDays(days=78558, meetings=[[19045,44672],[54572,78079],[10368,50188],[13355,28953],[2404,34057],[54415,77471],[60296,61311],[71565,74846],[59025,69422],[9528,24542],[50247,58572],[27268,69294],[55250,74351],[27096,77860],[6622,69265],[50992,63085],[1436,31540],[30549,53125],[22696,61310],[40986,78013],[6979,69673],[9444,70734],[26471,71465],[3570,35424],[67207,78118],[1871,55797],[29722,37536],[5936,60192],[23621,38090],[2196,76403],[28674,59478],[68879,76049],[34539,67491],[2676,23819],[46923,67879],[1627,7085],[36805,56933],[21248,48255],[41546,74153],[36166,40828],[42247,75555],[8811,19053],[38226,57290],[39532,51099],[41330,57034],[8407,73804],[5420,75065],[36886,62802],[37225,70172],[63111,64860],[5251,70208]]))
