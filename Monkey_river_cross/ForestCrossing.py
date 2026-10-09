class ForestCrossing:
    def __init__(self):
        self.initial_state= (4,0,0)  # (number of monkeys on the left bank, number of monkeys on the right bank, position of the boat)
        self.goal_state = (0,4,1)  # (number of monkeys on the left bank, number of monkeys on the right bank, position of the boat)
    
    def actions(self,state):
        action=[]

        torch_position=state[2]
        #poichè la torcia può essere solo 0 o 1 seleziona automaticamente la sponda scegliendo se è l'elemento 0 o 1 dello stato 
        movable_monkey=state[torch_position]

        if movable_monkey>0:
            action.append([1, torch_position])
        if movable_monkey>1:
            action.append([2,torch_position])

        return action

    def result(self, state,action):

        new_state=list(state)

        n_monkey_to_move=action[0]
        torch_side=action[1]

        if(torch_side==0):
            new_state[0]-=n_monkey_to_move
            new_state[1]+=n_monkey_to_move
            new_state[2]= 1
        elif(torch_side==1):
            new_state[1]-=n_monkey_to_move
            new_state[0]+=n_monkey_to_move
            new_state[2]= 0
        else:
            raise ValueError("Valore di torcia errato")
        
        return tuple(new_state)
    
    def action_cost(self,state,action):
        return 1

    def is_goal(self,state):
        return state == self.goal_state