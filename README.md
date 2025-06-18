# Ball Trajectory Game
---
### Overview

This Python project is a simple game built using Pygame, where the player needs to throw a ball into a basket by selecting the correct trajectory and force. The game involves physics calculations, such as gravity and ball movement, making it an engaging way to practice your aim and test your understanding of projectile motion.

The goal of the game is to adjust the trajectory (angle) and set the right force (velocity) to successfully score the ball into the basket.

### Features

- **Interactive controls:** Players can control the trajectory and force applied to the ball.
- **Physics-based movement:** The game simulates real-world physics, including projectile motion and gravity.
- **Simple visuals:** The game uses basic 2D graphics to represent the ball, basket, and environment.
- **Score tracking:** Players can keep track of their successful throws.

### GamePlay

![While Shooting]<img width="1012" alt="Screenshot 2025-06-18 at 13 31 03" src="https://github.com/user-attachments/assets/9e7f0ecf-d060-4426-93cf-eeef64c6dd8f" />

### How It Works

The game uses Pygame, a Python library that allows you to build games and multimedia applications. The ball is launched based on the force and angle set by the player, and its movement is influenced by gravity, which pulls it downward as it travels through the air.

### Key Components:
- **Ball:** A ball object that is launched with an initial velocity and angle, following a parabolic trajectory.
- **Basket:** A stationary basket positioned at a fixed location, where the ball must land.
- **Force & Trajectory:** The player controls these two variables to launch the ball at different angles and speeds.
- **Gravity:** A constant force applied to the ball during its flight.

### Run the game
``` game.py ```
