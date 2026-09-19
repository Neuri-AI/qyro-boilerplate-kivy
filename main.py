from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from qyro_engine import ApplicationContext
from qyro_engine.ui.component import Component


class KivyExampleApp(App, Component, ApplicationContext):

    def component_will_mount(self):
        Window.size = (640, 480)
        Window.minimum_width = 640
        Window.minimum_height = 480

    def render(self):
        label = Label(
            text=(
                f"Hello, World!\n\n"
                f"App Title: {self.window_title}\n"
                f"Active Icon: {self.app_icon}\n"
                f"Platform: {self.platform.value} (Frozen: {self.is_frozen})\n\n"
                f"Build Settings:\n{self.app}\n"
            ),
            halign="left",
            valign="middle",
        )
        label.bind(size=label.setter("text_size"))
        return label

    def build(self):
        return self.render()


if __name__ == "__main__":
    KivyExampleApp().exec()