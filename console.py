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

    def do_create(self, arg):
        imput = args.split()
        if not imput:
            print("** class name missing **")
        if not:
            print("** class doesn't exist **")
    
    def do_show(

if __name__ == '__main__':
    HBNBCommand().cmdloop()
