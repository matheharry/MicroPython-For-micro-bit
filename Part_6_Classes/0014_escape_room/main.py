from time import sleep
import music
from microbit import display, Image, button_a, button_b, pin_logo, pin2
from Speech import Speech
from EscapeRoomCave import EscapeRoomCave
from EscapeRoomPlayer import EscapeRoomPlayer
from EscapeRoomUi import EscapeRoomUi
from EscapeRoomSoundEffects import EscapeRoomSoundEffects
from Question import Question
from FileManager import FileManager
from RandomNumberGenerator import RandomNumberGenerator

speech = Speech()
cave = EscapeRoomCave(5, 5)
player = EscapeRoomPlayer()
ui = EscapeRoomUi()
question = Question()
sound_effects = EscapeRoomSoundEffects()
file_manager = FileManager()
random_number_generator = RandomNumberGenerator()

if __name__ == '__main__':
    optional_height, optional_width = cave.optional_spaces_available()
    led_height, led_width = cave.grid_size()
    player_location = player.location()
    display.clear()
    grid = ui.update_display(led_height, led_width, player_location)
    display.show(Image(grid))
    display.set_pixel(player_location[0], player_location[1], 9)
    intro_text_welcome, intro_speaking_instructions = ui.intro()
    speech.speak(intro_text_welcome)
    speech.speak(intro_speaking_instructions)

    question_1 = False
    final_question = False

    while True:
        if button_a.is_pressed():
            # If badge player is against the left wall do NOT allow them to go through it
            if player_location[0] != 1 and player_location[0] <= optional_width:
                player.move_west()
                player_location = player.location()
                display.clear()
                grid = ui.update_display(led_height, led_width, player_location)
                display.show(Image(grid))
                display.set_pixel(player_location[0], player_location[1], 9)
            sleep(0.25)
        if button_b.is_pressed():
            if player_location[0] < optional_width:
                player.move_east()
                player_location = player.location()
                display.clear()
                grid = ui.update_display(led_height, led_width, player_location)
                display.show(Image(grid))
                display.set_pixel(player_location[0], player_location[1], 9)
            sleep(0.25)
        if pin_logo.is_touched():
            # If badge player is against the top wall do NOT allow them to go through it
            if player_location[1] != 1 and player_location[1] <= optional_height:
                player.move_north()
                player_location = player.location()
                display.clear()
                grid = ui.update_display(led_height, led_width, player_location)
                display.show(Image(grid))
                display.set_pixel(player_location[0], player_location[1], 9)
            sleep(0.25)
        if pin2.is_touched():
            if player_location[1] < optional_height:
                player.move_south()
                player_location = player.location()
                display.clear()
                grid = ui.update_display(led_height, led_width, player_location)
                display.show(Image(grid))
                display.set_pixel(player_location[0], player_location[1], 9)
            sleep(0.25)
        x, y = random_number_generator.generate_random_numbers()
        if player_location == (x, y) and not question_1:
            inventory = file_manager.read_inventory_file()
            player.inventory.append(inventory)
            if 'Red Key' not in player.inventory:
                random_question, \
                    answer_1, \
                    answer_2, \
                    answer_3, \
                    correct_answer_index, \
                    correct_answer \
                    = question.get_random_question()
                speech.speak(random_question)
                speech.speak('Press Ayy for {0}.'.format(answer_1))
                speech.speak('Toch the logo for {0}.'.format(answer_2))
                speech.speak('Press B for {0}.'.format(answer_3))
                while True:
                    if button_a.is_pressed():
                        response = 0
                        break
                    elif pin_logo.is_touched():
                        response = 1
                        break
                    elif button_b.is_pressed():
                        response = 2
                        break
                if response == correct_answer_index:
                    speech.speak('Correct!')
                    sound_effects.play_success_sound_effect()
                    question_1 = True
                else:
                    speech.speak('The correct answer is {0}.'.format(correct_answer))
                if question_1:
                    player.inventory.append('Red Key')
                    speech.speak('You picked up the red key!')
                    file_manager.write_inventory_file()
                    player_location = player.reset_player_location()
                    display.clear()
                    grid = ui.update_display(led_height, led_width, player_location)
                    display.show(Image(grid))
                    display.set_pixel(player_location[0], player_location[1], 9)
                if not question_1:
                    player_location = player.reset_player_location()
                    display.clear()
                    grid = ui.update_display(led_height, led_width, player_location)
                    display.show(Image(grid))
                    display.set_pixel(player_location[0], player_location[1], 9)
        x, y = random_number_generator.generate_random_numbers()
        if player_location == (x, y) and not final_question:
            inventory = file_manager.read_inventory_file()
            player.inventory.append(inventory)
            random_question, \
                answer_1, \
                answer_2, \
                answer_3, \
                correct_answer_index, \
                correct_answer \
                = question.get_random_question()
            speech.speak(random_question)
            speech.speak('Press Ayy for {0}.'.format(answer_1))
            speech.speak('Toch the logo for {0}.'.format(answer_2))
            speech.speak('Press B for {0}.'.format(answer_3))
            while True:
                if button_a.is_pressed():
                    response = 0
                    break
                elif pin_logo.is_touched():
                    response = 1
                    break
                elif button_b.is_pressed():
                    response = 2
                    break
            if response == correct_answer_index:
                speech.speak('Correct!')
                sound_effects.play_success_sound_effect()
                final_question = True
            else:
                speech.speak('The correct answer is {0}.'.format(correct_answer))
            if 'Red Key' in player.inventory and final_question:
                speech.speak('You Won!  You Escaped!')
                win_game_sound_effect = sound_effects.win_game_sound_effect()
                music.play(win_game_sound_effect)
                file_manager.clear_inventory_file()
                display.show(Image.ALL_CLOCKS, loop=True, delay=100)
            else:
                speech.speak('You do not have the red key to escape.')
                final_question = False
            if not final_question:
                player_location = player.reset_player_location()
                display.clear()
                grid = ui.update_display(led_height, led_width, player_location)
                display.show(Image(grid))
                display.set_pixel(player_location[0], player_location[1], 9)
