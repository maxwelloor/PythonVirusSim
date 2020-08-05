
class Scroller:

    def __init__(self, scroll_limit_down):
        self.offset = 100
        self.sensitivity = 30
        self.scroll_limit = scroll_limit_down - 850

    def scroll_wheel_up(self):
        self.offset += self.sensitivity

        if self.offset > 100:
            self.offset = 100

    def scroll_wheel_down(self):
        self.offset -= self.sensitivity

        if self.offset < self.scroll_limit * -1:
            self.offset = self.scroll_limit * -1

    def get_offset(self):
        return self.offset
