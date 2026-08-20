class Facebook:
    usernames = {}

    def __init__(self, name, username, age, gender, psd):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd
        self.friends = 0
        self.following = 0
        self.friends_list = []
        self.logged = False

        Facebook.usernames[username] = self

    @staticmethod
    def validate_password(psd):
        if len(psd) < 8:
            return False
        if not any(i.isupper() for i in psd):
            return False
        if not any(i.islower() for i in psd):
            return False
        if not any(i.isdigit() for i in psd):
            return False
        return True

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")

        while True:
            username = input("Enter your username: ")

            if username in Facebook.usernames:
                print("Username already registered. Try another one")
            else:
                break

        # Password validation using method
        while True:
            psd = input("Enter Your Password: ")

            if cls.validate_password(psd):
                print("Password is valid")
                break
            else:
                print("Invalid Password")
                print("Password must contain:")
                print("- At least 8 characters")
                print("- At least one uppercase letter")
                print("- At least one lowercase letter")
                print("- At least one digit")

        age = input("Enter your age: ")
        gender = input("Enter your gender(Male/Female): ")

        return cls(name, username, age, gender, psd)

    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your username: ")
            password = input("Enter your password: ")

            if user == self.username and password == self.password:
                self.logged = True
                print("Logged in Successfully")
            else:
                print("Invalid Credentials")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def add_friend(self, user):
        if self.logged:
            if user == self:
                print("You cannot add yourself")
            elif user not in self.friends_list:
                self.friends_list.append(user)
                self.friends += 1

                user.friends_list.append(self)
                user.friends += 1

                print(f"{user.name} added as friend")
            else:
                print("User is already your friend")
        else:
            print("Not logged in")

    def remove_friend(self, user):
        if self.logged:
            if user in self.friends_list:
                self.friends_list.remove(user)
                self.friends -= 1

                if self in user.friends_list:
                    user.friends_list.remove(self)
                    user.friends -= 1

                print(f"{user.name} removed from friends")
            else:
                print("User not found")
        else:
            print("Not logged in")

    def profile(self):
        if self.logged:
            print(f"\n{self.name}'s Profile")
            print(f"Name      : {self.name}")
            print(f"Username  : {self.username}")
            print(f"Age       : {self.age}")
            print(f"Gender    : {self.gender}")
            print(f"Friends   : {self.friends}")
            print(f"Following : {self.following}")
        else:
            print("Not logged in")

    def friends_profile(self):
        if self.logged:
            if len(self.friends_list) == 0:
                print("No friends")
                return

            for i, j in enumerate(self.friends_list):
                print(f"{i} : {j.name}")

            l = int(input("Enter your choice: "))

            if 0 <= l < len(self.friends_list):
                self.friends_list[l].profile()
            else:
                print("Invalid choice")
        else:
            print("Not logged in")


# Main Program

f1 = Facebook.signup()
f2 = Facebook.signup()
f3 = Facebook.signup()
f4 = Facebook.signup()

f1.login()
f2.login()

f1.add_friend(f2)
f1.add_friend(f3)
f1.add_friend(f4)

f1.profile()

f1.friends_profile()

f2.remove_friend(f1)

f3.add_friend(f2)

f3.friends_profile()

f1.logout()