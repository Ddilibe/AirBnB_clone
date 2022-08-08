#!/usr/bin/python3
"""
    Module or file used to run the console for the AirBnB_Clone
"""
import re
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    major_class = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }
    major_command = ['all', 'create', 'update', 'destroy', 'show', 'count']

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

    def do_create(self, args):
        """Create command used to create an instance of the BaseModel\n"""
        args = args.split(" ")
        if args[0] == "":
            print("** class name missing **")
        else:
            if args[0] in self.major_class:
                new_model = self.major_class[args[0]]()
                print(new_model.id)
                new_model.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Show command for printing the string representation of an \
instance based in the class name and id\n"""
        if not args:
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in self.major_class:
            print("** class doesn't exit **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            args[1] = list(args[1])
            for i in args[1]:
                if i in ('"', "'"):
                    args[1].remove(i)
            args[1] = ''.join(args[1])
            new_storage = storage.all()
            for key in new_storage.keys():
                new_key = key.split(".")[0]
                if new_key == args[0]:
                    new_base = new_storage[key]
                    if args[1] == new_base.id:
                        print(new_storage[key])
                        return
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy Command deletes an instance \
based on the class name and id\n"""
        if not args:
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in self.major_class:
            print("** class doesn't exit **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            args[1] = list(args[1])
            for i in args[1]:
                if i in ('"', "'"):
                    args[1].remove(i)
            args[1] = ''.join(args[1])
            new_storage = storage.all()
            for key in new_storage.keys():
                new_key = key.split(".")[0]
                if new_key == args[0]:
                    new_base = new_storage[key]
                    if args[1] == new_base.id:
                        del storage.all()[key]
                        storage.save()
                        return
            print("** no instance found **")

    def do_all(self, args):
        """All command prints all respective representation of all instances \
based or not on the class name \n"""
        args = args.split(" ")
        new_storage, new_thing = storage.all(), []
        if len(args) > 0 and args[0] != "":
            if args[0] in self.major_class:
                for key in new_storage.keys():
                    new_key = key.split(".")[0]
                    if new_key == args[0]:
                        new_thing.append(new_storage[key].__str__())
            else:
                print("** class doesn't exist **")
                return
        else:
            for key in new_storage.keys():
                new_thing.append(new_storage[key].__str__())
        print(new_thing)

    def do_update(self, args):
        """Update command updates an instance based on the class name by \
adding or updating attribute\n"""
        if not args:
            print("** class name missing **")
            return
        types, args = [int, str], args.split(" ")
        if args[0] not in self.major_class:
            print("** class doesn't exit **")
        else:
            error = ["** instance id missing **",
                     "** attribute name missing **",
                     "** value missing **"]
            if len(args) < 4:
                print(error[len(args)-1])
                return
            args[1] = list(args[1])
            for i in args[1]:
                if i in ('"', "'"):
                    args[1].remove(i)
            args[1].pop()
            args[1] = ''.join(args[1])
            new_storage = storage.all()
            check = list(args[3])
            try:
                if '.' in check:
                    args[3] = float(args[3])
                else:
                    args[3] = int(arg[3])
            except Exception:
                args[3].strip(", ")
            for key in new_storage.keys():
                new_key = key.split(".")[0]
                if new_key == args[0]:
                    new_base = new_storage[key]
                    if args[1] == new_base.id:
                        if args[2] not in ['id', 'created_at', 'updated_at']:
                            setattr(new_base, args[2], args[3])
                            new_base.save()
                            return
            print("** no instance found **")

    def bracket(self, s: str) -> bool:
        """Method for syntax confirmation """
        pattern = r'[A-Za-z]+\.[a-z]+\(([*]{0,1}|[\w,\'\'+\.{}\s-])+\)'
        if re.fullmatch(pattern, s) is None:
            return False
        return True

    def precmd(self, line):
        """The Hook method executed just the before the command \
        is interpreted"""
        if self.bracket(line):
            first = line.split('.')
            refe = first[1].split('(')
            last = refe[1].split(')')
            if first[0] in self.major_class and refe[0] in self.major_command:
                line = refe[0] + ' ' + first[0] + ' ' + last[0]
        return line

    def do_count(self, args):
        """Count command used to retrive the number of \
instances of a class\n"""
        if not args:
            print("** class name missing **")
            return
        args = args.split(" ")
        if args[0] not in self.major_class:
            print("** class doesn't exit **")
        else:
            new_storage, count = storage.all(), 0
            for key in new_storage.keys():
                new_key = key.split(".")[0]
                if new_key == args[0]:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
