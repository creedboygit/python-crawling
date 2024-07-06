from icecream import ic


class Character:
    def __init__(self, name, hp):
        self.unit_name = name
        self.unit_hp = hp
        print("객체를 만들 때 실행되는 함수")

    def say(self):
        print(f"나는 {self.unit_name}(이)다.")

    def info(self):
        print("-" * 10)
        print(f"이름 : {self.unit_name}")
        print(f"체력 : {self.unit_hp}")
        print("-" * 10)


ezreal = Character("이즈리얼", 90)
ic(ezreal)

ezreal.say()
ezreal.info()
ic(ezreal.unit_name)
ic(ezreal.unit_hp)

jarvan = Character("자르반", 80)
jarvan.say()
jarvan.info()


### 생성자(__init__)
## magic method : 특정 시점에 자동으로 실행되는 함수


class Monster:
    def __init__(self, name):
        self.monster_name = name
        print("객체를 만들 때 실행되는 함수")

    def say(self):
        print(f"나는 {self.monster_name}(이)다.")


shark = Monster("상어")
shark.say()
