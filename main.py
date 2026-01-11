# smart-decision-app
 The best app for making the right decision as quickly as possible: the digital lottery.
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
import random

class SmartDecisionApp(MDApp):
    def build(self):
        self.options = {}
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        screen = MDScreen()
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        self.option = MDTextField(hint_text="الخيار", mode="rectangle")
        self.score = MDTextField(hint_text="التقييم (1-10)", input_filter="int", mode="rectangle")

        add_btn = MDRaisedButton(text="إضافة خيار", on_release=self.add_option)
        decide_btn = MDRaisedButton(text="اتخذ القرار", on_release=self.decide)

        self.result = MDLabel(text="", halign="center")

        layout.add_widget(self.option)
        layout.add_widget(self.score)
        layout.add_widget(add_btn)
        layout.add_widget(decide_btn)
        layout.add_widget(self.result)

        screen.add_widget(layout)
        return screen

    def add_option(self, instance):
        if self.option.text and self.score.text:
            self.options[self.option.text] = int(self.score.text)
            self.result.text = f"تمت إضافة: {self.option.text}"
            self.option.text = ""
            self.score.text = ""

    def decide(self, instance):
        if len(self.options) < 2:
            self.result.text = "أدخل خيارين على الأقل"
            return
        max_score = max(self.options.values())
        best = [k for k, v in self.options.items() if v == max_score]
        self.result.text = f"✅ القرار:\n{random.choice(best)}"

SmartDecisionApp().run()
