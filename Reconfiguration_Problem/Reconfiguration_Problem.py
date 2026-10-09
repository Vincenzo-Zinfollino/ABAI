import copy


class Reconfiguration_Problem:

    def __init__(self):
        # 0 is the empty tile 
        self.initial_state=( (5,2,7),(8,4,0),(1,3,6))
        self.goal_state=( (1,2,3),(4,5,6),(7,8,0))


    def actions(self,state):
        state=[list(r)for r in state]

        x=None
        y=None
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j]==0:
                    x=j
                    y=i

        actions=[]

        if x is None or y is None:
                raise ValueError(f"Errore critico: Zero non trovato nello stato!\nStato ricevuto: {state}")

            # Controllo i 4 confini della griglia in modo esplicito
        if x > 0: 
            actions.append((-1, 0)) # Può muoversi a sinistra
        if x < len(state[0]) - 1: 
            actions.append((1, 0))  # Può muoversi a destra
        if y > 0: 
            actions.append((0, -1)) # Può muoversi in alto
        if y < len(state) - 1: 
            actions.append((0, 1))  # Può muoversi in basso

        return tuple(actions)



    def result(self,state,action):
                    
        element=list(action)
        
        #print("element "+str(element))

        new_state=[]
        state=[list(r)for r in state]
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j]==0:
                    x=j
                    y=i

        #so che l'elemento  [i,j] è zero quindi posso sommare il valore che teovo nella casella  [i+action[0],j+action[i]]

        temp_state_x=copy.deepcopy(state)
        temp_element=0
        if(element[0]!= 0):
            temp_element=temp_state_x[y][x+element[0]]
            temp_state_x[y][x+element[0]]=0
            temp_state_x[y][x]=temp_element
            new_state=temp_state_x

        #move y
        temp_state_y=copy.deepcopy(state)
        if(element[1] != 0):
            temp_element=temp_state_y[(y+element[1])][x]
            temp_state_y[(y+element[1])][x]=0
            temp_state_y[y][x]=temp_element
            new_state=temp_state_y

        #new_state = tuple(tuple(tuple(row) for row in matrix) for matrix in new_state)
        new_state=tuple(tuple(s) for s in new_state)

        return new_state
    

    def action_cost(self,state,action):
        return 1
    
    def is_goal(self,state):
        return state==self.goal_state