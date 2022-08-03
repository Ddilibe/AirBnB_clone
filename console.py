#!/usr/bin/python3
"""
    Module or file used to run the console for the AirBnB_Clone
"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt
        """
        pass

    def do_EOF(self, arg):
        """End OF File Command to exit the program\n """
        sys.exit()

    def do_quit(self, arg):
        """Quit command to exit the program\n """
        sys.exit()

    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
