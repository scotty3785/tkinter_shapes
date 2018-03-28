<h1 id="tkinter_shapes">tkinter_shapes</h1>


<h2 id="tkinter_shapes.rotate_left">rotate_left</h2>

```python
rotate_left()
```
Rotate the shape by +10 degrees
<h2 id="tkinter_shapes.change_sides">change_sides</h2>

```python
change_sides(chg)
```
Increase the number of sides by 'chg' sides''
<h2 id="tkinter_shapes.change_color">change_color</h2>

```python
change_color()
```
Change the color to a random color
<h2 id="tkinter_shapes.objectSelect">objectSelect</h2>

```python
objectSelect(event)
```
Make the clicked on shape the selected shape, set the outline of
the new shape and clear the outline of the new shape
<h2 id="tkinter_shapes.move">move</h2>

```python
move(x, y)
```
Move the shape by x,y pixels
<h2 id="tkinter_shapes.with_args">with_args</h2>

```python
with_args(func_name, *args)
```
Helper function to make lambda functions easier
Thanks to guizero
<h2 id="tkinter_shapes.rotate_right">rotate_right</h2>

```python
rotate_right()
```
Rotate the shape by -10 degrees
<h2 id="tkinter_shapes.change_size">change_size</h2>

```python
change_size(chg)
```
Change the side of the shape's radius by 'chg' pixels''''
<h1 id="tkinter_shapes.Shape">Shape</h1>

```python
Shape(self, canvas, x, y, radius, sides, angle=0, **args)
```

<h2 id="tkinter_shapes.Shape.get_poly_coords">get_poly_coords</h2>

```python
Shape.get_poly_coords(self, x, y, radius, sides, rotate=0)
```
Calculate position of the vertices of the shape
<h2 id="tkinter_shapes.Shape.rotate">rotate</h2>

```python
Shape.rotate(self, rotate_by)
```
Rotate the shape by the 'rotate_by' degrees''
<h2 id="tkinter_shapes.Shape.color">color</h2>

Get the color of the shape
<h2 id="tkinter_shapes.Shape.draw">draw</h2>

```python
Shape.draw(self)
```
Draw the shape and set default configuration
<h2 id="tkinter_shapes.Shape.radius">radius</h2>

Get the radius of the shape
<h2 id="tkinter_shapes.Shape.select">select</h2>

```python
Shape.select(self, state)
```
Select/Unselect by marking the shape with a black outline or clear the outline
<h2 id="tkinter_shapes.Shape.y">y</h2>

Get the y coordinate of the shape
<h2 id="tkinter_shapes.Shape.x">x</h2>

Get the x coordinate of the shape
<h2 id="tkinter_shapes.Shape.redraw">redraw</h2>

```python
Shape.redraw(self)
```
Recalculate shape coordinates and redraw
<h2 id="tkinter_shapes.Shape.sides">sides</h2>

Get the number of sides of the shape
