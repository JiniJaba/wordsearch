import pygame
import generate
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))

selected = []
image=pygame.image.load(r'bg.png')


def game_over_screen(screen, list_copy):
    game_over_format = pygame.font.Font("freesansbold.ttf", 100)

    if list_copy == []:
        screen.fill((220,224,230))

        display_word = game_over_format.render("YOU WIN", True, (137,188,254))
        screen.blit(display_word, (175, 200))


def refine_list(lst):
    for i in range(len(lst)):
        lst[i] = remove_duplicate(lst[i])
    return lst


def remove_duplicate(word):
    try:
        s = ""
        s += word[0]
        for i in range(1, len(word)):
            if word[i] != s[-1]:
                s += word[i]
        return s
    except IndexError:
        return 0


def display_board():
    x_start = 0
    y_start = 0
    for i in range(10):
        for j in range(10):
            if [x_start, y_start] in guessed_indexes:
                pygame.draw.rect(screen, (126,184,254), (x_start, y_start, 40, 40), 0)
                pygame.draw.rect(screen, (3,27,57), (x_start, y_start, 40, 40), 2)
            elif [x_start, y_start] in selected:
                pygame.draw.rect(screen, (126,184,254), (x_start, y_start, 40, 40), 0)
                pygame.draw.rect(screen, (3,27,57), (x_start, y_start, 40, 40), 2)

            else:
                pygame.draw.rect(screen, (216,213,213), (x_start, y_start, 40, 40), 0)
                pygame.draw.rect(screen, (87,159,10), (x_start, y_start, (40), (40)), 2)
            x_start += 40
        x_start = 0
        y_start += 40


def print_search():
    y = 21
    search_format = pygame.font.Font("freesansbold.ttf", 23)
    for line in generate.grid:
        x = 23
        for i in range(10):
            search_render = search_format.render(line[i].upper(), True, (0,0,0))
            width = search_render.get_width()
            height = search_render.get_height()
            screen.blit(search_render, (x - width // 2, y - height // 2))
            x += 40
        y += 40


def display_words():
    x = 535
    y = 150
    word_format = pygame.font.Font("freesansbold.ttf", 25)
    title_words_format = pygame.font.Font("freesansbold.ttf", 35)

    title_words = title_words_format.render("WORDS", True, "brown")
    screen.blit(title_words, (500, 100))
    for word in generate.words_copy:
        display_word = word_format.render(word, True, (0, 0, 0))
        screen.blit(display_word, (x, y))
        y += 33


drag = False
guessed = []
word = ""
running = True
guessed_indexes = []
words_to_guess = refine_list(generate.words_copy[::])
while (running):

    screen.blit(image,(0,0))

    display_board()
    display_words()
    print_search()
    game_over_screen(screen, words_to_guess)

    for event in pygame.event.get():
        if (event.type != pygame.MOUSEBUTTONUP):
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                drag = True

                x, y = pygame.mouse.get_pos()
                if x <= 600:
                    word += generate.grid[(y // 40 % 600)][(x // 40 % 600)]
            if event.type == pygame.MOUSEMOTION and drag:
                x, y = pygame.mouse.get_pos()
                if x <= 600:
                    word += generate.grid[(y // 40 % 600)][(x // 40 % 600)]

                    guessed_indexes.append([x // 40 * 40, y // 40 * 40])
        else:
            drag = False
            if remove_duplicate(word) in words_to_guess:
                selected += (guessed_indexes)
                if (remove_duplicate(word) == "duck"):
                    mixer.music.load("duck.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "crow"):
                    mixer.music.load("crow.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "dove"):
                    mixer.music.load("dove.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "eagle"):
                    mixer.music.load("eagle.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "hen"):
                    mixer.music.load("hen.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "ostrich"):
                    mixer.music.load("ostrich.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "owl"):
                    mixer.music.load("owl.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "peacock"):
                    mixer.music.load("peacock.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "quail"):
                    mixer.music.load("quail.mp3")
                    mixer.music.play()
                if (remove_duplicate(word) == "swallow"):
                    mixer.music.load("swallow.mp3")
                    mixer.music.play()

                index = words_to_guess.index(remove_duplicate(word))
                words_to_guess.remove(remove_duplicate(word))
                generate.words_copy.pop(index)

            word = ""
            guessed_indexes = []
        pygame.display.update()