import cmd
import random
import string

class PasswordGenerator(cmd.Cmd):
    intro = "Welcome to the Password Generator! Type help or ? to list commands.\n"
    prompt = "> "

    def __init__(self):
        super().__init__()
        self.password = None
        self.usages = None
        self.db = DataBaseConnector("avitoparser", "avitoparser", "Bqe2ydB7", "31.31.192.187")
        db_control.connect()
        db_control.insert("keys", ("key", "usages"), ("test", "100"))
        db_control.stop()

    def do_generate_password(self, arg):
        """Generate a random password of the specified length. Usage: generate_password <length>"""
        try:
            length = int(arg)
            if length <= 0:
                raise ValueError
            self.password = self.generate_password(length)
            print(f"You generate password: {self.password}")
        except ValueError:
            print("Please enter a positive integer.")

    def do_set_password(self, arg):
        """Set a password. Usage: set_password <pass>"""
        self.password = arg
        print(f"You set password: {self.password}")

    def do_usages(self, arg):
        """Set usages for key. Usage: usages <length>"""
        try:
            usages = int(arg)
            if usages <= 0:
                raise ValueError
            self.usages = usages
            print(f"You set usages: {self.usages}")
        except ValueError:
            print("Please enter a positive integer.")

    def do_save(self, arg):
        """Save the password and usages to database. Usage: save"""
        if self.password and self.usages:
            print(self.password, self.usages)
            return True

    def do_exit(self, arg):
        """Exit the password generator. Usage: exit"""
        print("Goodbye!")
        return True

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    PasswordGenerator().cmdloop()
