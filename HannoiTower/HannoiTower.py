class HannoiTower:

    def __init__(self):
        self.goal_state=((0,0,0),(0,0,0),(1,2,3))
        self.initial_state=((1,2,3),(0,0,0),(0,0,0))

    def actions(self,state):

        state=list(list(e) for e in state)
        empty=[]
        occupied=[]

        actions=[]

        for i in range(len(state)):
            for j in  range (len(state[i])):
                if(state[i][j]==0):
                    empty.append([i,j])
                else:
                    occupied.append([i,j])

        temp_elem=None
        movable=[]
        for element in occupied:
            if(temp_elem==None):
                temp_elem=element
                movable.append(element)
            if(temp_elem[0]==element[0] ):
                temp_elem=element
            else:
                movable.append(element)
                temp_elem=element

        for element in movable:
   
            for empty_space in empty:
                element_tower=element[0]
                empty_space_tower=empty_space[0]
                if (element_tower!= empty_space_tower): #verifico che le due torri siano diverse 

                    element_location=element[1]
                    empty_element_location=empty_space[1]

                    if(empty_element_location == 2): #verifico se l'elemento vuoto selezionato sia un fondo torre 
                        actions.append((element,empty_space)) 

                    elif (empty_element_location>=0 and empty_element_location<3):
                            if((state[empty_space_tower][empty_element_location+1] > state[element_tower][element_location]) and (state[empty_space_tower][empty_element_location]==0)):
                                actions.append((element,empty_space))

        actions=tuple(tuple(tuple(e)for e in a)for a in actions)  


        return actions
    
    def result(self,state,action):
        
        tower0, tower1, tower2 =state

        towers=[list(tower0), list(tower1), list(tower2)]

        element_to_move=list(action[0])
        end_point=list (action[1])

        print(element_to_move)
        print(end_point)

        temp_elem=towers[element_to_move[0]][element_to_move[1]]
        towers[element_to_move[0]][element_to_move[1]]=0
        towers[end_point[0]][end_point[1]]=temp_elem
            
        state= tuple((tuple(tower0),tuple(tower1),tuple(tower2)))

        return state
    
    def is_goal(self,state):
        return state== self.goal_state
    
    def action_cost(self,action,state):
        return 1