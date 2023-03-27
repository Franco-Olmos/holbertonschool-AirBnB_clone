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
    dic_classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

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
        if not arg:
            print("** class name missing **")
        elif arg not in self.dic_classes:
            print("** class doesn't exist **")
        else:
            inst = self.dic_classes[arg]()
            storage.save()
            print(inst.id)
    
    def do_show(self, arg):
        """Add comment"""
        inputs = arg.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in self.dic_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + "." + inputs[1]
            all_inst = storage.all()
            if key in all_inst.keys():
                print(all_inst[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Add comment"""
        if len(arg) == 0:
            print("** class name missing **")
            return

        argument = arg.split()
        if not argument[0] in self.dic_classes.keys():
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
        inputs = arg.split()
        if len(inputs) > 0 and inputs[0] not in self.dic_classes.keys():
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            print([str(objects[obj]) for obj in objects])

    """def do_all(self, arg):
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.dic_classes.keys():
            print("** class doesn't exist **")
        else:
            print([str(a) for a in storage.all(arg).values()])"""

    """def do_update(self, arg):
        inputs = arg.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in self.dic_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        key = inputs[0] + "." + inputs[1]
        all_arg = storage.all()
        if key not in all_arg.keys():
            print("** no instance found **")
        elif len(inputs) < 3:
            print("** attribute name missing **")
        elif len(inputs) < 4:
            print("** value missing **")
        else:
            setattr(storage.all()[key], inputs[2], inputs[3])
            storage.save()"""

    def do_update(self, arg):
        inputs = arg.split()
        if not inputs:
            print("** class name missing **")
        elif inputs[0] not in self.dic_classes:
            print("** class doesn't exist **")
        elif len(inputs) < 2:
            print("** instance id missing **")
        else:
            key = inputs[0] + "." + inputs[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(inputs) < 3:
                print("** attribute name missing **")
            elif len(inputs) < 4:
                print("** value missing **")
            else:
                setattr(storage.all()[key], inputs[2], inputs[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
