import gi  # Importando bibliotecas do GTK/GI
import os  # Importando bibliotecas do Linux/UNIX

LEDon = 'headsetcontrol -l 1'  # Variável do tipo string
LEDoff = 'headsetcontrol -l 0'  # Variável do tipo string
ChBattery = 'headsetcontrol -b'  # Variável do tipo string
outputB = os.popen(ChBattery)  # Lendo output do comando
readTerminalB = outputB.readlines()  # Lendo linha por linha do comando

for line in readTerminalB:  # Formatando a string readTerminalB
    line = line.strip('\r\n')

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class BatteryDialogBox(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="HeadSetControl Battery", transient_for=parent, flags=0)
        self.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        self.set_default_size(150, 100)

        label = Gtk.Label(label=readTerminalB)

        box = self.get_content_area()
        box.add(label)
        self.show_all()

class HeadSetGUI(Gtk.Window):
    def __init__(self):
        super().__init__(title="Button Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Check Battery")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)


    def on_click_me_clicked(self, widget):
        dialog = BatteryDialogBox(self)
        response = dialog.run



win = HeadSetGUI()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()