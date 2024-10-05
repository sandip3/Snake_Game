import pygame
import random

pygame.init()

# Color

Sky_blue = "#F5F5F5"
Dark_blue = "#01204E"
Red = "#FF6600"
green = "#73EC8B"
Purpel = "#604CC3"


class Game:
    def __init__(self):

        # Display Resolution
        self.width = 1080
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Define FPS
        self.clock = pygame.time.Clock()
        self.Score = 0
        self.Game_over = False

        # Snack_block = Snak body
        # Value is Condination(x,y)
        self.Snake_block = [(500, 300), (490, 300), (480, 300)]
        self.block = 10

        self.food_position = self.Create_Food()
        self.Direction = "Right"

    def Run(self):
        while not self.Game_over:
            for event in pygame.event.get():
                # Click 'X' to CLose
                if event.type == pygame.QUIT:
                    self.Game_over = True
                    self.Display_Game_over()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.Direction != "Down":
                        self.Direction = "Up"
                    elif event.key == pygame.K_DOWN and self.Direction != "Up":
                        self.Direction = "Down"
                    elif event.key == pygame.K_LEFT and self.Direction != "Right":
                        self.Direction = "Left"
                    elif event.key == pygame.K_RIGHT and self.Direction != "Left":
                        self.Direction = "Right"

            # Snake's Head Movement not (Moving)
            self.Snake_moment()

            # Background
            self.screen.fill(Sky_blue)

            # if Game_over_Check is True then chage value of game over to true and exit
            if self.Game_over_Check():
                self.Display_Game_over()
                continue

            # chack If head touch food if not remove sanke's lenght -1 to keep it's lenght going forward
            if self.new_head == self.food_position:
                self.Snake_block.append(self.Snake_block[-1])
                self.food_position = self.Create_Food()
                self.Score += 1
            else:
                self.Snake_block.pop()
            # Move Snake Forword
            self.Snake_block.insert(0, self.new_head)

            # Display Snake Body
            for block in self.Snake_block:
                pygame.draw.rect(
                    self.screen,
                    green,
                    pygame.Rect(block[0], block[1], self.block, self.block),
                )
            pygame.draw.rect(
                self.screen,
                Red,
                pygame.Rect(
                    self.food_position[0], self.food_position[1], self.block, self.block
                ),
            )

            self.Display_Score(self.Score)
            pygame.display.update()
            self.clock.tick(15)

    def Create_Food(self):
        # x , y Coordinates of the food
        x = (random.randint(0, (self.width - self.block) // self.block)) * self.block
        y = (random.randint(0, (self.height - self.block) // self.block)) * self.block
        return (x, y)

    # Move Snake's Head
    def Snake_moment(self):
        if self.Direction == "Up":
            self.new_head = (
                self.Snake_block[0][0],
                self.Snake_block[0][1] - self.block,
            )
        elif self.Direction == "Down":
            self.new_head = (
                self.Snake_block[0][0],
                self.Snake_block[0][1] + self.block,
            )
        elif self.Direction == "Left":
            self.new_head = (
                self.Snake_block[0][0] - self.block,
                self.Snake_block[0][1],
            )
        elif self.Direction == "Right":
            self.new_head = (
                self.Snake_block[0][0] + self.block,
                self.Snake_block[0][1],
            )

    def Game_over_Check(self):
        # chack if snack head is in it self
        if self.new_head in self.Snake_block[1:]:
            return True

        # chack if snack touch border
        if (
            self.new_head[0] < 0
            or self.new_head[0] >= self.width
            or self.new_head[1] < 0
            or self.new_head[1] >= self.height
        ):
            return True

        return False

    # Display Score
    def Display_Score(self, score):
        # Seting font of System
        font = pygame.font.SysFont(None, 40)
        txt = font.render(f"Score : {score}", True, Dark_blue)
        # Position of score
        self.screen.blit(txt, (10, 10))

    def Display_Game_over(self):
        font = pygame.font.SysFont(None, 100)
        txt = font.render(f"Game Over!", True, Purpel)
        self.screen.blit(txt, (340, 300))
        pygame.display.update()
        pygame.time.delay(2000)

        self.Game_over = True


game = Game()
game.Run()
pygame.quit()
