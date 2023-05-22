import pygame

class Puzzle:
    def __init__(self):
        self.pgn = None
        self.solution = None
        self.side_to_move = None

class Game:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.display = pygame.display.set_mode((self.width, self.height))

        # LOAD IMAGES
        self.box_size = 60
        self.images = {
            'b': pygame.transform.smoothscale((pygame.image.load('pieces/b.png')), (self.box_size, self.box_size)),
            'k': pygame.transform.smoothscale((pygame.image.load('pieces/k.png')), (self.box_size, self.box_size)),
            'n': pygame.transform.smoothscale((pygame.image.load('pieces/n.png')), (self.box_size, self.box_size)),
            'p': pygame.transform.smoothscale((pygame.image.load('pieces/p.png')), (self.box_size, self.box_size)),
            'q': pygame.transform.smoothscale((pygame.image.load('pieces/q.png')), (self.box_size, self.box_size)),
            'r': pygame.transform.smoothscale((pygame.image.load('pieces/r.png')), (self.box_size, self.box_size)),
            'wB': pygame.transform.smoothscale((pygame.image.load('pieces/wB.png')), (self.box_size, self.box_size)),
            'wK': pygame.transform.smoothscale((pygame.image.load('pieces/wK.png')), (self.box_size, self.box_size)),
            'wN': pygame.transform.smoothscale((pygame.image.load('pieces/wN.png')), (self.box_size, self.box_size)),
            'wP': pygame.transform.smoothscale((pygame.image.load('pieces/wP.png')), (self.box_size, self.box_size)),
            'wQ': pygame.transform.smoothscale((pygame.image.load('pieces/wQ.png')), (self.box_size, self.box_size)),
            'wR': pygame.transform.smoothscale((pygame.image.load('pieces/wR.png')), (self.box_size, self.box_size))
        }

        # LOAD PUZZLES
        self.puzzles = []
        with open('puzzles.txt', 'r') as f:
            temp_puzzle = Puzzle()
            for i, line in enumerate(f):
                if i % 3 == 0:
                    temp_puzzle.pgn = line
                elif i % 3 == 1:
                    temp_puzzle.solution = line.split(' ')[1:-1]
                else:
                    temp_puzzle.side_to_move = line
                    self.puzzles.append(temp_puzzle)
                

        self.game_over = False
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.puzzle = self.puzzles[0]
        self.puzzle_step = 0

        self.incorrect = None
        self.correct = None

        while not self.game_over:
            # MAIN LOOP
            self.draw()
            self.update()
            self.clock.tick(self.fps)

    def draw(self):
        # DRAW BOARD
        for x in range(8):
            for y in range(8):
                color = (240, 217, 181) if (x+y)%2 == 0 else (181, 136, 99)
                pygame.draw.rect(self.display, color, pygame.Rect(x*self.box_size, y*self.box_size, self.box_size, self.box_size))
        # DRAW PIECES
        idx = 0
        for char in self.puzzle.pgn[:-11]:
            if char == '/':
                continue
            elif char.isnumeric():
                idx += int(char)
            else:
                self.display.blit(self.images[(char if char.islower() else ('w' + char))], ((idx % 8)*self.box_size, (idx // 8)*self.box_size))
                idx += 1
                
        if self.incorrect:
            pass
        if self.correct:
            pass
        pygame.display.flip()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.game_over = True
            if pygame.mouse.get_pressed()[0]:
                self.selected = pygame.mouse.get_pos()
                self.selected = (self.selected[0] // self.box_size, self.selected[1] // self.box_size)

                print(self.selected)
                

if __name__ == '__main__':
    g = Game(1000,600)