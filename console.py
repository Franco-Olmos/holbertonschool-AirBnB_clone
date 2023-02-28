#!/usr/bin/python3
""" shebang """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    file = None

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def do_emptyline(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
