from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 20
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.8, 0.7

        MDLabel:
            text: "Login"
            halign: "center"
            font_style: "H4"

        MDTextField:
            id: username
            hint_text: "Username"
            icon_right: "account"
            size_hint_x: None
            width: 300
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: password
            hint_text: "Password"
            icon_right: "lock"
            password: True
            size_hint_x: None
            width: 300
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Log In"
            pos_hint: {"center_x": 0.5}
            on_release: app.login()

        MDLabel:
            id: result_label
            text: ""
            halign: "center"
            theme_text_color: "Error"  # Xato matn rangi
'''

class LoginApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def login(self):
        # Login funksiyasi
        username = self.root.ids.username.text
        password = self.root.ids.password.text
        result_label = self.root.ids.result_label

        # Simple login tekshiruvi
        if username == "user" and password == "pass":
            result_label.text = "Login successful!" 
            result_label.theme_text_color = "Primary"  # Muvaffaqiyatli xabar rangi
        else:
            result_label.text = "Invalid username or password."
            result_label.theme_text_color = "Error"  # Xato xabar rangi

LoginApp().run()
