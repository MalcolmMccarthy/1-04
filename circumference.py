# Created by: Malcolm McCarthy
# Created on: Sep 2017
# Created for: ICS3U
# This program calculates the circumference of a circle,
#   when you give it the radius

import ui

def calculate_touch_up_inside(sender):
	# calculates circumference

 PI = 3.14 
# constant

 radius = int(view['radius_textbox'].text)
#input

 circumference = 2 * PI * radius
#process

 view['answer_label'].text = 'The circumference is: ' + str(circumference) + ' cm'
#output

view = ui.load_view()
view.present('sheet')
