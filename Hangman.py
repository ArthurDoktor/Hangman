import random

words = ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes',
         'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar',
         'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness',
         'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves',
         'embezzle', 'equip', 'espionage', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping',
         'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize',
         'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku',
         'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker',
         'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jujitsu', 'jockey', 'jogging', 'joking', 'jovial',
         'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch',
         'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix',
         'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph',
         'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka',
         'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum',
         'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz',
         'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome',
         'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'twelfth', 'twelfths', 'unknown', 'unworthy',
         'unzip', 'uptown', 'vaporize', 'vixen', 'voodoo', 'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy',
         'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy',
         'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag',
         'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

while True:
    tries = []
    word = random.choice(words)
    display = ['-' for i in range(len(word))]
    n = 0
    start = input('H A N G M A N\nType "play" to play the game, "exit" to quit: ')
    if start == 'exit':
        break
    if start != 'play':
        continue
    while n < 8:
        print('\n' + ''.join(display))
        char = input('Input a letter: ')
        if len(char) != 1:
            print('You should print a single letter ')
            continue
        if char not in chars:
            print('It is not an ASCII lowercase letter ')
            continue
        if char in tries:
            print('You already typed this letter ')
            continue
        tries.append(char)
        count = 0
        letter_in_word = False
        for i in word:
            if char == word[count]:
                letter_in_word = True
                display[count] = word[count]
            count += 1
        if not letter_in_word:
            n += 1
            print('No such letter in the word')
        if word == ''.join(display):
            print('You guessed the word {}!\nYou survived!\n'.format(''.join(display)))
            break
    else:
        print('You ran out of tries!\nYou are hanged!\nThe word to guess was {}\n'.format(word))
