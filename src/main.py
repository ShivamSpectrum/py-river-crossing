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

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Left bank
    pygame.draw.rect(screen, (34, 139, 34), (0, 0, 300, 500))
    # River
    pygame.draw.rect(screen, (30, 144, 255), (300, 0, 300, 500))
    # Right bank
    pygame.draw.rect(screen, (34, 139, 34), (600, 0, 300, 500))

    # Text
    left_text = font.render("Left Bank", True, (255, 255, 255))
    right_text = font.render("Right Bank", True, (255, 255, 255))
    screen.blit(left_text, (80, 20))
    screen.blit(right_text, (680, 20))

    # Counts
    screen.blit(font.render(f"M: {left['M']}  C: {left['C']}", True, (255,255,255)), (60, 60))
    screen.blit(font.render(f"M: {right['M']}  C: {right['C']}", True, (255,255,255)), (660, 60))

    # People
    draw_people(left["M"], 60, 130, (255,255,255))   # missionaries
    draw_people(left["C"], 60, 180, (200,0,0))       # cannibals
    draw_people(right["M"], 660, 130, (255,255,255))
    draw_people(right["C"], 660, 180, (200,0,0))

    pygame.display.flip()

pygame.quit()

