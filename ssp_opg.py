import constants


# Raised when invalid acknowledgement from receiver were received.
class InvalidAcknowledgement(Exception):
    pass


# Called when wrong sensor reading.
class SensorReadingError(Exception):
    pass


def external_communication(command):
    while True:
        try:
            print(f"Command: {command}")

            response = input("Acknowledgement: ")

            if response == constants.EXTERNAL_ACKNOWLEDGEMENT_VALUE:
                print("Acknowledgement received")
                break
            else:
                raise InvalidAcknowledgement

        except InvalidAcknowledgement:
            print("Could not get the correct acknowledgement. Trying again.")


# external_communication(constants.START_WATER_DISPENSING)
# external_communication(constants.STOP_WATER_DISPENSING)

def internal_communication(address, command):
    print(f"Address: {address}, command: {command}")
    response = input("Response: ")

    return response


def get_sensor_reading(address):
    while True:
        response = internal_communication(address, constants.GET_SENSOR_VALUE)

        try:
            if response == constants.SENSOR_ERROR_READING:
                raise SensorReadingError
            else:
                try:
                    sensor_reading = int(response)
                    break
                except ValueError:
                    print("Not a number")

        except SensorReadingError:
            print("Error from sensor.")
    return sensor_reading


print(f"sensor reading: {get_sensor_reading(constants.SENSOR_ADDRESS)}")


