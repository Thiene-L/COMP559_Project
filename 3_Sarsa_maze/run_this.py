from maze_env import Maze
from RL_brain import SarsaTable
import matplotlib.pyplot as plt

def update():
    attempt_counter = 0
    success_counter = 0
    steps_per_success = []

    for episode in range(100):
        observation = env.reset()
        steps = 0
        action = RL.choose_action(str(observation))

        while True:
            env.render()

            observation_, reward, done = env.step(action)
            action_ = RL.choose_action(str(observation_))

            RL.learn(str(observation), action, reward, str(observation_), action_)

            observation = observation_
            action = action_

            steps += 1

            if done:
                attempt_counter += 1
                if reward == 1:
                    success_counter += 1
                    steps_per_success.append(steps)
                    print(f'Successful route found with {steps} steps.')
                break

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
    RL = SarsaTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()
