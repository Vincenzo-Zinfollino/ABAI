
#possiamo supporre che lo 0 sia l'elemento vuoto 

UP="UP"
DOWN="DOWN"
LEFT="LEFT"
RIGHT="RIGHT"

moves={
     UP: -1,
     DOWN :+1,
     LEFT: -1,
     RIGHT: +1
}

class EightProblem:

    def __init__(self):

        #self.initial_state=((5,2,7),(8,4,0),(1,3,6))
        self.initial_state=((1,2,3),(4,5,6),(7,0,8))
        self.goal_state=((1,2,3),(4,5,6),(7,8,0))

    def find_empty(self,state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                    if state[i][j]==0:
                        position=[i,j]
                        break
        return position

    def actions(self, state):
            position = self.find_empty(state)
            row = position[0]
            col = position[1]
            possible_action = []

            # Controllo movimento UP (riga - 1)
            if row - 1 >= 0:
                possible_action.append(UP)
                
            # Controllo movimento DOWN (riga + 1)
            if row + 1 < len(state):
                possible_action.append(DOWN)
                
            # Controllo movimento LEFT (colonna - 1)
            if col - 1 >= 0:
                possible_action.append(LEFT)
                
            # Controllo movimento RIGHT (colonna + 1)
            if col + 1 < len(state[0]):
                possible_action.append(RIGHT)
                
            return possible_action




    def result(self,state,action):

        initial_state_list=[list(x) for x in state ]
       
        position=self.find_empty(initial_state_list)
        temp_elem=0

        if action== UP:
            # se siamo in UP o DOWN varia la i
            temp_elem=initial_state_list[position[0]+moves[UP]][position[1]]
            initial_state_list[position[0]+moves[UP]][position[1]]=0
            initial_state_list[position[0]][position[1]]=temp_elem
        elif action==DOWN:
            temp_elem=initial_state_list[position[0]+moves[DOWN]][position[1]]
            initial_state_list[position[0]+moves[DOWN]][position[1]]=0
            initial_state_list[position[0]][position[1]]=temp_elem
        elif action==RIGHT:
            #se siamo in LEFT o RIGHT muoviamo la j
            temp_elem=initial_state_list[position[0]][position[1]+moves[RIGHT]]
            initial_state_list[position[0]][position[1]+moves[RIGHT]]=0
            initial_state_list[position[0]][position[1]]=temp_elem
        elif action==LEFT:
            temp_elem=initial_state_list[position[0]][position[1]+moves[LEFT]]
            initial_state_list[position[0]][position[1]+moves[LEFT]]=0
            initial_state_list[position[0]][position[1]]=temp_elem

        print("state "+str(initial_state_list))
        return (tuple(tuple(x) for x in initial_state_list ))


    def action_cost(self,state,action):
        return 1

    def is_goal(self,state):
        return state == self.goal_state