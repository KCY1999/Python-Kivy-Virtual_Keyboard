import kivy

kivy.require('2.0.0')

from kivy.app import App

#import lib
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MyApp(App):
    def build(self):

        #creat layout to add label and keyboard
        layout = GridLayout(cols=1)

        # create layout to add label and keyboard
        keyboard = VKeyboard(on_key_up=self.key_up)
        #create label to show key
        self.label = Label(text="Select key : ", font_size="50sp")

        #add label & keyboard in layout
        layout.add_widget(self.label)
        layout.add_widget(keyboard)

        return layout

    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            keycode=keycode[1]

        self.label.text="Select key: "+str(keycode)


if __name__ == '__main__':
    MyApp().run()
