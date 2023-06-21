from settings import *
import sys
from tetris import Tetris


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Tetris-clone")
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

    def set_timer(self):
        self.user_event = pygame.USEREVENT + 0
        self.anim_trigger = False
        pygame.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

    def update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris.draw()
        pygame.display.flip()

    def check_events(self):
        self.anim_trigger = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.tetris.control(pressed_key=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App()
    app.run()
