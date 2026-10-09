class HannoiProvlem:

    # Definiamo lo stato come 3 tuple 
    # i dischi sono rappresentati dai numeri 3,2,1 
    # lo stato iniziale sarà necessariamente ((3,2,1),(),())

    def __init__(self):

        self.initial_state=((3,2,1),(),())
        self. goal_state=((),(),(3,2,1))


    def actions(self,state):

        # Restituiamo una tupla dove ogni azione è individuata da (palo_origine,palo_arrivo)
        #ricordando che nposso spostare solo l'ultimo  elemento [-1]

        actions=[]

        for i in range(3):
            for j in range(3):
            # i pali devono essere diversi
            #possiamo spostare solo se è vuoto o ha un numero piu alto 
                if not  (i==j):

                    if len(state[i])>0:
                        disk_value= state[i][-1] # il -1 restituisce l'ultimo elemento non devi ciclare per trovarlo !

                        if len(state[j])==0 or state[j][-1]> disk_value:
                            actions.append((i,j))

        return actions 


    def result(self,state,action):

        #ricorda che applichiamo ad un singolo stato una singola azione quindi in questo caso sarà un unico elemento di lista dal valore (i,J) 
        # gli stati devono essere restituiti come tuple 

        # in questo caso v rimossa il disco dalla tupla  i di origine e messo nella tupla j didestinazione

        new_state=[]

        piolo1 , piolo2 , piolo3 = state

        new_state=[list(piolo1),list(piolo2),list(piolo3)]

        i,j = action

        element=new_state[i].pop()
        new_state[j].append(element)

        return tuple( tuple(state) for state in new_state)

    
    def action_cost(self,state,action):

        return 1
    
    def is_goal(self,state):

        return state == self.goal_state