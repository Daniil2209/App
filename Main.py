import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

# Цвет фона приложения
Window.clearcolor = (0.05, 0.06, 0.09, 1)

QUOTES = {
    "🔥 Мотивация": [
        "Начни сейчас. Потом может не быть.",
        "Дисциплина делает то, что мотивация не может.",
        "Каждый день — новый шанс.",
        "Ты сильнее, чем думаешь.",
        "Мечты требуют действий."
    ],
    "🧠 Философия": [
        "Мы видим мир не таким, какой он есть, а такими, какие мы есть.",
        "Тишина — тоже ответ.",
        "Смысл жизни — в самой жизни.",
        "Истина проста, но не всегда удобна."
    ],
    "💪 Успех": [
        "Работай тихо. Пусть результат говорит.",
        "Успех — это привычка.",
        "Маленькие шаги каждый день.",
        "Не сравнивай начало с чужим финишем."
    ],
    "😌 Жизнь": [
        "Жизнь — не гонка.",
        "Иногда нужно просто остановиться.",
        "Цени простые моменты.",
        "Не всё должно быть идеально."
    ],
    "😂 Мемы": [
        "Я не ленивый, я в режиме энергосбережения.",
        "Планы были, но настроение отменило.",
        "Мотивация ушла, не попрощавшись.",
        "С понедельника — это состояние души."
    ],
    "❤️ Любовь": [
        "Любовь — это забота.",
        "Счастье — быть понятым.",
        "Любовь начинается с уважения."
    ],
    "🧘 Спокойствие": [
        "Не всё требует твоей реакции.",
        "Спокойствие — твоя сила.",
        "Отпусти то, что не можешь контролировать."
    ]
}

class QuoteCard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 30
        self.size_hint_y = None
        self.height = 380

        with self.canvas.before:
            Color(0.12, 0.14, 0.2, 1)
            self.bg = RoundedRectangle(radius=[30])

        self.bind(pos=self.update_bg, size=self.update_bg)

        self.quote_label = Label(
            text="Нажми кнопку или свайпни вверх",
            font_size=24,
            halign="center",
            valign="middle",
            color=(1, 1, 1, 1)
        )
        self.quote_label.bind(size=self.quote_label.setter("text_size"))
        self.add_widget(self.quote_label)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size

    def set_quote(self, text):
        self.quote_label.text = f"«{text}»"

class QuoteBombBig(App):

    def build(self):
        self.category = list(QUOTES.keys())[0]

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        title = Label(
            text="💣 Quote Bomb RU",
            font_size=36,
            size_hint_y=None,
            height=70,
            bold=True
        )
        root.add_widget(title)

        self.spinner = Spinner(
            text=self.category,
            values=list(QUOTES.keys()),
            size_hint_y=None,
            height=55
        )
        self.spinner.bind(text=self.change_category)
        root.add_widget(self.spinner)

        scroll = ScrollView()
        self.card = QuoteCard()
        scroll.add_widget(self.card)
        root.add_widget(scroll)

        btn = Button(
            text="💥 Новая цитата",
            size_hint_y=None,
            height=65,
            background_color=(0.6, 0.3, 1, 1)
        )
        btn.bind(on_press=self.new_quote)
        root.add_widget(btn)

        Window.bind(on_touch_up=self.on_swipe)

        self.new_quote()
        return root

    def change_category(self, spinner, text):
        self.category = text
        self.new_quote()

    def new_quote(self, *args):
        quote = random.choice(QUOTES[self.category])
        self.card.set_quote(quote)

    def on_swipe(self, window, touch):
        if touch.dy > 50:
            self.new_quote()

if __name__ == "__main__":
    QuoteBombBig().run()
