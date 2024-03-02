# Scott Walker

## FreeCodeCamp Time Calculator project

This is the second project in a series of five project for the FCC certification in Scientific Computing with Python.

[Link to project guidlines](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)

[Description](#description)

[Day 2 - Math and 24H time](#2024-02-18)  
[Day 3 - Wow, this while loop hates me](#2024-02-28)  
[Day 4 - Finally finished](#2024-03-01)

### Description

This is my second project. In my first project, [An Arithmetic Arranger](https://github.com/wswalker87/fcc_arithmetic_arranger) I used a lot of inline comments. These are meant for me as I get further into my python learning. With this second project I will keeping more comments in this README.

I **understand** that is not necessarily the purpose of this file, but it is **_MY_** project and I intend to use it to work more in markdown as well as keep my hurdles listed as a kind of ~~"Wow, look at everything I messed up."~~ "Look how far I've come!"

### 2024-02-18

I worked out adding the duration to the start time. I did it by splitting the time into two variables using the space as a delimiter. I was then able to break out the time to two ints using the colon as a delimiter.

Once that was done I applied some logic to convert it to military time. Had a bit of an issue with midnight and noon in military time. This was because the logic I was using was avoiding those times all together, which was throwing and error on my `final_time_of_day` variable. The error was an UnboundLocalError. It boiled down to the variable not having a value.

The next step will be to work out the days. I am thinking that I can assign each day of the week a number. Grab the variable that is passed to the function, sort the number that is assigned to it, and then I can apply the logic. I will need to keep track of the number of days, maybe with `num_of_days`, as well as `num_of_weeks`.

**I just discovered through accident, that I can use 1, 2, or 3 `backticks` in markdown to highlight code**

I am also realizing that this would be so much easier if I could import a library, but it is fun to work it out myself. I barely had to google anything this go.

### 2024-02-28

Been a minute since I could get in and mess with this. I was having an issue where I though my computer was ~~fucked~~ limited. I kept running my program and nothing happened. What I ended up finding when I moved to my work laptop was that VSC was stuck in a while loop.

I got out of the while loop and I am mostly there. I have the times printing almost all correctly. I am still trying to fix the day count. It is one day high and I need to figure out why. After that I need to fix the portion that prints, so that if a third paramter is **NOT** passed, I don't print/return a pair of blank parentheses.

DON'T FORGET TO CHANGE THE PRINT STATEMENTS TO RETURN STATEMENTS FOR THE UNIT TESTING!!

In the words of Skeletor...Until we meet again!

### 2024-03-01

**OMG**
I have taken so long that FreeCodeCamp updated the test and I had more edge cases to deal with. Ugh.

So I was able to eventually figure this out. My biggest issue was that I would get one use case working and another would fail. Once I got all the times to work, the day iteration would fail. Then I got it all working and I had to create some if statements to determine what parameters were passed and based off that print different return statements. I am 100% sure there is a better way to do it, but I am so over this project. I learned A LOT though. I can't wait to use a library.

If I had to do this again, I think instead of using 24H time I would convert everything to minutes, add the duration, and then do the math to break it back down into days and hours. I also attempted to psuedo-code this one, without much luck. I did end up making a "truth" table to help figure out my return statements.

I'm over it. Budget app is next.
