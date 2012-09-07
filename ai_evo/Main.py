'''
@author: Michael Smith, Akhil Kapoor
'''
from Evolution import Evolution
from matplotlib import pyplot as plt

class TronEvo(object):
    '''
    classdocs
    '''

    def __init__(self,params):
        '''
        Constructor
        '''
        
    def run(self):
        tronEvo = self.run_evolution()
        self.run_statistics(tronEvo)
        
    def run_evolution(self):
        tronEvo = Evolution(None)
        tronEvo.run()
        return tronEvo
        
    def run_statistics(self, tronEvo):
        
        stats = tronEvo.statistics
        ngen = tronEvo.ngenerations
        
        for i in range(4):
            plt.figure(i)
            plt.plot(range(ngen), stats[i][0], label='Minimum Weight Value')
            plt.plot(range(ngen), stats[i][0], label='Maximum Weight Value')
            plt.plot(range(ngen), stats[i][0], label='Mean Weight Value')
            plt.xlabel('Generation')
            plt.ylabel('Weight Value')
            plt.legend()
            plt.title('Final weight value of ' + str(stats[i][-1]))
            plt.show()