from abc import ABCMeta, abstractmethod
import time
class Base_Load(metaclass=ABCMeta):
    
    def __init__(self, stop_event):
        try:
            print('look')
            self.stop_event = stop_event
        except Exception as e:
            pass
    def start(self):
        try:
            while self.stop_event.is_set() == False:
                self.process('HI')
                time.sleep(60)
        except Exception as e:
            pass
            
    
    
    
    @abstractmethod    
    def process(self,query):
        #print('hi')
        pass
    