from settings import *


class Board:
    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self, show=False):
        for col in range(COLS):
            if (
                self.squares[0][col]
                == self.squares[1][col]
                == self.squares[2][col]
                != 0
            ):
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        for row in range(ROWS):
            if (
                self.squares[row][0]
                == self.squares[row][1]
                == self.squares[row][2]
                != 0
            ):
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        return 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = [
            (row, col)
            for row in range(ROWS)
            for col in range(COLS)
            if self.empty_sqr(row, col)
        ]
        return empty_sqrs

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0


class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player
        self.logger_levelinfo()

    def logger_levelinfo(self):
        logging.info(
            "AI is in UNBEATABLE mode!!, press '0' for RANDOM mode"
            if self.level
            else "AI is in RANDOM mode!!, press '1' for UNBEATABLE mode"
        )

    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))

        return empty_sqrs[idx]

    def minimax(self, board, maximizing):
        case = board.final_state()

        if case == 1:
            return 1, None

        if case == 2:
            return -1, None

        elif board.isfull():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for row, col in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for row, col in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            eval = "random"
            move = self.rnd(main_board)
        else:
            eval, move = self.minimax(main_board, False)

        logging.info(
            f"AI has chosen to mark the square in pos {move} "
            + ( f"with an eval of: {eval}"
            if DEBUG
            else "" )
        )

        return move


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.gamemode = "ai"
        self.running = True
        self.show_lines()
        self.logger_gamemode()

    def logger_gamemode(self):
        logg_gmode = (
            ["SINGLE PLAYER", "MULTI PLAYER"]
            if self.gamemode == "ai"
            else ["MULTI PLAYER", "SINGLE PLAYER"]
        )
        logging.info(
            f"Game is in {logg_gmode[0]} mode, press 'g' to switch to {logg_gmode[1]} mode"
        )

    def show_lines(self):
        screen.fill(BG_COLOR)

        pygame.draw.line(screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (WIDTH - SQSIZE, 0),
            (WIDTH - SQSIZE, HEIGHT),
            LINE_WIDTH,
        )

        pygame.draw.line(screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, HEIGHT - SQSIZE),
            (WIDTH, HEIGHT - SQSIZE),
            LINE_WIDTH,
        )

    def draw_fig(self, row, col):
        if self.player == 1:
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)

    def make_move(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_fig(row, col)

        if self.gamemode == "ai":
            if self.player == 1:
                logging.info(
                    f"You have chosen to mark the square in pos ({row}, {col})"
                )
        else:
            logging.info(
                ("Player 1" if self.player == 1 else "Player 2")
                + f" have chosen to mark the square in pos ({row}, {col})"
            )
        self.next_turn()

    def next_turn(self):
        self.player = self.player % 2 + 1

    def change_gamemode(self):
        self.gamemode = "ai" if self.gamemode == "pvp" else "pvp"
        self.logger_gamemode()

    def isover(self):
        if self.board.final_state(show=True) != 0:
            unique, counts = np.unique(self.board.squares, return_counts=True)
            counter = dict(zip(unique, counts))
            if 2 in counter:
                if self.gamemode == "ai":
                    logging.info(
                        ("You Won!!" if counter[1] > counter[2] else "AI Won!!")
                        + ", press 'r' to Reset"
                    )
                else:
                    logging.info(
                        (
                            "Player 1 Won!!"
                            if counter[1] > counter[2]
                            else "Player 2 Won!!"
                        )
                        + ", press 'r' to Reset"
                    )
        else:
            if self.board.isfull():
                logging.info("Match DRAW!!, press 'r' to Reset")

        return self.board.final_state(show=True) != 0 or self.board.isfull()

    def reset(self):
        self.__init__()
        logging.info("Game Resetted, Make a move!!")


def main():
    logging.debug(f"Starting the Game")

    game = Game()
    board = game.board
    ai = game.ai

    logging.info("Game Started Make a Move!!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    game.change_gamemode()

                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                if event.key == pygame.K_0:
                    logging.info(
                        "AI is in RANDOM mode!!, press '1' for UNBEATABLE mode"
                    )
                    ai.level = 0

                if event.key == pygame.K_1:
                    logging.info(
                        "AI is in UNBEATABLE mode!!, press '0' for RANDOM mode"
                    )
                    ai.level = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_sqr(row, col) and game.running:
                    game.make_move(row, col)

                    if game.isover():
                        game.running = False

        if game.gamemode == "ai" and game.player == ai.player and game.running:
            pygame.display.update()

            row, col = ai.eval(board)
            game.make_move(row, col)

            if game.isover():
                game.running = False

        pygame.display.update()


main()
