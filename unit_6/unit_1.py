import time


class TrafficLight:
    __color = "red"

    def running(self):

        for i in range(1, 10000, 1):

            if (i - 1) % 3 == 0:
                print(f"red")
                time.sleep(1)

            if (i + 1) % 3 == 0:
                print(f"yellow")
                time.sleep(2)

            if i % 3 == 0:
                time.sleep(2)
                print(f"green")


a = TrafficLight()
a.running()
