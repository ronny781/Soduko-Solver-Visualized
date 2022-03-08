

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#technologies-used">Technologies used</a></li>
      </ul>
    </li>
      <li>
      <a href="#getting-started">Getting started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#instructions">Instructions</a></li>
      </ul>
    </li>
    <li>
      <a href="#auto-solver">Auto Solver</a>
      <ul>
        <li><a href="#how-does-the-solver-work">How does the solver work?</a></li>
         <li><a href="#note">Auto solver implementation focus</a></li>
      </ul>
    </li>
       <li>
      <a href="#gui">GUI</a>
      <ul>
        <li><a href="#main-menu">Main Menu</a></li>
        <li><a href="#options-menu">Options Menu</a></li>
        <li><a href="#difficulty-menu">Difficulty Menu</a></li>
        <li><a href="#game-screen">Game Screen</a></li>
         <li><a href="#game-over-screen">Game Over Screen</a></li>
        <li><a href="#win-screen">Win Screen</a></li>
      </ul>
    </li>
     </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

A sudoku game that includes GUI consist with multiple screens,</br> supports 3 different difficulty levels, visualized auto solver and more.

![](https://media.giphy.com/media/bAL5IUsjvch93SaytW/giphy.gif)

The game starts after the user choose difficulty level,</br> then the program sends <b> GET request </b> to a <a href="https://github.com/bertoort/sugoku">sudoku board generator API</a> in order to fetch a </br> random board with the corresponding difficulty level.</br> The response received as <b> JSON </b> object that then gets parsed into a two-dimensional array.



### Technologies used:

* Python
* Pygame
* REST API

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites:</br>
Make sure you have installed python interpreter and pygame on your machine.</br>

### Instructions:</br>

Download the project and run the main.py file.</br>
For playing choose play on the main menu and select a difficulty level.</br>
To initiate the auto solver, press <b> 'SPACE' </b>.</br>
Note: to navigate backwards between screens, press <b> 'ESC' </b>


<p align="right">(<a href="#about-the-project">back to top</a>)</p>

<!-- Auto Solver -->
## Auto Solver

![](https://media.giphy.com/media/JdWDR7p4KMNyhJ8IWU/giphy.gif)

### How does the solver work?

The program first seeks an empty cell, then attempts to insert a valid number in the order of 1 to 9. </br>
The program does this until the puzzle is stuck. Then it runs a backtracking DFS search to "try out" the other possibilities,</br> eliminating those (and its children) that doesn't work.

### Note:
This project has been created for educational purposes only,</br>
and to visualize the backtracking in a "reasonable" speed for the human eye to watch.</br>
Therefore, there wasn't <b> any effort </b> of solving the board with efficient run time.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

## GUI

### Main Menu
<img src="images/main menu.png" height="450px" width="450px">

### Options Menu
<img src="images/options menu.png" height="450px" width="450px">

The number of "lives" (number of mistakes you can make) can be set between 1 to 7.</br>
The speed of the auto solver visualization can be set between 1 to 5, where 5 is the fastest (without delay).</br>
End game: if the player has run out of lives, then the <a href="#game-over-screen">game over screen</a> will be rendered.</br>
Else if the player has solved the sudoku, then the <a href="#win-screen"> winning screen </a> will be rendered

### Difficulty Menu
<img src="images/difficulty menu screen.png" height="450px" width="450px"></br>
There are 3 options here: EASY, MEDIUM, HARD 

### Game screen
<img src="images/game screen.png" height="450px" width="450px"></br>
The game screen features a clock and also renders left lives.

### Game Over screen
<img src="images/game over screen.png" height="450px" width="450px">


### Win screen
<img src="images/win screen.png" height="450px" width="450px">

<p align="right">(<a href="#about-the-project">back to top</a>)</p>



