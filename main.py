from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class TennisTrackerUI(BoxLayout):
    def __init__(self, **kwargs):
        super(TennisTrackerUI, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.label_match_status = Label(text="En attente du début du match")
        self.label_score = Label(text="Score: 0-0")

        self.add_widget(self.label_match_status)
        self.add_widget(self.label_score)

    def update_match_info(self, match_status, score):
        self.label_match_status.text = match_status
        self.label_score.text = f"Score: {score}"

class TennisTrackerApp(App):
    def build(self):
        self.ui = TennisTrackerUI()
        return self.ui

    def on_start(self):
        match_status = "En cours"
        score = "2-1"  # Remplacez cela par les vraies données du match
        self.ui.update_match_info(match_status, score)

if __name__ == '__main__':
    TennisTrackerApp().run()
