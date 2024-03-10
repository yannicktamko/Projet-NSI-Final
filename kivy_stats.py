from recup_match_temps_reel import get_matchs_stats

from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from recup_match_temps_reel import recup_match_data
from recup_match_temps_reel import get_matchs_stats


class StatApp(MDApp):
    index = StringProperty()
    def __init__(self, index, **kwargs):
        super(StatApp, self).__init__(**kwargs)
        self.current_match_index = index

    def build(self):
        self.screen = Screen(name="Classement")
        self.matches = recup_match_data()

        self.labelj1 = MDLabel(
            text=f"Stat de {self.matches[self.current_match_index][1]}\n\n{self.match_stats_str(self.current_match_index,0)}",
            halign="center",
            pos_hint={"center_x": 0.25, "center_y":0.5})

        self.labelj2 = MDLabel(
            text=f"Stat de {self.matches[self.current_match_index][2]}\n\n{self.match_stats_str(self.current_match_index, 1)}",
            halign="center",
            pos_hint={"center_x": 0.75, "center_y": 0.5})
        #print(self.match_stats_str(self.current_match_index,0))
        self.screen.add_widget(self.labelj1)
        self.screen.add_widget(self.labelj2)

        return self.screen

    def match_stats_str(self,match_index,joueur):
        """
        joueur: 0 pr joueur 1, 1 pr joueur 2
        """
        txt = ""
        print(get_matchs_stats()[0])
        for elem in get_matchs_stats()[match_index][joueur]:
            for k, v in elem.items():
                txt += f"{k}: {v}\n"
        return txt


