# Greed Game
Precious gems are falling out of the sky! Unfortunately, so are huge rocks. Your goal is to collect as many gems (*) as you can while avoiding the rocks (o). Collecting gems will earn you fifty points, and running into rocks will make you lose fifty points too. How many points can you earn?

## Getting Started

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 cse210-04 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the cse210-04 folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cse210-04           (source code for game)
  +-- game              (specific game classes)
    +-- casting         (game artifacts and actor)
    +-- directing       (game director)
    +-- services        (keyboard and video services)
    +-- shared          (game color and point)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies

* Python 3.8.0
* Raylib Python CFFI 3.7

## Rules

- Players can move up, down, left and right:
- Player one moves using the W, S, A and D keys.
- Player two moves using the I, K, J and L keys.
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail...THE GAME IS OVER!

## Requirements

- The program must have a README file.
- The program must have at least 16 classes.
- Each module, class and method must have a corresponding comment.
- The game must remain generally true to the order of play described in the overview.

## Team

 Group name: team-01
- Aaron Bechtel
- Jared Malan
- Jessica Angulo
- Oscar Peterson
- Nayra Rebeca Ferreira