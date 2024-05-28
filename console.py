#!/usr/bin/python3
"""The console script"""
import cmd
import sys
from models import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character."""
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass
class create_instance(class.name):
    if class_name == "":
        print("** class name missing **")
        return BaseModel
    elif class_name == "":
        print("** class doesn't exist **")
        return MyModel
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
