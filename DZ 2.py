import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 100
        self.progress = 100
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 25
        self.gladness -= 10
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 20
    def to_chill(self):
        print("Rest time")
        self.gladness += 25
        self.progress -= 5
    def to_walk(self):
        print("Walk")
        self.gladness += 25
    def to_skipcouple(self):
        print("Skip couple")
        self.progress -= 20
    def to_session(self):
        print("Session")
        self.progress += 25
        self.gladness -= 10
    def to_sports(self):
        print("Sports")
        self.gladness += 25
    def to_cook(self):
        print("Cooking")
        self.gladness += 20
    def to_eat(self):
        print("Eating")
        self.gladness += 30
    def to_selfdeveloment(self):
        print("Self-development")
        self.progress +=50
        self.gladness += 20
    def is_alive(self):
        if self.progress < 0:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 50:
            print("Depression…")
            self.alive = False
        elif self.progress > 1000:
            print("Passed externally…")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
nick = Student(name="Yaroslav")
for day in range(365):
 if nick.alive == False:
    break
 nick.live(day)