#!/usr/bin/python3
"""
Entry point of the command interpreter:
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing on space """
        print
    
    def do_EOF(self, line):
        """Quit the program  """
        return True

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    HBNBCommand().cmdloop()
