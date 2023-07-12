class vehicle:
    def start(self):
        print("vehicle started")

    def stop(self):
        print("vehicle stopped")


class car(vehicle):
    def start(self):
        print("car started")

    def stop(self):
        print("car stopped")


class motorcycle(vehicle):
    def start(self):
        print("motorcycle started")

    def stop(self):
        print("motorcycle stopped")


if __name__ == '__main__':
    veh = vehicle()
    ca = car()
    motor = motorcycle()
    veh.start()
    ca.stop()
    motor.stop()
