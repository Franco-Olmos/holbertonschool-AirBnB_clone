#!/usr/bin/python3
""" shebang """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None
    classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
               'City': City, 'Amenity': Amenity, 'Place': Place,
               'Review': Review}

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
        if argv is not BaseModel:
            print("** class doesn't exist **")
    
    def do_show(self, argv):
        imput = args.split()
        if not imput:
            print("** class name missing **")
        if argv is not BaseModel:
            print("** class doesn't exist **")
        if len(argv) == 1:
            print("** instance id missing **")
        if __name__ == '__main__':
            HBNBCommand().cmdloop()

    def do_destroy(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
            return

        argument = arg.split()
        if not argument[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if len(argument) > 1:
            key = argument[0] + '.' + argument[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
            return
        if not arg.split()[0] in self.classes.keys():
            print("** class doesn't exist **")
            return
        if arg in self.classes.keys():
            for a in storage.all():
                print(str(a))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
