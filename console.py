#!/usr/bin/python3
"""
    Module or file used to run the console for the AirBnB_Clone
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    major_class = {
            "BaseModel":BaseModel,
            "User":User
            }

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
        if args[0] != "BaseModel":
            print("** class doesn't exit **")
        else:
            if len(args) == 1:
                print("** instance id missing **")
                return
            new_storage = storage.all()
            for key in new_storage.keys():
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
            if args[0] == "BaseModel":
                for key in new_storage.keys():
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
        if args[0] != "BaseModel":
            print("** class doesn't exit **")
        else:
            error = ["** instance id missing **",
                     "** attribute name missing **",
                     "** value missing **"]
            if len(args) < 4:
                print(error[len(args)-1])
                return
            new_storage = storage.all()
            check = list(args[3])
            try:
                if '.' in check:
                    args[3] = float(args[3])
                else:
                    args[3] = int(arg[3])
            except:
                for i in check:
                    if i in ('"', "'"):
                        check.remove(i)
                        args[3] = "".join(check)
            for key in new_storage.keys():
                new_base = new_storage[key]
                if args[1] == new_base.id:
                    if args[2] not in ['id', 'created_at', 'updated_at']:
                        setattr(new_base, args[2], args[3])
                        new_base.save()
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
