import time


class TrafficLight:
    __color = "red"

    def running(self):

        for i in range(1, 10000, 1):

            if (i - 1) % 3 == 0:
                print(TrafficLight.__color)
                time.sleep(7)

            if (i + 1) % 3 == 0:
                print(f"yellow")
                time.sleep(2)

            if i % 3 == 0:

                print(f"green")
                time.sleep(10)

a = TrafficLight()
a.running()
