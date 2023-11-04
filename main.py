from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
import string

class WordGuessingApp(App):
    stages = [
        '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''',
        '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         /   |
              |
        =========
        ''',
        '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        '''
    ]

    def build(self):
        self.chosen_word = random.choice(word_list)
        self.word_length = len(self.chosen_word)
        self.display = ["_"] * self.word_length
        self.lives = 6
        self.current_stage = 0

        layout = BoxLayout(orientation='vertical', spacing=10)

        self.word_label = Label(text=' '.join(self.display), font_size=24)
        self.info_label = Label(text='', font_size=20)
        self.input_box = TextInput(hint_text="Guess a letter", font_size=24, multiline=False)
        self.input_box.bind(on_text_validate=self.check_guess)

        layout.add_widget(self.word_label)
        layout.add_widget(self.info_label)
        layout.add_widget(self.input_box)

        return layout

    def check_guess(self, instance):
        guess = instance.text.lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            self.info_label.text = "Please enter a single letter."
            instance.text = ""
            return

        if guess in self.display:
            self.info_label.text = f"You have already guessed '{guess}' letter."
        elif guess in self.chosen_word:
            for position in range(self.word_length):
                letter = self.chosen_word[position]
                if letter == guess:
                    self.display[position] = letter
            self.info_label.text = ""
        else:
            self.lives -= 1
            self.info_label.text = f"You guessed '{guess}', which is not in the word. You have got {self.lives} lives left."
            self.current_stage += 1

        if self.lives == 0:
            self.info_label.text = "You have lost!"
            self.input_box.disabled = True
        elif "_" not in self.display:
            self.info_label.text = "You win!"
            self.input_box.disabled = True
        elif self.current_stage < len(self.stages):
            self.info_label.text += self.stages[self.current_stage]

        self.word_label.text = ' '.join(self.display)
        instance.text = ""

word_list = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]

if __name__ == '__main__':
    WordGuessingApp().run()
