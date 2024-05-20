import cmd

class baseclass(cmd.Cmd):
    def do_exit(self):
        print("exitting in progress")
        return true

    def do_empty(self):
        print("alternative exit from program")
        return true

    if __name__ == '__main__':
    HBNBCommand().cmdloop()
