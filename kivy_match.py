from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from recup_match_temps_reel import recup_match_data
from recup_match_temps_reel import get_matchs_stats
from kivy_stats import StatApp

class MatchApp(MDApp):
    def build(self):
        self.screen = Screen(name="Classement")
        self.matches = recup_match_data()
        self.current_match_index = 0

        self.current_match_label = MDLabel(
            text=self.get_match_result(self.current_match_index),
            halign="center",
            theme_text_color='Custom',
            text_color=(0, 0, 0, 1),
            size_hint_y=None,
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            height="50dp"
        )
        print(len(self.matches))
        self.match_indicator = MDLabel(text=f"{self.current_match_index+1}/{len(self.matches)}",
                                       halign="center",
                                       pos_hint={"center_x": 0.9, "center_y":0.1})


        self.screen.add_widget(self.current_match_label)
        self.screen.add_widget(self.match_indicator)

        btn_previous = MDRaisedButton(
            text="Précédent",
            on_release=self.previous_match,
            size_hint=(0.5, None),
            pos_hint={"center_x": 0.25, "center_y": 0.03},
            height="50dp"
        )
        self.screen.add_widget(btn_previous)

        btn_next = MDRaisedButton(
            text="Suivant",
            on_release=self.next_match,
            size_hint=(0.5, None),
            pos_hint={"center_x": 0.75, "center_y": 0.03},
            height="50dp"
        )

        btn_stats_j1 = MDRaisedButton(
            text="Stat joueur 1",
            on_release=self.affiche_stats_j1,
            pos_hint={"center_x": 0.2, "center_y": 0.9}
        )

        btn_stats_j2 = MDRaisedButton(
            text="Stat joueur 2",
            on_release=self.affiche_stats_j2,
            pos_hint={"center_x": 0.8, "center_y": 0.9}
        )

        btn_retour_match = MDRaisedButton(
            text="Refresh Match",
            on_release=self.update_current_match_label,
            pos_hint={"center_x": 0.5, "center_y": 0.1}
        )

        self.screen.add_widget(btn_stats_j1)
        self.screen.add_widget(btn_stats_j2)
        self.screen.add_widget(btn_retour_match)



        self.screen.add_widget(btn_next)


        return self.screen


    def get_match_result(self, match_index):
        matchs = recup_match_data()
        match = matchs[match_index]
        result_text = f"{match[1]} vs {match[2]}\nDébut du match: {match[0]}\nScore: {match[3]}\n"
        for i in range(4, len(match)-1):
            result_text += f"\nSet {i - 3}: {match[i]} \n"
        result_text += f"\nJeu en cours: {match[-1]}\n"
        return result_text


    def affiche_stats_j1(self,instance):
        self.current_match_label.text = f"Stat de {self.matches[self.current_match_index][1]}\n\n{self.match_stats_str(self.current_match_index,0)}"

    def affiche_stats_j2(self,instance):
        self.current_match_label.text = f"Stat de {self.matches[self.current_match_index][2]}\n\n{self.match_stats_str(self.current_match_index,1)}"


    def previous_match(self, instance):
        if self.current_match_index > 0:
            self.current_match_index -= 1
            #print(self.match_indicator.text[0])# = str(int(self.match_indicator.text[0]) - 1)
            self.update_current_match_label()

    def next_match(self, instance):
        if self.current_match_index < len(self.matches) - 1:
            self.current_match_index += 1
            #self.match_indicator.text[0] = str(int(self.match_indicator.text[0])+1)
            self.update_current_match_label()

    def update_current_match_label(self, instance=None):
        self.current_match_label.text = self.get_match_result(self.current_match_index)
        self.match_indicator.text=f"{self.current_match_index+1}/{len(self.matches)}"

    def match_stats_str(self, match_index, joueur):
        """
        joueur: 0 pr joueur 1, 1 pr joueur 2
        """
        txt = ""
        print(get_matchs_stats()[0])
        for elem in get_matchs_stats()[match_index][joueur]:
            for k, v in elem.items():
                txt += f"{k}: {v}\n"
        return txt


if __name__ == '__main__':
    MatchApp().run()
