#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

# Комбинируемые диакритические знаки
BREVE   = "\u0306"   # breve — й, ъ, э
DIAER   = "\u0308"   # diaeresis — ё, ь, ю, я
CARON   = "\u030c"   # caron — ж, ч, ш
CEDILLA = "\u0327"   # cedilla — щ

LOW = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
    "ё": "o" + DIAER, "ж": "z" + CARON, "з": "z", "и": "i",
    "й": "i" + BREVE, "к": "k", "л": "l", "м": "m", "н": "n",
    "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "h", "ц": "c", "ч": "c" + CARON, "ш": "s" + CARON,
    "щ": "s" + CEDILLA, "ъ": "y" + BREVE, "ы": "y", "ь": "y" + DIAER,
    "э": "e" + BREVE, "ю": "u" + DIAER, "я": "a" + DIAER,
}
UP = {k.upper(): v.upper() for k, v in LOW.items()}

def translit(text):
    return "".join(UP.get(ch) or LOW.get(ch) or ch for ch in text)

class TranslitApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Transliteraciä")
        self.set_default_size(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.apply_css()

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,
                      spacing=10, border_width=10)
        self.add(box)

        # Заголовок — системный шрифт интерфейса, жирный
        title = Gtk.Label(label="Transliteraciä", xalign=0)
        title.get_style_context().add_class("title")
        box.pack_start(title, False, False, 0)

        # Верхнее поле — моноширинный, обычный вес
        self.top_sw, self.top_view = self.make_field(editable=True)
        box.pack_start(self.top_sw, True, True, 0)

        # Кнопка — системный UI-шрифт, без моноширины, без жирного
        btn = Gtk.Button(label="Transliterirovatÿ")
        btn.get_style_context().add_class("btn-ui")
        btn.connect("clicked", self.on_translit)
        box.pack_start(btn, False, False, 0)

        # Нижнее поле — моноширинный, обычный вес, только для чтения
        self.bottom_sw, self.bottom_view = self.make_field(editable=False)
        box.pack_start(self.bottom_sw, True, True, 0)

    def make_field(self, editable=True):
        view = Gtk.TextView(wrap_mode=Gtk.WrapMode.WORD_CHAR)
        view.set_editable(editable)
        view.get_style_context().add_class("mono")
        sw = Gtk.ScrolledWindow()
        sw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        sw.set_shadow_type(Gtk.ShadowType.IN)
        sw.add(view)
        return sw, view

    def on_translit(self, widget):
        buf = self.top_view.get_buffer()
        text = buf.get_text(buf.get_start_iter(), buf.get_end_iter(), False)
        self.bottom_view.get_buffer().set_text(translit(text))

    def apply_css(self):
        provider = Gtk.CssProvider()
        css = """
            /* Заголовок: системный шрифт, жирный */
            .title {
                font-weight: bold;
                font-size: 20px;
            }

            /* Текстовые поля: моноширинный, обычный вес */
            .mono {
                font-family: monospace;
            }

            /* Кнопка: системный UI-шрифт, без моноширины, без жирного */
            .btn-ui {
                font-weight: normal;
                padding: 8px 16px;
            }
        """
        provider.load_from_data(css.encode("utf-8"))
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

win = TranslitApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

