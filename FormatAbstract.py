from abc import ABC, abstractmethod

class FormatAbstract(ABC):
    @abstractmethod
    def __init__(self):
        self.schedule

    def get_instance(self):
        '''
        Returns an object that is an instance of itself
        '''
        pass

    @abstractmethod
    def export(self, schedule):
        '''
        Exports a schedule object to a format
        '''
        pass