from HannoiProblem import HannoiProvlem
from path_search.search import Search
from path_search.strategies import RandomStrategy

problem = HannoiProvlem()

strategy = RandomStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()
if result is None:
    print('No solution found')
else:    
    print(f'Solution found with path cost {result.path_cost}')