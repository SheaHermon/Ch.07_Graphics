'''
PYCASSO PROJECT (4pts)
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
# A Pokeball Catching A Pokemon
import arcade
offset=0
arcade.open_window(500, 500, "Shea Hermon: Poke Ball")
arcade.set_background_color((72, 155, 227))
arcade.start_render()
for i in range(12):
    arcade.draw_arc_filled(364, 357, 1000, 1000, (255, 255, 255, 15), offset, 15+offset)
    offset+=30
arcade.draw_circle_filled(394, 362, 4.5, (102, 102, 114))
arcade.draw_arc_filled(356, 310, 126, 110, (208, 216, 222), 140, 360, 50)
arcade.draw_arc_outline(356, 310, 126, 110, arcade.color.BLACK, 140, 360, 3, 50)
arcade.draw_arc_filled(343, 397, 121, 120, arcade.color.RED, 110, 360, 185)
arcade.draw_arc_outline(343, 397, 121, 120, arcade.color.BLACK, 110, 360, 3, 185)
arcade.draw_ellipse_filled(350, 320, 120, 60, arcade.color.BLACK, -35)
arcade.draw_ellipse_filled(340, 380, 115, 60, arcade.color.BLACK, 10)
arcade.draw_circle_filled(310, 405, 15, (208, 216, 222))
arcade.draw_circle_outline(310, 405, 15, arcade.color.BLACK, 4)
arcade.draw_circle_outline(310, 405, 9, arcade.color.BLACK, 2)
arcade.draw_circle_filled(328, 280, 12, arcade.color.BLACK)
arcade.draw_ellipse_filled(365, 430, 20, 30, arcade.color.WHITE, -30)
point_list = ((360, 328),
              (356, 320),
              (235, 335),
              (255, 375))
arcade.draw_polygon_filled(point_list, arcade.color.RED)
point_list = ((255, 375),
              (270, 340),
              (195, 225),
              (125, 275))
arcade.draw_polygon_filled(point_list, arcade.color.RED)
point_list = ((195, 225),
              (125, 275),
              (175, 100),
              (225, 50))
arcade.draw_polygon_filled(point_list, arcade.color.RED)
point_list = ((175, 100),
              (225, 50),
              (80, -150),
              (-150, 150))
arcade.draw_polygon_filled(point_list, arcade.color.RED)
point_list = ((330, 337),
              (326, 334),
              (275, 354),
              (255, 369))
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
point_list = ((255, 360),
              (250, 344),
              (190, 288),
              (140, 274))
arcade.draw_ellipse_filled(225, 300, 60, 5, arcade.color.WHITE, -50)
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
point_list = ((190, 200),
              (175, 250),
              (190, 120),
              (215, 70))
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
point_list = ((155, 90),
              (200, 70),
              (50, 80),
              (5, 110))
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)
arcade.draw_ellipse_filled(110, 30, 120, 10, arcade.color.WHITE, -20)
arcade.draw_ellipse_filled(70, 50, 120, 6, arcade.color.WHITE, -5)
arcade.draw_ellipse_filled(155, 228, 80, 5, arcade.color.WHITE, -104)
point_list = ((360, 328),
              (356, 320),
              (267, 332),
              (195, 225),
              (225, 50),
              (80, -150),
              (-150, 150),
              (175, 100),
              (125, 275),
              (255, 375))
arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 3)
arcade.draw_polygon_outline(point_list, arcade.color.WHITE, .8)
arcade.finish_render()
arcade.run()


