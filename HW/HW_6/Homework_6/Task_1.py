"""
# HW6 - Task № 1
Create a TrafficLight class (traffic light) and define one color
attribute and a running method. The attribute is implemented as private.
As part of the method, implement switching traffic lights in modes: red,
yellow, green. The duration of the first state (red) is 7 seconds, the second
(yellow) - 2 seconds, the third (green) - at your discretion. Switching between
modes should be carried out only in the indicated order (red, yellow, green).
Test the example by creating an instance and calling the described method.
"""
from time import sleep


class TrafficLight:
    __color = ['RE', 'YELLOW', 'GREEN']

    def run(self):
        for i in range(3):
            print(f'Traffic light: {TrafficLight.__color[i]}')
            if i == 0 and TrafficLight.__color[i] == 'RED':
                sleep(7)
            else:
                print('Wrong light, should be RED')
                break
            if i == 1 and TrafficLight.__color[i] == 'YELLOW':
                sleep(2)
            else:
                print('Wrong light, should be YELLOW')
                break
            if i == 2 and TrafficLight.__color[i] == 'GREEN':
                sleep(6)
            else:
                print('Wrong light, should be GREEN')
                break


traffic = TrafficLight()
traffic1 = TrafficLight()
traffic.run()
traffic1.run()
