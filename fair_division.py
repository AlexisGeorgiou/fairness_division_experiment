import random
import numpy as np

n = 5 # number of agents
m = 10 # number of items
number_of_simulations = 1000000

def initialize_preference_matrix(n, m):
    #INPUT: n: (integer) number of agents
    #     : m: (integer) number of items
    #OUTPUT: preference_matrix (numpy array) a matrix with the preferences of each agent,
    #        the preferences of each agent are based on Borda rule, 
    #        so the agent ranks 1 the lowest preferred and m the most preferred. 
    preference_matrix = []
    for i in range(n):
        agent_preferences = random.sample(range(1, m+1), m)
        preference_matrix.append(agent_preferences)

    preference_matrix = np.array(preference_matrix)
    return preference_matrix


def initialize_preference_matrix_random_sum_to_1(n, m):
    #INPUT: n: (integer) number of agents
    #     : m: (integer) number of items
    #OUTPUT: preference_matrix (numpy array) a matrix with the preferences of each agent,
    #        the preferences of each agent are random numbers between 0 and 1, 
    #        and each row is normalized so that it sums to 1.

    preference_matrix = []
    for i in range(n):
        agent_preferences = np.random.rand(m)
        agent_preferences /= agent_preferences.sum() # Normalize so that the preferences sum to 1
        preference_matrix.append(agent_preferences)

    preference_matrix = np.array(preference_matrix)
    return preference_matrix


#Protocol
def run_my_protocol(preference_matrix, n, m):
    #Runs the protocol
    #INPUT: preference_matrix: (numpy array) a matrix with the preferences of each agent,
    #     : n: (integer) number of agents
    #     : m: (integer) number of items
    #OUTPUT: total_preferences (list), a list that includes the total score of every agent, 
    #                                  his score is the additive value of his preference every item he got

    # Randomize order of agents
    agent_order = list(range(n))
    random.shuffle(agent_order)

    # initialize list of total preference scores
    total_preferences = [0] * n


    # loop until all items are assigned
    for turn in range(m):
        #When every agent selects an item, we reverse the order list for the next "round"
        # print(turn % n)
        # print(agent_order[turn % n])
        #This will reverse the ordering after every round, no needed for round robin
        # if turn % n == 0:
        #     agent_order.reverse()

        # print(agent_order)
        #agent_i is the id of the agent "playing"
        agent_i = agent_order[turn % n]

        # Get the maximum value of the agent's row
        max_value = preference_matrix[agent_i].max()
        total_preferences[agent_i] += max_value

        # Get the item/column index of the maximum value in the agent's row
        col_idx = preference_matrix[agent_i].argmax()
        preference_matrix[:,col_idx] = 0 

    return total_preferences


if __name__ == '__main__':
    preferences = []
    preference_matrix_original = initialize_preference_matrix(n,m)
    print(preference_matrix_original)
    for i in range(number_of_simulations):
        # preference_matrix = initialize_preference_matrix(n,m)
        preference_matrix = preference_matrix_original.copy()
        total_preferences = run_my_protocol(preference_matrix, n, m)
        preferences.append(total_preferences)
    
    # Initialize a list to hold the sums
    sums = [0] * len(preferences[0])
    
    # Iterate through the lists and items
    for lst in preferences:
        for i, item in enumerate(lst):
            sums[i] += item
    sums = [x/number_of_simulations for x in sums]
    print(sums)
        

