"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.
"""

from maze_env import Maze
from RL_brain import QLearningTable

def update():
    attempt_counter = 0  # Initialize the counter for attempts to find the optimal route
    optimal_found = False
    steps_per_attempt = []  # List to store the number of steps for each successful attempt

    for episode in range(100):
        # initial observation
        observation = env.reset()
        steps = 0  # Reset step counter for this attempt

        while True:
            # fresh env
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # Increment step counter
            steps += 1

            # break while loop when end of this episode
            if done:
                if reward == 1:  # Assuming reward of 1 is for reaching paradise which is the optimal route
                    optimal_found = True
                    steps_per_attempt.append(steps)  # Record the number of steps for this successful attempt
                    print(f'Successful route found with {steps} steps.')
                break

        attempt_counter += 1  # Increment the counter each episode

        if optimal_found:
            print(f'Optimal route found after {attempt_counter} attempts.')
            attempt_counter = 0  # Reset the counter after finding optimal route
            optimal_found = False  # Reset the flag for the next run

    # Print all successful attempts with their step counts
    print('Steps per successful attempt:', steps_per_attempt)

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
