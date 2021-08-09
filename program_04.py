WIDTH = 1280
HEIGHT = 640


class Game:
    def __init__(self, background_active):
        self.background_active = background_active
        self.background_position = (0, 0)
        self.floor_level = 460
        self.hero = Actor('character-right-01.png')
        self.hero.pos = (WIDTH / 2, self.floor_level)

    def update_game(self):
        pass

    def draw_scene(self):
        screen.blit(self.background_active, self.background_position)
        self.hero.draw()


class Key:
    def __init__(self, file_name, in_pocket, room_number, place_on_floor):
        self.file_name = file_name
        self.in_pocket = in_pocket
        self.room_number = room_number
        self.place_on_floor = place_on_floor
        pass

background_active = 'corridor-01.jpg'

key_00 = Key('key-00.png', False, 11, 1025)
key_01 = Key('key-01.png', False, 17, 80)
key_02 = Key('key-02.png', False, 16, 850)
key_03 = Key('key-03.png', False, 4, 950)
key_04 = Key('key-04.png', False, 0, 370)

game = Game(background_active)

def update():
    game.update_game()

def draw():
    game.draw_scene()



