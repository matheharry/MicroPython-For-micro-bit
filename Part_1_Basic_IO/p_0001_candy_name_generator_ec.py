from microbit import display, Image
from speech import say

SPEED = 95

candy_title = input('Wie lautet der Name der Süßigkeit? ')
candy_flavor = input('Welchen Geschmack hat die Süßigkeit? ')

display.show(Image.SURPRISED)
print('Wir wollen sie {0} {1} nennen!'.format(candy_title, candy_flavor))
say('Wir wollen sie {0} {1} nennen!'.format(candy_title, candy_flavor))
display.show(Image.HAPPY)
