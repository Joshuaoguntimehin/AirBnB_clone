import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
