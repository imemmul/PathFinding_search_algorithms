"""
    Name: Emir
    Surname: Ulurak
    Student ID: S020526
"""

from tree_search_agents.TreeSearchAgent import *
from tree_search_agents.PriorityQueue import PriorityQueue
import time

def print_path_list(path:list, env: Environment):
    temp_p = []
    for p in path:
        temp_p.append(env.to_position(p))

def print_queue(queue, env: Environment):
    # print(f"queue {queue}")
    for i in queue:
        print(f"Position: {print_path_list(i[0][0], env)} | Total Score: {i[0][2]} | Action List {i[0][1]}")

class UCSAgent(TreeSearchAgent):
    def run(self, env: Environment) -> (List[int], float, list):
        """
            You should implement this method for Uniform Cost Search algorithm.
            - **UP**       :   0
            - **LEFT**     :   1
            - **DOWN**     :   2
            - **RIGHT**    :   3
            DO NOT CHANGE the name, parameters and output of the method.
        :param env: Environment
        :return: List of actions and total score
        """
        # print(env.to_position(14))
        pq = PriorityQueue()  # priority queue to keep track of the frontier
        pq.enqueue(([env.to_state(env.current_position)], [], 0), 0) # insert the starting node with a priority of 0
        # total_score = []
        # print(f"pq before {pq.queue}")
        # print(pq.queue)
        visited = set()  # set to keep track of explored nodes
        while not pq.is_empty():
            # print(f"whole queue {pq.queue}")
            # print_queue(pq.queue, env)
            # print(pq.queue)
            curr_obj = pq.dequeue()
            # print(f"where am i {env.current_position}")

            curr_state = curr_obj[0][-1] # returns current state
            env.set_current_state(curr_state)
            
            # print(f"curr_state {env.to_position(curr_state)}")
            curr_reward = curr_obj[2]
            if env.is_done(env.to_position(curr_state)):
                # print(f"get node type {env.get_node_type(env.to_position(curr_state))}")
                # for node in curr_obj[0]:
                #     print(f"positions {env.to_position(node)}")
                return curr_obj[1], curr_obj[2], curr_obj[0]
            # print(f"curr node {curr_node}")
            # print(f"i am in position of {env.to_position(curr_state)}")
            # print(f"my action to achieve {curr_obj[1]}")
            visited.add(curr_state)
            for action in range(4):
                next_state, new_reward, is_done = env.move(action)
                # print(f"rewards {new_reward}")
                # print(f"curr state: {curr_state} next_state {next_state}")
                # if next_state not in visited and env.get_node_type(env.to_position(next_state)) != "D":
                if next_state not in visited:
                    # print(f"what is my node type {env.get_node_type(env.to_position(next_state))}")
                    new_path = curr_obj[0].copy()
                    new_path.append(next_state)
                    new_action_list = curr_obj[1].copy()
                    new_action_list.append(action)
                    new_score = curr_reward + new_reward
                    pq.enqueue((new_path, new_action_list, new_score), new_score)
                # elif next_state in env.get_goals():
                #     curr_obj[1].append(action)
                #     return curr_obj[1], curr_obj[2] + new_reward, curr_obj[0]
                # elif is_done and next_state not in env.get_goals():
                #     pass
                env.set_current_state(curr_state)
            
    @property
    def name(self) -> str:
        return "UCS"
