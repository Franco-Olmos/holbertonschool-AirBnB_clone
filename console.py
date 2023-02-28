#!/usr/bin/python3
""" shebang """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """ddddddd!"""
        return True

    def do_EOF(self, arg):
        """ddddd"""
        return True

    def do_emptyline(self):
        """ddddddd"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
