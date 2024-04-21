# Lesson 2: Drawing Shapes

## Learning Objectives
- Build on the concepts of Turtle movement learned in Lesson 1
- Learn how to draw basic shapes like squares, circles, and triangles using Turtle
- Experiment with ways to customize the turtle through colors, shapes, and so on

## More Turtle Commands

**Move the Turtle**: Move the turtle to the specified coordinates.

```python
my_turtle.goto(100, 100) # Move the turtle to the (100, 100) location on the screen
```

![Lesson 2 1 Go To](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/6226eb3b-8c8b-4e41-93b6-3ad2d60c9320)

**Get Turtle Position**: Find the turtle's current location `(x, y)`. This is similar to Python's built-in function `index()` for lists.

```python
my_turtle.pos() # Get the coordinates of the turtle
```

**Reset the Turtle**: Move the turtle to the origin (0, 0).

```python
my_turtle.home() # Return the turtle to (0, 0)
```

![Lesson 2 2 Home](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/7f4d59ba-e060-4538-881f-8b6942d05df4)

**Draw a Dot**: Draw a dot with the specified size.

```python
my_turtle.dot(100) # Draw a dot with diameter 100
```

![Lesson 2 3 Dot](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/728b12a7-2556-4b55-bbca-ab2dc37fc8a6)

**Draw a Circle**: Draw a circle with the specified radius.

```python
my_turtle.circle(100) # Draw a circle with radius 100
```

![Lesson 2 4 Circle](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/e0c7a6bf-8da4-4d11-9204-49a22f4a683f)

## Pen Customization

**Change Pen Size**: Change the size of the pen. Either one of the two functions below can be used to achieve the same effect.

```python
my_turtle.pensize(5) # Set the line thickness to 5
my_turtle.width(5) # Also sets the line thickness to 5
```

**Change Pen Speed**: Change the speed of the pen. If the input is greater than `10` or smaller than `0.5`, then the speed is set to `0` (no animation takes place).

| **Speedstring** | **Speedvalue** |
| :----- | :----- |
| `'fastest'` | `0` |
| `'fast'` | `10` |
| `'normal'` | `6` |
| `'slow'` | `3` |
| `'slowest'` | `1` |

```python
my_turtle.speed(10) # Change the pen speed to 10
my_turtle.speed('fast') # Also changes the pen speed to 10
```

**Change Pen Color**: Change the color of the pen.

```python
my_turtle.pencolor("red") # Change the pen color to red
```

**Set Fill Color**: Set the fill color.

```python
my_turtle.fillcolor("yellow") # Set the fill color to yellow
```

**Set Pen Color and Fill Color**: Change both the color of the pen and the fill color using one function.

```python
my_turtle.color("red", "blue") # Change the pen color to red and the fill color to blue
```

**Set Pen Settings**: Combine some of the functions discussed above to customize the pen.

```python
my_turtle.pen(fillcolor="yellow", pencolor="red", pensize=5, speed=10) # Change the fill color to yellow, the pen color to red, the pen size/thickness to 5, and the pen speed to 10
```

**Fill a Shape**: Alternative way to fill a shape or any enclosed drawing. After setting colors, this function can be used.

```python
my_turtle.begin_fill()
my_turtle.circle(10) # Draw a circle with radius 10
my_turtle.end_fill()
```

> Remember to call `turtle.done()` at the end of your program to ensure that the Turtle Graphics window does not close immediately.

## Review

### Question 1
What is the correct method to draw a circle with a diameter of 60 units?  
a. `my_turtle.circle(60)`  
b. `screen.circle(60)`  
c. `my_turtle.circle(30)`  
d. `my_turtle.circle(120)`

<details>
<summary>Answer</summary>
c
</details>

### Question 2
How do you set the pen size to 5?  
a. `my_turtle.width(5)`  
b. `turtle.pensize(5)`  
c. `screen.pensize(5)`  
d. `my_turtle.pensize(5)`

<details>
<summary>Answer</summary>
a, d (both answers accepted)
</details>

### Question 3
Which method is used to set the fill color to blue?  
a. `my_turtle.fillcolor("red")`  
b. `my_turtle.pencolor("blue")`  
c. `screen.pencolor(5)`  
d. `my_turtle.color("", "blue")`

<details>
<summary>Answer</summary>
d
</details>

### Question 4
How do you move the turtle to the coordinates (50, 50)?  
a. `my_turtle.goto(100, 100)`  
b. `my_turtle.goto(50, 50)`  
c. `my_turtle.move_to(50, 50)`  
d. `turtle.goto(100, 100)`

<details>
<summary>Answer</summary>
b
</details>

### Question 5
What is the correct method to end the Turtle Graphics window?  
a. `my_turtle.done()`  
b. `screen.done()`  
c. `turtle.done()`  
d. `my_turtle.close()`

<details>
<summary>Answer</summary>
c (<code>done()</code> is part of the main package)
</details>

## Exercise
Now that you know the basics, let's draw some shapes!

a. (Easy) Draw a circle of radius 50.
<details>
<summary>Hint</summary>
Use <code>my_turtle.circle()</code>
</details>

b. (Easy) Draw a square with side length 200.
<details>
<summary>Hint</summary>
Use <code>my_turtle.forward()</code> and <code>my_turtle.right()</code>
</details>

c. (Medium) Draw a triangle with side length 200.
<details>
<summary>Hint</summary>
Use <code>my_turtle.forward()</code> and <code>my_turtle.right()</code>
</details>

d. (Medium) Draw a decagon (10 sides) with pen color blue and fill color red.
<details>
<summary>Hint</summary>
Use <code>my_turtle.forward()</code> and <code>my_turtle.right()</code>
</details>

e. (Hard) Draw Captain America's shield.

<img src="https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/940a7d85-cb7e-4667-8d8f-c7e4c1f7074e" width="210" height="210">

<img src="https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/caa1a3cf-f1a5-4d13-a972-0d5443923ff0" width="210" height="210">

<img width="490" alt="Screenshot 2024-02-18 162712" src="https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/1415d238-4249-4bb9-87cb-a522723626e4">
<details>
<summary>Hint</summary>
Captain America's shield is made up of 4 concentric circles (circles that have the same center) and 1 star.
</details>