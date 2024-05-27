class RobotController:
    def __init__(self):
        self.water_sensor = WaterSensorCommunication(5989999)
        self.valve = ValveCommunication(464884)
        self.base = BaseCommunication(564847)

    def fill_tank(self):
        self.valve.open()
        self.base.open()
        while self.water_sensor.water_level() < 100:
            continue
        self.base.close()
        self.valve.close()


class Communication:
    def __init__(self, address):
        self.address = address

    def send(self, message):
        print(f"{self.address}: {message}")

    def recieve(self):
        recieve_data = input("Response: ")
        return recieve_data


class WaterSensorCommunication(Communication):
    def __init__(self, address):
        super().__init__(address)

    def water_level(self):
        self.send("Water reading")
        response = self.recieve()

        try:
            response = int(response)

            if response >= 0 and response <= 100:
                return response
            else:
                print("Fejl, tal mellem 0 og 100!")
                response = self.water_level()

        except ValueError:
            print("Fejl, ingen bogstaver!")
            response = self.water_level()

        return response


class ValveCommunication(Communication):
    def __init__(self, address):
        super().__init__(address)

    def open(self):
        self.send("Open valve")
        response = self.recieve()

        if response != "open":
            self.open()

        return True

    def close(self):
        self.send("Close valve")
        response = self.recieve()

        if response != "close":
            self.close()

        return True


class CommunicationExternal:
    def __init__(self, address):
        self.address = address

    def send(self, message):
        print(f"{self.address}: {message}")

    def recieve(self):
        recieve_data = input("Response: ")
        return recieve_data


class BaseCommunication(CommunicationExternal):
    def __init__(self, address):
        super().__init__(address)

    def open(self):
        self.send("Open base valve")
        response = self.recieve()

        if response != "open":
            self.open()

        return True

    def close(self):
        self.send("Close base valve")
        response = self.recieve()

        if response != "close":
            self.close()

        return True


if __name__ == "__main__":
    robot_controller = RobotController()
    robot_controller.fill_tank()



