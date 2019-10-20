class Duck:
    sound = 'Quackkksss!!'
    walking = 'Walking like a duck'
    def quack(self):
        print(self.sound)
        print(type(self.sound))

    def walk(self):
        print(self.walking)
        print(type(self.quack()))


def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()