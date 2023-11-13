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
        =========
        ''',
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

        main_layout = BoxLayout(orientation='vertical', spacing=10)

        # BoxLayout for word-related components
        word_layout = BoxLayout(orientation='vertical', spacing=10)

        self.word_label = Label(text=' '.join(self.display), font_size=48)
        self.input_box = TextInput(hint_text="Guess a letter", font_size=48, multiline=False)
        self.input_box.bind(on_text_validate=self.check_guess)

        word_layout.add_widget(self.word_label)
        word_layout.add_widget(self.input_box)

        # BoxLayout for info_label
        info_layout = BoxLayout(orientation='vertical', spacing=10)
        self.info_label = Label(text='', font_size=30)
        info_layout.add_widget(self.info_label)

        # Add the word_layout and info_layout to the main_layout
        main_layout.add_widget(word_layout)
        main_layout.add_widget(info_layout)

        return main_layout

    def check_guess(self, instance):
        guess = instance.text.lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            self.info_label.text = "Please enter a single letter."
            instance.text = ""
            return

        if guess in self.display:
            self.info_label.text = f"\nYou have already guessed '{guess}' letter."
        elif guess in self.chosen_word:
            for position in range(self.word_length):
                letter = self.chosen_word[position]
                if letter == guess:
                    self.display[position] = letter
            self.info_label.text = ""
        else:
            self.lives -= 1
            self.info_label.text = f"\nYou guessed '{guess}', which is not in the word.\nYou have got {self.lives} lives left."
            self.current_stage += 1

        if self.lives == 0:
            self.info_label.text = "You have lost!"
            self.input_box.disabled = True
        elif "_" not in self.display:
            self.info_label.text = "You have won!"
            self.input_box.disabled = True
        elif self.current_stage < len(self.stages):
            self.info_label.text += self.stages[self.current_stage]

        self.word_label.text = ' '.join(self.display)
        instance.text = ""

word_list = [
    'sad',
    'happy',
    'upset'
]

if __name__ == '__main__':
    WordGuessingApp().run()
