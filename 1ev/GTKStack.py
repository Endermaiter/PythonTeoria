import gi
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Applicacion(Gtk.Window):
    def __init__(self):

        super().__init__(title="Exeplo de uso de Gtk.Stack()")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        stack = Gtk.Stack()

        combobox = Gtk.ComboBoxText()
        combobox.append_text("Pulsame!!!")
        combobox.append_text("Etiqueta")
        combobox.connect("changed", self.on_combo_changed,stack)

        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        botonCheck = Gtk.CheckButton(label="Pulsame!!")
        stack.add_titled(botonCheck, "Boton", "Pulsame!!")

        etiqueta = Gtk.Label(label="Una bonita etiquieta")
        stack.add_titled(etiqueta, "Etiqueta", "Una bonita etiqueta")

        conmutador = Gtk.StackSwitcher()
        conmutador.set_stack(stack)

        caixaV.pack_start(combobox, True, True, 2)
        caixaV.pack_start(conmutador, True, True, 2)
        caixaV.pack_start(stack, True, True, 0)

        self.add(caixaV)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_combo_changed(self, referenciaCombo, stack):
        text = referenciaCombo.get_active_text()

        if text == "Pulsame!!!":
            stack.set_visible_child_name("Boton")
        else:
            stack.set_visible_child_name("Etiqueta")


if __name__ == "__main__":
    Applicacion()
    Gtk.main()
