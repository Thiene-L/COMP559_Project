from maze_env import Maze
from RL_brain import SarsaTable

def update():
    attempt_counter = 0  # Initialize the counter for attempts to find the optimal route
    steps_per_attempt = []  # List to store the number of steps for each successful attempt
    optimal_found = False

    for episode in range(100):
        # initial observation
        observation = env.reset()
        steps = 0  # Reset step counter for this attempt

        # RL choose action based on observation
        action = RL.choose_action(str(observation))

        while True:
            # fresh env
            env.render()

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL choose action based on next observation
            action_ = RL.choose_action(str(observation_))

            # RL learn from this transition (s, a, r, s', a') ==> Sarsa
            RL.learn(str(observation), action, reward, str(observation_), action_)

            # swap observation and action
            observation = observation_
            action = action_

            # Increment step counter
            steps += 1

            # break while loop when end of this episode
            if done:
                if reward == 1:  # Assuming a reward of 1 is for reaching paradise, the optimal route
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
    RL = SarsaTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
