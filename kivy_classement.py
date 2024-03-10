from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp
from recup_classement import *

class MainApp(MDApp):
    league = StringProperty()

    def __init__(self, league, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.league = league

    def build(self):
        self.screen = Screen(name="Classement")
        self.create_table()

        self.bouton_atp = MDFlatButton(text="ATP", on_press=self.btn_press, pos_hint={'center_x': 0.07, 'center_y': 0.96})
        self.bouton_wta = MDFlatButton(text="WTA", on_press=self.btn_press, pos_hint={'center_x': 0.93, 'center_y': 0.96})

        self.searchbar = MDTextField(
            id = "searchbar",
            hint_text="Cherchez un joueur parmis cette liste",
            pos_hint={'center_x': 0.5, 'center_y':0.96},
            size_hint_x=.7,
            on_text_validate=self.clear_table
        )

        self.screen.add_widget(self.bouton_atp)
        self.screen.add_widget(self.bouton_wta)
        self.screen.add_widget(self.searchbar)

        return self.screen

    def create_table(self):
        if hasattr(self, 'table'):
            self.screen.remove_widget(self.table)

        self.table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.47},
            size_hint=(0.9, 0.9),
            use_pagination=True,
            pagination_menu_pos="top",
            rows_num=8,
            column_data=[
                ("Classement", dp(30)),
                ("Joueur", dp(40)),
                ("Nationalité", dp(40)),
                ("Points", dp(25))
            ],
            row_data=get_joueurs_classement(self.league)
        )
        self.table.bind(on_row_press=self.on_row_press)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"

        self.screen.add_widget(self.table)

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''
        print("PAGE JOUEUR", instance_row.text)

    def clear_table(self, instance):
        corres = self.get_nom(instance.text)
        print(corres)
        if corres != None:
            if hasattr(self, 'table'):
                self.screen.remove_widget(self.table)
            self.table = MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.47},
                size_hint=(0.9, 0.9),
                use_pagination=True,
                pagination_menu_pos="top",
                rows_num=8,
                column_data=[
                    ("Classement", dp(30)),
                    ("Joueur", dp(40)),
                    ("Nationalité", dp(40)),
                    ("Points", dp(25))
                ],
                row_data=corres
            )
            self.table.bind(on_row_press=self.on_row_press)
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Green"

            self.screen.add_widget(self.table)



    def btn_press(self, instance):
        self.league = instance.text
        self.create_table()

    def get_nom(self,nom_recherche):
        rep=[]
        for elem in self.table.row_data:
            if nom_recherche.lower() in elem[1].lower():
                rep.append(elem)
        if len(rep)>0:
            return rep
        else:
            return None

if __name__ == "__main__":
    MainApp(league="ATP").run()
