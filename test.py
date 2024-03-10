from recup_match_temps_reel import get_matchs_stats


from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from recup_match_temps_reel import recup_match_data
from recup_match_temps_reel import get_matchs_stats


class MatchApp(MDApp):
    def build(self):
        self.screen = Screen(name="Classement")
        txt=""
        for elem in get_matchs_stats()[0][0]:
            for k,v in elem.items():
                txt+=f"{k}: {v}\n"
        self.labelj1 = MDLabel(text=txt)


        self.screen.add_widget(self.labelj1)
        return self.screen




if __name__ == '__main__':
    MatchApp().run()
