# Lesson 3: Compilation of Lessons 1 & 2

## Learning Objectives
- Strengthen knowledge of constructing shapes from the commands taught in Lessons 1 & 2
- Complete drawing challenges with more complex shapes
- Establish good coding practices: Plan the drawing > Implement it in code form > Adjust where required

## Final Turtle Commands

**Undo Changes**: Undo the most recent action you did. If you want to undo your last five commands, then type `my_turtle.undo()` five times.

```python
my_turtle.forward(100)
my_turtle.undo()
```

**Clear Screen**: Clear your turtle to make room for more drawings. Your variables will not change, and the turtle will remain in the same position. If you have multiple turtles on the screen, then you need to call the specific turtle you want to clear.

```python
my_turtle.clear() # Clear my_turtle
```

**Reset Environment**: Remove all drawings from the screen to start from scratch. All parameters will be returned to their default values.

```python
my_turtle.reset()
```

**Leave a Stamp**: Leave a stamp of your turtle on the screen to trakc your actions.

```python
my_turtle.stamp()
my_turtle.fd(100)
my_turtle.stamp()
my_turtle.fd(100)
```

**Clear a Stamp**: Clear a particular stamp using its stamp ID.

```python
my_turtle.clearstamp(1) # Clear stamp with a stamp ID of 1
```

**Clone**: There are times when you need another turtle, and that is where this function comes in handy. The clone's parameters can be changed independent of the initial turtle.

```python
second_turtle = my_turtle.clone() # Clone my_turtle to make a second turtle called second_turtle
my_turtle.color("red")
second_turtle.color("blue")
my_turtle.circle(100)
second_turtle.circle(60)
```

![Lesson 3 1 Clone](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/7b602d1b-8167-4404-8f1d-3af5bac0db05)

## Review

### Question 1
What does the `.undo()` function do in Turtle Graphics?  
a. It clears the screen.  
b. It undoes the last turtle movement.  
c. It resets the turtle to its original position.  
d. It clears all stamps.

<details>
<summary>Answer</summary>
b
</details>

### Question 2
What happens when you call `.undo()` after using `.stamp()`?  
a. The stamp is removed.  
b. The turtle's movement is undone.  
c. The turtle's position is reset.  
d. The screen is cleared.

<details>
<summary>Answer</summary>
a
</details>

### Question 3
What does the `.clear()` function do in Turtle Graphics?  
a. It clears the screen.  
b. It clears the last turtle movement.  
c. It resets the turtle to its original position.  
d. It clears all stamps.

<details>
<summary>Answer</summary>
a
</details>

### Question 4
What does the `.clone()` function do in Turtle Graphics?  
a. It creates a copy of the turtle at its current position.  
b. It clears the screen.  
c. It resets the turtle to its original position.  
d. It clears all stamps.

<details>
<summary>Answer</summary>
a
</details>

### Question 5
What happens when you call `.clearstamp(5)` after using `.stamp()`?  
a. The turtle's position is reset.  
b. All stamps are removed.  
c. The stamp with ID 5 is removed.  
d. The screen is cleared.

<details>
<summary>Answer</summary>
c
</details>

## Exercise
Write a Python program for drawing each of these shapes!

(Easy) Challenges 1-5: The student should be able to do all of these with the concepts learned up to this point.  

(Medium) Challenges 6-11: The same concepts can be used, but the scripts may be longer for these challenges.  

(Hard) Challenges 12-14: Advanced concepts such as loops may be needed, so do not do these challenges. They will be returned to later.

![Screenshot 2024-03-03 152334](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/3a31c6cd-71d2-47eb-b098-372b60131d50)

<details>
<summary>Hint</summary>
Attempt each challenge first. If you are stuck, you can refer to the Scripts (Answer Key) > Lesson 3 Scripts folder, where there will be a sample solution for each of the challenges (only one of the many ways that you can create each image!). This exercise is meant to boost your creativity and learn programming concepts using Turtle along the way!
</details>

<details>
<summary>Challenge 1</summary>

![Lesson 3 Challenge 1](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/3e4c74c9-e56d-4794-9382-38c7ebf8af8a)
</details>

<details>
<summary>Challenge 2</summary>

![Lesson 3 Challenge 2](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/1c1d3796-f812-4488-97fb-a6b4743e9a88)
</details>

<details>
<summary>Challenge 3</summary>

![Lesson 3 Challenge 3](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/c58c5d7d-cd1e-4f2a-9992-8ae2966e96d9)
</details>

<details>
<summary>Challenge 4</summary>

![Lesson 3 Challenge 4](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/a65213ec-3fbb-417d-88e1-a7cf95755680)
</details>

<details>
<summary>Challenge 5</summary>

![Lesson 3 Challenge 5](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/b7c506e2-b294-4b1b-a281-a959d5e399ac)
</details>

<details>
<summary>Challenge 6</summary>

![Lesson 3 Challenge 6](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/efb5ca43-f341-4eff-ae94-5d8e35ad6f05)
</details>

<details>
<summary>Challenge 7</summary>

![Lesson 3 Challenge 7](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/51d58658-1484-4fe2-afe9-d4994c5aca99)
</details>

<details>
<summary>Challenge 8</summary>

![Lesson 3 Challenge 8](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/c4f5db12-f5ef-4f89-a221-d68f06a4e571)
</details>

<details>
<summary>Challenge 9</summary>

![Lesson 3 Challenge 9](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/67f3ca1a-6a77-4fdf-b68e-51a83ec8f39d)
</details>

<details>
<summary>Challenge 10</summary>

![Lesson 3 Challenge 10](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/2d420dff-3559-4b13-be94-1c8f4292b29a)
</details>

<details>
<summary>Challenge 11</summary>

![Lesson 3 Challenge 11](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/088d0eb9-60ae-40a9-b675-2409fbff0d7b)
</details>

<details>
<summary>Challenge 12</summary>

![Lesson 3 Challenge 12](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/32cee938-a7cd-41f6-8f6a-bf377892a27f)
</details>

<details>
<summary>Challenge 13</summary>

![Lesson 3 Challenge 13](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/e2fc5381-af1b-4379-bd8a-ac31db9fd45f)
</details>

<details>
<summary>Challenge 14</summary>

![Lesson 3 Challenge 14](https://github.com/cgtiu642/intro-to-turtle-learning/assets/97239180/fad0f3a2-34e0-46b6-8f1f-df2d2c37949d)
</details>