# Lesson 1: Drawing Lines

## Learning Objectives
- Learn basic Turtle Graphics commands
- Understand how to control the turtle's movement
- Explore ways to customize the initial screen

## Basic Turtle Commands
In Turtle, you can command the cursor to move around to create visual drawings like shapes. Let's learn some basic commands to control your turtle:

**Move Forward**: Make your turtle move forward by a certain distance.

```python
my_turtle.forward(100) # Move forward 100 units
```

![Lesson 1 1 Forward](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/0834396a-71c5-44b5-b827-8542910b317a)

**Move Backward**: Make your turtle move backward by a certain distance.

```python
my_turtle.backward(100) # Move backward 100 units
```

![Lesson 1 2 Backward](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/377fdce0-75e9-433d-8815-798a949c708c)

**Turn Right**: Turn your turtle to the right by a certain angle.

```python
my_turtle.right(90) # Turn right by 90 degrees
```

![Lesson 1 3 Right](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/46cbfc9c-b5a7-4b36-bcc7-f9dc5e537d68)

**Turn Left**: Turn your turtle to the left by a certain angle.

```python
my_turtle.left(90) # Turn left by 90 degrees
```

![Lesson 1 4 Left](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/4649c4c1-ff27-444d-95b1-911df8c4b5e8)

All 4 functions also have shorthand versions `my_turtle.fd()`, `my_turtle.bk()`, `my_turtle.rt()`, and `my_turtle.lt()` which work in the same way.

**Set Orientation**: Alternative way to change the orientation of the turtle. The initial angle of the cursor is set to `0` (east) by default.

```python
my_turtle.setheading(90) # Set the orientation of the turtle to 90 degrees (north)
```

![Lesson 1 5 Set Heading](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/0af83791-0cee-4e66-bc8b-1bae5af9f14d)

**Pen Up / Pen Down**: Lift your turtle's pen up or down. When the pen is up, the turtle will move without drawing. When the pen is down, the turtle will resume drawing.

```python
my_turtle.penup() # Lift the pen
my_turtle.pendown() # Put the pen down
```

Let's look at an example. You can try typing the following script on your code editor. Don't forget the 3 steps discussed in Lesson 0 to start using Turtle Graphics!

```python
my_turtle.forward(100) # This line will be drawn
my_turtle.penup()
my_turtle.right(90)
my_turtle.forward(100) # This line will not be drawn
my_turtle.pendown()
my_turtle.forward(100) # This line will be drawn
```

![Lesson 1 6 Pen Up   Pen Down](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/c94ec323-1151-4c53-b286-85b4c5318be7)

## Initial Customization
Here are some functions you can use to customize the Turtle screen.

**Change Screen Title**: Change the title of the screen, located at the top of the window.

```python
screen.title("Intro to Turtle") # Change the title of the screen to "Intro to Turtle"
```

**Change Background Color**: Change the background color of the screen.

```python
screen.bgcolor("red") # Change the background color to red
```
You can also try using `"green"` or `"blue"`.

**Change Turtle Size**: Change the size of the turtle using the function `my_turtle.shapesize(stretch_width, stretch_length, outline)`.

```python
my_turtle.shapesize(1, 5, 10) # turtle with stretch_width 1, stretch_length 5, and outline 10
```

**Change Turtle Shape**: Change the shape of the turtle. 

```python
my_turtle.shape("turtle") # Change the turtle shape to a turtle
```

There are also other options you can try using, including `"arrow"`, `"circle"`, `"square"`, `"triangle"`, and `"classic"` (default arrowhead).

## Review

### Question 1
Which command is the same as `my_turtle.backward(90)`?  
a. `my_turtle.fd(90)`  
b. `my_turtle.bk(90)`  
c. `my_turtle.rt(90)`  
d. `my_turtle.lt(90)`

<details>
<summary>Answer</summary>
b
</details>

### Question 2
What is the purpose of the `my_turtle.penup()` command?  
a. Lift the pen, so the turtle doesn't draw  
b. Lower the pen to start drawing  
c. Change the pen color to red  
d. Increase the thickness of the pen

<details>
<summary>Answer</summary>
a
</details>

### Question 3
How do you change the background color of the graphics window to green?  
a. `my_turtle.bgcolor("red")`  
b. `my_turtle.backgroundcolor("green")`  
c. `my_turtle.background("green")`  
d. `screen.bgcolor("green")`

<details>
<summary>Answer</summary>
d (<code>bgcolor()</code> is a Screen method)
</details>

### Question 4
Which command is used to turn the turtle to the right by 45 degrees?  
a. `my_turtle.right(45)`  
b. `my_turtle.right(90)`  
c. `my_turtle.left(45)`  
d. `my_turtle.left(90)`

<details>
<summary>Answer</summary>
a
</details>

### Question 5
Which command can be used as an alternative for turning the turtle by a certain angle?  
a. `my_turtle.done()`  
b. `my_turtle.shapesize()`  
c. `my_turtle.setheading()`  
d. `turtle.setheading()`

<details>
<summary>Answer</summary>
c
</details>

## Exercise
In this lesson, you will be drawing lines. Complete the following tasks using the functions taught above.

a. (Easy) Make the shape of the turtle a circle.
<details>
<summary>Hint</summary>
Use <code>my_turtle.shape()</code>
</details>

b. (Easy) Draw a straight line forward that is 25 units long.
<details>
<summary>Hint</summary>
Use <code>my_turtle.forward()</code>
</details>

c. (Medium) Leave a gap of 10 units, then continue the drawing with a line that is 50 units long.
<details>
<summary>Hint</summary>
Use <code>my_turtle.penup()</code> and <code>my_turtle.pendown()</code>
</details>

d. (Medium) Draw 5 vertical lines, spaced apart by 10 units.
<details>
<summary>Hint</summary>
Use <code>my_turtle.penup()</code> and <code>my_turtle.pendown()</code>
</details>

e. (Medium) Draw a zigzag line that has line segments that are 20 units long and separated by 45 degrees.
<details>
<summary>Hint</summary>
Use <code>my_turtle.setheading()</code>
</details>

f. (Hard) Draw a regular 5-point star.

<img width="200" alt="Image" src="https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/a5fbcc31-9340-44c8-a8d2-96b2e2b1a316">

<details>
<summary>Hint</summary>
Use a combination of <code>my_turtle.forward()</code> and <code>my_turtle.setheading()</code> with angles of 36 degrees and 252 degrees. This is optional, and it will be covered in later modules using loops instead.
</details>