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

    def do_create(self, argv):
        imput = args.split()
        if not imput:
            print("** class name missing **")
        if argv not is BaseModel:
            print("** class doesn't exist **")
    
    def do_show(self, argv):
        imput = args.split()
        if not imput:
            print("** class name missing **")
        if argv not is BaseModel:
            print("** class doesn't exist **")
        if len(argv) == 1:
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
