# 7.0 Jedi Training (20pts)  Name: Shea

'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
# import arcade
# offset = 20
# arcade.open_window(500,400, "Pacman")
# arcade.set_background_color(arcade.color.ALMOND)
# arcade.start_render()
# for i in range(25):
#  arcade.draw_line(0, offset, 500, offset, arcade.color.BLACK, 1)
#  arcade.draw_line(offset, 0, offset, 400, arcade.color.BLACK, 1)
#  offset += 20
# arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)
# arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
# arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BRICK_RED, 20)
# arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 330)
# arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
# arcade.draw_ellipse_filled(100, 100, 120, 40, arcade.color.AMBER)
# arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE)
# arcade.draw_point(460, 10, arcade.color.RED, 5)
# arcade.finish_render()
# arcade.run()

'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
hoist = int(input("What is the hoist of your flag? ==>"))
offsets = hoist * .0769
arcade.open_window(hoist * 1.9, hoist, "The Stars and Stripes")
arcade.set_background_color(arcade.color.RED)
arcade.start_render()
for i in range (6):
 arcade.draw_rectangle_filled(hoist* 1.9/2, offsets+hoist*.0769/2,  hoist* 1.9,  hoist* .0769, arcade.color.WHITE)
 offsets += hoist * .0769 *2
arcade.draw_rectangle_filled(hoist*0.76/2, hoist*.26925+hoist*.4615, hoist*.76, hoist*.5385, arcade.color.BLUE)
offsets = hoist*.054
for i in range (5):
 arcade.draw_text("*    *    *    *    *    *", hoist*.063-hoist*.013, hoist*.4615+offsets-hoist*.027, arcade.color.WHITE, hoist*.0616)
 offsets += hoist*.054
 arcade.draw_text("*    *    *    *    *", hoist*.063 + hoist*.063-hoist*.013, hoist*.4615 + offsets-hoist*.027, arcade.color.WHITE, hoist*.0616)
 offsets += hoist * .054
arcade.finish_render()
arcade.run()


