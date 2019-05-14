# Grid-problem-using-RL
Suppose that an agent is situated in the 4x3 environment as shown in Figure .  
Beginning in the start state, it must choose an action at each time step.  The interaction with the environment terminates when the agent 
reaches one of the goal states, marked +1 or -1.  We assume that the environment is fully observable, so that the agent always knows where 
it is. Following four actions in every state can be taken:  Up, Down, Left and Right.  However, the environment is stochastic, 
that means the action that you take may not lead you to desired state.  Each action achieves the intended effect with probability 0.8, but 
the rest of the time, the action moves the agent at right angles to the intended direction with equal probabilities.  Furthermore, if the 
agent bumps into a wall, it stays in the same square.  The immediate reward for moving to any state (s) except for the terminal states S+ 
is r(s)= -0.04.  And the reward for moving to terminal states is +1 and -1 respectively.  Find the value function corresponding to the 
optimal policy using value iteration

Below is a 4X3 grid with red color grid position representing -1 reward. Grid position 0 is the starting state and 11 is the goal state with reward +1
<br />
![](grid.jpg)

### Approach
First calculate the value for each action from the current state by using the value function and take the action which gives the maximum value (Bellman equation). This becomes our optimal action for that iteration in that state. In each iteration we check whether the previous iteration values of the states are equal to the corresponding current iteration value, if yes, then we stop, else iterate again.
