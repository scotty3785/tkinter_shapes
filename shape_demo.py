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
from tkinter import *
import random

def with_args(func_name, *args):
    """Helper function to make lambda functions easier
    Thanks to guizero"""
    return lambda: func_name(*args)

class ShapeDemo(Frame):
    def __init__(self,master,**args):
        Frame.__init__(self,master,args)
        canvas = Canvas(self,width=400,height=400)
        canvas.grid(columnspan=2)
        canvas.bind('<ButtonPress-1>',self.objectSelect)
        self.canvas = canvas
        
        #Storage for shapes
        self.shape = None
        self.shape_list = []


        #Create 4 shapes and add them to the list
        self.shape_list.append(Shape(canvas,100,100,50,5,color='red'))
        self.shape_list.append(Shape(canvas,200,200,50,3,color='green'))
        self.shape_list.append(Shape(canvas,150,100,50,5,color='pink'))
        self.shape_list.append(Shape(canvas,200,150,50,3))
        #Set the first shape as the current shape
        self.shape = self.shape_list[0]
        
        #Create a control panel to change the properties of the shape
        frm = Frame(self)
        frm.grid(row=2,column=0)
        Button(frm,text='<',command=self.rotate_left).grid(row=0,column=0)
        Button(frm,text='>',command=self.rotate_right).grid(row=0,column=2)
        Button(frm,text='Up',command=with_args(self.move,0,-5)).grid(row=0,column=1)
        Button(frm,text='L ',command=with_args(self.move,-5,0)).grid(row=1,column=0)
        Button(frm,text='**',command=self.change_color).grid(row=1,column=1)
        Button(frm,text=' R',command=with_args(self.move,5,0)).grid(row=1,column=2)
        Button(frm,text='-',command=with_args(self.change_sides,-1)).grid(row=2,column=0)
        Button(frm,text='Dn',command=with_args(self.move,0,5)).grid(row=2,column=1)
        Button(frm,text='+',command=with_args(self.change_sides,1)).grid(row=2,column=2)
        Button(frm,text='--',command=with_args(self.change_size,-5)).grid(row=3,column=0)
        Button(frm,text='++',command=with_args(self.change_size,5)).grid(row=3,column=2)
        Frame(frm,bg="darkgray",height=5).grid(row=4,columnspan=3)
        frm2 = Frame(self)
        frm2.grid(row=2,column=1)
        Button(frm2,text="New Shape",command=self.new_shape).grid(row=5)
        Button(frm2,text="Delete Shape",command=self.del_shape).grid(row=6)
        Button(frm2,text="Raise Shape",command=self.raise_shape).grid(row=7)
        Button(frm2,text="Lower Shape",command=self.lower_shape).grid(row=8)

    def rotate_left(self):
        """Rotate the shape by +10 degrees"""
        self.shape.rotate(10)
        
    def rotate_right(self):
        """Rotate the shape by -10 degrees"""
        self.shape.rotate(-10)
        
    def move(self,x,y):
        """Move the shape by x,y pixels"""
        self.shape.x += x
        self.shape.y += y
        
    def change_color(self):
        """Change the color to a random color"""
        cols = ['red','blue','green','yellow','purple']
        self.shape.color = random.choice(cols)
        
    def change_sides(self,chg):
        """Increase the number of sides by 'chg' sides''"""
        self.shape.sides += chg
        #shape.redraw()
        
    def change_size(self,chg):
        """Change the side of the shape's radius by 'chg' pixels''''"""
        self.shape.radius += chg
        
    def objectSelect(self,event):
        """Make the clicked on shape the selected shape, set the outline of 
        the new shape and clear the outline of the new shape"""
        element_id = self.canvas.find_withtag(CURRENT)
        for s in self.shape_list:
            try:
                if s.shape == element_id[0]:
                    if self.shape == None:
                        self.shape = s
                        self.shape.select(True)
                    elif not s == self.shape:
                        self.shape.select(False)
                        self.shape = s
                        self.shape.select(True)
                    else:
                        self.shape.select(False)
                        self.shape = None
            except IndexError as err:
                pass
                
    def new_shape(self):
        cols = ['red','blue','green','yellow','purple']
        self.shape_list.append(Shape(self.canvas,200,100,50,5,color=random.choice(cols)))
        
    def del_shape(self):
        for idx,s in enumerate(self.shape_list):
            if s.shape == self.shape.shape:
                del self.shape_list[idx]
                self.shape = None
                

    def raise_shape(self):
        self.shape.to_front()
        
    def lower_shape(self):
        self.shape.to_back()

def main():

    
    #Create a tkinter instance with a canvas and make it clickable
    root = Tk()
    ShapeDemo(root).grid()
    
    #Start the mainloop
    root.mainloop()

if __name__ == '__main__':

    main()
