RIEMPIRE= "Riempire"
SVUOTARE= "Svuotare"
TRAQVASARE= "Travasare"

class WaterJung:

    def __init__(self):

        #lo stato rappresenta quanta acqua è presente nella jar 

        self.size= [8, 5 ,3]
        self.initial_state= (0,0,0)
        self.goal=6


    def actions(self,state):

        actions=[]
        for i in range(len(state)):
            if (state[i]>0):
                actions.append([SVUOTARE,i])

            if state[i]< self.size[i]:
                actions.append([RIEMPIRE,i])

            for j in range(len(state)):
                if i != j :
                    if (state[i]>0 and state[j]<self.size[j]):
                        actions.append([TRAQVASARE,i,j])

        return actions

    def result(self,state,action): 

        state=list(state)

        act, i , *_=action

        if act==RIEMPIRE:
            state[i]=self.size[i]
        if act==SVUOTARE:
            state[i]=0
        if act== TRAQVASARE:
            act, i , j=action
            quant=min(self.size[i],self.size[j]-state[j])
            state[i]-= quant
            state[j]+= quant

        return tuple(state)


    def action_cost(self,state,action):

        act, i , *j=action

        if act==SVUOTARE:
            return state[i]
    
        return 1
        

    def is_goal(self,state):

        for i in state:
            if i == self.goal:
                return True

        return False

