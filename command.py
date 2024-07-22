from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver class
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# Concrete command classes
class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker class
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print("Command not found")

# Usage
light = Light()
turn_on_command = TurnOnCommand(light)
turn_off_command = TurnOffCommand(light)

remote_control = RemoteControl()
remote_control.register_command("on", turn_on_command)
remote_control.register_command("off", turn_off_command)

remote_control.execute_command("on")  # Output: Light is on
remote_control.execute_command("off")  # Output: Light is off
remote_control.execute_command("toggle")  # Output: Command not found