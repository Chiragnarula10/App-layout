import kivy
from kivy.app import App
from kivy.uix.label import Label

class ChiragApp(App):

    def build(self):
        return Label(text="Hi Chirag")

if __name__=="__main__":
    ChiragApp().run()