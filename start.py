import signal
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor


from action import Loadrecord_Get


def keyboardInterruptHandler(signal, frame):
    try:
        global event
        global log
        event.set()
    except Exception as e:
        print(e)

def presence(stop_event):
    try:
        # global log
        # global event
        # print('start:', event)
        presence = Loadrecord_Get(stop_event)
        presence.start()
    except Exception as e:
        print("hi")
        print(e)
        event.set()
        raise
     
if __name__ == '__main__':
    try:
        global event
        global log
        event = Manager().Event()
        print('start event:', event)
        signal.signal(signal.SIGINT, keyboardInterruptHandler)
        with ProcessPoolExecutor() as executor:
            task1 = executor.submit(presence, event)
    except Exception as e:
        
        print(e)
        event.set()
        
        