import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3 Missionaries & 3 Cannibals")

clock = pygame.time.Clock()

# game state
left = {"M": 3, "C": 3}
right = {"M": 0, "C": 0}

font = pygame.font.SysFont(None, 36)

def draw_people(count, x_start, y, color):
    x = x_start
    for _ in range(count):
        pygame.draw.circle(screen, color, (x, y), 15)
        x += 40

def update_people_on_boat_positions():
    for i, person in enumerate(people_on_boat):
        person.rect.center = (
            boat_rect.centerx - 20 + i * 40,
            boat_rect.centery
        )


class Person:
    def __init__(self, kind, x, y):
        self.kind = kind  # "M" or "C"
        self.rect = pygame.Rect(x - 15, y - 15, 30, 30)

    def draw(self, screen):
        color = (255, 255, 255) if self.kind == "M" else (200, 0, 0)
        pygame.draw.circle(screen, color, self.rect.center, 15)

people_left = []
people_right = []
people_on_boat = []

# create 3 missionaries
for i in range(3):
    people_left.append(Person("M", 60 + i * 40, 130))

# create 3 cannibals
for i in range(3):
    people_left.append(Person("C", 60 + i * 40, 180))

boat_rect = pygame.Rect(375, 300, 150, 40)
boat_side = "left"


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if boat_rect.collidepoint(mouse_pos):
                if boat_side == "left":
                    boat_rect.x = 375   # right side of river
                    boat_side = "right"
                else:
                    boat_rect.x = 375 - 225  # left side of river
                    boat_side = "left"
            
            # click on people on the left bank
            for person in people_left[:]:
                if person.rect.collidepoint(mouse_pos):
                    if boat_side == "left" and len(people_on_boat) < 2:
                        people_left.remove(person)
                        people_on_boat.append(person)

                        idx = len(people_on_boat) - 1
                        
                        break


    # Left bank
    pygame.draw.rect(screen, (34, 139, 34), (0, 0, 300, 500))
    # River
    pygame.draw.rect(screen, (30, 144, 255), (300, 0, 300, 500))

    pygame.draw.rect(screen, (139, 69, 19), boat_rect, border_radius=10)

    update_people_on_boat_positions()

    for p in people_on_boat:
        p.draw(screen)


    # Right bank
    pygame.draw.rect(screen, (34, 139, 34), (600, 0, 300, 500))

    # Text
    left_text = font.render("Left Bank", True, (255, 255, 255))
    right_text = font.render("Right Bank", True, (255, 255, 255))
    screen.blit(left_text, (80, 20))
    screen.blit(right_text, (680, 20))

    # draw people (object-based)
    for p in people_left:
        p.draw(screen)

    for p in people_right:
        p.draw(screen)


    pygame.display.flip()

pygame.quit()

