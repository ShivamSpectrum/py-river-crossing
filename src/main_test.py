import pygame

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3 Missionaries & 3 Cannibals")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)


class Person:
    def __init__(self, kind, x, y):
        self.kind = kind  # "M" or "C"
        self.rect = pygame.Rect(x - 15, y - 15, 30, 30)

    def draw(self, screen):
        color = (255, 255, 255) if self.kind == "M" else (200, 0, 0)
        pygame.draw.circle(screen, color, self.rect.center, 15)


def update_people_on_boat_positions():
    for i, person in enumerate(people_on_boat):
        person.rect.center = (
            boat_rect.centerx - 20 + i * 40,
            boat_rect.centery
        )


people_left = []
people_right = []
people_on_boat = []

# create people
for i in range(3):
    people_left.append(Person("M", 60 + i * 40, 130))
    people_left.append(Person("C", 60 + i * 40, 180))

# boat
BOAT_LEFT_X = 150
BOAT_RIGHT_X = 450
boat_rect = pygame.Rect(BOAT_LEFT_X, 300, 150, 40)
boat_side = "left"


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # BOAT CLICK
            if boat_rect.collidepoint(mouse_pos):

                # unload people first
                if people_on_boat:
                    if boat_side == "left":
                        for person in people_on_boat:
                            person.rect.x = 60 + len(people_left) * 40
                            person.rect.y = 130 if person.kind == "M" else 180
                            people_left.append(person)

                    else:
                        for person in people_on_boat:
                            person.rect.x = 660 + len(people_right) * 40
                            person.rect.y = 130 if person.kind == "M" else 180
                            people_right.append(person)

                    people_on_boat.clear()

                # move boat
                if boat_side == "left":
                    boat_rect.x = BOAT_RIGHT_X
                    boat_side = "right"
                else:
                    boat_rect.x = BOAT_LEFT_X
                    boat_side = "left"

            # PEOPLE CLICK (load onto boat)
            for person in people_left[:]:
                if person.rect.collidepoint(mouse_pos):
                    if boat_side == "left" and len(people_on_boat) < 2:
                        people_left.remove(person)
                        people_on_boat.append(person)
                    break

    # DRAWING
    screen.fill((0, 0, 0))

    # Left bank
    pygame.draw.rect(screen, (34, 139, 34), (0, 0, 300, 500))
    # River
    pygame.draw.rect(screen, (30, 144, 255), (300, 0, 300, 500))
    # Right bank
    pygame.draw.rect(screen, (34, 139, 34), (600, 0, 300, 500))

    # Boat
    pygame.draw.rect(screen, (139, 69, 19), boat_rect, border_radius=10)

    # Update + draw boat passengers
    update_people_on_boat_positions()
    for p in people_on_boat:
        p.draw(screen)

    # Draw people on banks
    for p in people_left:
        p.draw(screen)

    for p in people_right:
        p.draw(screen)

    pygame.display.flip()

pygame.quit()
