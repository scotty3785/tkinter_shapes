#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shape_demo.py
#  
#  Copyright 2018 Scott Thomson <github @scotty3785>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from tkinter_shapes import Shape

def with_args( func_name, *args):
    """Helper function to make lambda functions easier
    Thanks to guizero"""
    return lambda: func_name(*args)

def rotate_left():
    """Rotate the shape by +10 degrees"""
    shape.rotate(10)
    
def rotate_right():
    """Rotate the shape by -10 degrees"""
    shape.rotate(-10)
    
def move(x,y):
    """Move the shape by x,y pixels"""
    shape.x += x
    shape.y += y
    
def change_color():
    """Change the color to a random color"""
    cols = ['red','blue','green','yellow','purple']
    shape.color = random.choice(cols)
    
def change_sides(chg):
    """Increase the number of sides by 'chg' sides''"""
    shape.sides += chg
    #shape.redraw()
    
def change_size(chg):
    """Change the side of the shape's radius by 'chg' pixels''''"""
    shape.radius += chg
    
def objectSelect(event):
    """Make the clicked on shape the selected shape, set the outline of 
    the new shape and clear the outline of the new shape"""
    global shape
    element_id = canvas.find_withtag(CURRENT)
    for s in shape_list:
        try:
            if s.shape == element_id[0]:
                shape.select(False)
                shape = s
                shape.select(True)
        except IndexError as err:
            pass
    

def main():
    global shape
    global shape_list
    global canvas
    
    #Create a tkinter instance with a canvas and make it clickable
    root = Tk()
    canvas = Canvas(root,width=400,height=400)
    canvas.grid()
    canvas.bind('<ButtonPress-1>',objectSelect)

    #Create 4 shapes and add them to the list
    shape_list.append(Shape(canvas,100,100,50,5,color='red'))
    shape_list.append(Shape(canvas,200,200,50,3,color='green'))
    shape_list.append(Shape(canvas,150,100,50,5,color='pink'))
    shape_list.append(Shape(canvas,200,150,50,3))
    #Set the first shape as the current shape
    shape = shape_list[0]
    
    #Create a control panel to change the properties of the shape
    frm = Frame(root)
    frm.grid()
    Button(frm,text='<',command=rotate_left).grid(row=0,column=0)
    Button(frm,text='>',command=rotate_right).grid(row=0,column=2)
    Button(frm,text='Up',command=with_args(move,0,-5)).grid(row=0,column=1)
    Button(frm,text='L ',command=with_args(move,-5,0)).grid(row=1,column=0)
    Button(frm,text='**',command=change_color).grid(row=1,column=1)
    Button(frm,text=' R',command=with_args(move,5,0)).grid(row=1,column=2)
    Button(frm,text='-',command=with_args(change_sides,-1)).grid(row=2,column=0)
    Button(frm,text='Dn',command=with_args(move,0,5)).grid(row=2,column=1)
    Button(frm,text='+',command=with_args(change_sides,1)).grid(row=2,column=2)
    Button(frm,text='--',command=with_args(change_size,-5)).grid(row=3,column=0)
    Button(frm,text='++',command=with_args(change_size,5)).grid(row=3,column=2)
    
    #Start the mainloop
    root.mainloop()

if __name__ == '__main__':
    from tkinter import *
    import random
    
    shape = None
    canvas = None
    shape_list = []
    main()
