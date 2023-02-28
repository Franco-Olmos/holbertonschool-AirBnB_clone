#!/usr/bin/python3
""" shebang """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """dddddddddddddddddddddddddddddd"""
        return True

    def do_EOF(self, arg):
        """dddddddddddddddddddddddddddddd"""
        return True

    def emptyline(self):
        """dddddddddddddddddddddddddddddd"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
