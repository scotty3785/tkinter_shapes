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
<h2 id="tkinter_shapes.Shape.draw">draw</h2>

```python
Shape.draw(self)
```
Draw the shape and set default configuration
<h2 id="tkinter_shapes.Shape.color">color</h2>

Get the color of the shape
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
<h2 id="tkinter_shapes.Shape.to_back">to_back</h2>

```python
Shape.to_back(self)
```
Move shape behind others
<h2 id="tkinter_shapes.Shape.sides">sides</h2>

Get the number of sides of the shape
<h2 id="tkinter_shapes.Shape.to_front">to_front</h2>

```python
Shape.to_front(self)
```
Move shape in front of others
