from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from recup_classement import *

class MainApp(MDApp):
    def build(self):
        screen= Screen(name="Classement")

        table = MDDataTable(
            pos_hint={'center_x':0.5, 'center_y':0.47},
            size_hint=(0.9, 0.9),
            use_pagination=True,
            pagination_menu_pos="top",
            rows_num=8,
            column_data = [
                ("Classement", dp(30)),
                ("Joueur", dp(40)),
                ("Nationalité", dp(40)),
                ("Points",dp(25))
            ],
            row_data = get_joueurs_classement("ATP")

        )
        table.bind(on_row_press=self.on_row_press)
        self.theme_cls.theme_style="Light"
        self.theme_cls.primary_palette = "Green"

        screen.add_widget(table)

        return screen

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''
        print("PAGE JOUEUR", instance_row.text)


if __name__ == "__main__":
    MainApp().run()