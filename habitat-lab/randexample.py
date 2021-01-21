# based on example from habitat docs

import habitat
from habitat.sims.habitat_simulator.actions import HabitatSimActions
import cv2
import random


def transform_rgb_bgr(image):
    return image[:, :, [2, 1, 0]]


#choose a random action
def random_action():
    act = random.randrange(3)
    if act == 0:
        print("action: FORWARD")
        action = HabitatSimActions.MOVE_FORWARD
    elif act == 1: 
        action = HabitatSimActions.TURN_LEFT
        print("action: LEFT")
    elif act == 2: 
        action = HabitatSimActions.TURN_RIGHT
        print("action: RIGHT")
    elif act == 3: 
        action = HabitatSimActions.STOP
        print("action: FINISH")
    return action

def example():
    env = habitat.Env(
        config=habitat.get_config("configs/tasks/pointnav.yaml")
    )

    print("Environment creation successful")
    observations = env.reset()
    print("Destination, distance: {:3f}, theta(radians): {:.2f}".format(
        observations["pointgoal_with_gps_compass"][0],
        observations["pointgoal_with_gps_compass"][1]))
    cv2.imshow("RGB", transform_rgb_bgr(observations["rgb"]))

    print("Agent stepping around inside environment.")

    count_steps = 0
    while not env.episode_over:
        action = random_action()
        observations = env.step(action)
        count_steps += 1

        print("Destination, distance: {:3f}, theta(radians): {:.2f}".format(
            observations["pointgoal_with_gps_compass"][0],
            observations["pointgoal_with_gps_compass"][1]))
        cv2.imshow("RGB", transform_rgb_bgr(observations["rgb"]))

    print("Episode finished after {} steps.".format(count_steps))

    if (
        action == HabitatSimActions.STOP
        and observations["pointgoal_with_gps_compass"][0] < 0.2
    ):
        print("you successfully navigated to destination point")
    else:
        print("your navigation was unsuccessful")


if __name__ == "__main__":
    example()
