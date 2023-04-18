"""
    Name:
    Surname:
    Student ID:
"""


from tree_search_agents.TreeSearchAgent import *
from tree_search_agents.PriorityQueue import PriorityQueue
import time
from math import sqrt

class AStarAgent(TreeSearchAgent):
    def run(self, env: Environment) -> (List[int], float, list):
        """
            You should implement this method for A* algorithm.

            DO NOT CHANGE the name, parameters and output of the method.
        :param env: Environment
        :return: List of actions and total score
        """
        # total_score = []
        # print(f"pq before {pq.queue}")
        # print(pq.queue)
        pq = PriorityQueue()  # priority queue to keep track of the frontier
        pq.enqueue(([env.to_state(env.current_position)], [], 0), -self.get_heuristic_manhattan_goal(env, env.to_state(env.current_position))) # insert the starting node with a priority of 0
        visited = set()  # set to keep track of explored nodes
        while not pq.is_empty():
            # print(f"whole queue {pq.queue}")
            # print_queue(pq.queue, env)
            # print(pq.queue)
            curr_obj = pq.dequeue()
            curr_state = curr_obj[0][-1] # returns current state
            env.set_current_state(curr_state)
            # print(f"where am i {env.current_position}")
            # print(f"curr_state {curr_obj}")
            curr_reward = curr_obj[2]
            # print(f"pq {pq.queue}")
            if env.is_done(env.current_position):
                # print(f"get node type {env.get_node_type(env.to_position(curr_state))}")
                return curr_obj[1], curr_obj[2], curr_obj[0]
            # elif len(results) == len(env.get_goals()):
            #     return max(results, key=lambda x: x[2])
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
                    new_score = new_reward + curr_reward # keeps total score
                    new_pri = -self.get_heuristic_manhattan_goal(env, next_state) + new_score # calculates straight_line distance and adds new_reward to it
                    pq.enqueue((new_path, new_action_list, new_score), new_pri)
                env.set_current_state(curr_state)
        # print(f"results {results}")
        # for result in results:
            

    ###### ANOTHER FUNCTION TO RUN IN ######
    # def run(self, env: Environment) -> (List[int], float, list):
    #     """
    #         You should implement this method for A* algorithm.

    #         DO NOT CHANGE the name, parameters and output of the method.
    #     :param env: Environment
    #     :return: List of actions and total score
    #     """
    #     # total_score = []
    #     # print(f"pq before {pq.queue}")
    #     # print(pq.queue)
    #     results = []
    #     for goal in env.get_goals():
    #         env.reset()
    #         pq = PriorityQueue()  # priority queue to keep track of the frontier
    #         pq.enqueue(([env.to_state(env.current_position)], [], 0), -self.get_heuristic(env, env.to_state(env.current_position), goal)) # insert the starting node with a priority of 0
    #         visited = set()  # set to keep track of explored nodes
    #         print(f"goal position {env.to_position(goal)}")
    #         while not pq.is_empty():
    #             # print(f"whole queue {pq.queue}")
    #             # print_queue(pq.queue, env)
    #             # print(pq.queue)
    #             curr_obj = pq.dequeue()
    #             curr_state = curr_obj[0][-1] # returns current state
    #             env.set_current_state(curr_state)
    #             # print(f"where am i {env.current_position}")
    #             # print(f"curr_state {curr_obj}")
    #             curr_reward = curr_obj[2]
    #             # print(f"pq {pq.queue}")
    #             if curr_state == goal:
    #                 # print(f"get node type {env.get_node_type(env.to_position(curr_state))}")
    #                 results.append((curr_obj[1], curr_obj[2], curr_obj[0]))
    #                 break
    #             # elif len(results) == len(env.get_goals()):
    #             #     return max(results, key=lambda x: x[2])
    #             print(f"curr node {curr_state}")
    #             # print(f"i am in position of {env.to_position(curr_state)}")
    #             # print(f"my action to achieve {curr_obj[1]}")
    #             visited.add(curr_state)
    #             for action in range(4):
    #                 next_state, new_reward, is_done = env.move(action)
    #                 # print(f"rewards {new_reward}")
    #                 # print(f"curr state: {curr_state} next_state {next_state}")
    #                 # if next_state not in visited and env.get_node_type(env.to_position(next_state)) != "D":
    #                 if next_state not in visited:
    #                     # print(f"what is my node type {env.get_node_type(env.to_position(next_state))}")
    #                     new_path = curr_obj[0].copy()
    #                     new_path.append(next_state)
    #                     new_action_list = curr_obj[1].copy()
    #                     new_action_list.append(action)
    #                     new_pri = -self.get_heuristic(env, next_state, goal) + new_reward # calculates straight_line distance and adds new_reward to it
    #                     new_score = new_reward + curr_reward # keeps total score
    #                     pq.enqueue((new_path, new_action_list, new_score), new_pri)
    #                 env.set_current_state(curr_state)
    #     # print(f"results {results}")
    #     # for result in results:
            
    #     return max(results, key=lambda x: x[1]) # return maximum rewarded object


    def get_heuristic(self, env: Environment, state: int, goal:int) -> float:
        """
            You should implement your heuristic calculation for A *as

            DO NOT CHANGE the name, parameters and output of the method.

            Note that you can use kwargs to get more parameters :)
        :param env: Environment object
        :param state: Current state
        :param kwargs: More parameters
        :return: Heuristic score
        """ 
        # below is manhattan distance implementation
        goal_pos = env.to_position(goal)
        curr_pos = env.to_position(state)
        return (abs(goal_pos[0] - curr_pos[0]) + abs(goal_pos[1] - curr_pos[1]))
    
    def get_heuristic_manhattan_goal(self, env: Environment, state:int) -> int:
        return min(abs(env.to_position(goal)[0] - env.to_position(state)[0]) + abs(env.to_position(goal)[1] - env.to_position(state)[1]) for goal in env.get_goals())
    def get_heuristic_min_euclidian(self, env: Environment, state:int) -> float:
        return min(sqrt((env.to_position(goal)[0] - env.to_position(state)[0])**2 + (env.to_position(goal)[1] - env.to_position(state)[1])**2) for goal in env.get_goals())
    @property
    def name(self) -> str:
        return "AStar"
