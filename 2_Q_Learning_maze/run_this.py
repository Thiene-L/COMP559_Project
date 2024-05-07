from maze_env import Maze
from RL_brain import QLearningTable
import matplotlib.pyplot as plt

def update():
    attempt_counter = 0
    success_counter = 0
    steps_per_success = []

    for episode in range(100):
        observation = env.reset()
        steps = 0

        while True:
            env.render()

            action = RL.choose_action(str(observation))

            observation_, reward, done = env.step(action)

            RL.learn(str(observation), action, reward, str(observation_))

            observation = observation_

            steps += 1

            if done:
                if reward == 1:
                    success_counter += 1
                    steps_per_success.append(steps)
                    print(f'Successful route found with {steps} steps.')
                break

        attempt_counter += 1

        if success_counter == 20:
            print(f'Optimal route found after {success_counter} successes.')
            break

    print('Steps per successful attempt:', steps_per_success)
    print('Total number of attempts:', attempt_counter)

    plt.figure(figsize=(10, 5))
    plt.plot(steps_per_success, marker='o', linestyle='-')
    plt.title('Steps per Successful Attempt')
    plt.xlabel('Success Count')
    plt.ylabel('Steps')
    plt.grid(True)
    plt.show()

    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
