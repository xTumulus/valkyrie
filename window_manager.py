import sys

import gi
try:
    gi.require_version("Gtk", "4.0")
    from gi.repository import GLib, Gtk
except ImportError or ValueError as exc:
    print('Error: Dependencies not met.', exc)
    sys.exit(1)

from device import Device

class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, app, appTitle):
        print('init window')
        # print(self.list_properties())
        super().__init__(application=app, title=appTitle)

        # configure window
        self.set_default_size(900, 600)
        self.set_resizable(True)

        # create header bar
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)

        # create main vertical box
        self.mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.mainBox)

        # menu bar
        self.menuBar = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, 
            halign=Gtk.Align.FILL
            )
        self.menuBar.set_margin_end(10)
        self.menuBar.set_margin_top(10)
        self.mainBox.append(self.menuBar)

        # tab bar
        self.tabBar = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            hexpand=True
            )
        self.menuBar.append(self.tabBar)

        # menu buttons
        self.menuButtons = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            halign=Gtk.Align.END,
            hexpand=True
            )
        self.menuBar.append(self.menuButtons)

        self.menuButtons.list_properties()

        # add button TODO make the button a class?
        self.scanButton = Gtk.Button(label='Scan Devices')
        self.scanButton.connect('clicked', self.on_click_scan)
        self.menuButtons.append(self.scanButton)

        # content window
        self.contentBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.mainBox.append(self.contentBox)
        
        print('created window')

    def on_click_scan(self, clicked_button):
        devices = self.getv4lDevices()
        # idea is to create a tab in the header for each device
        for device in devices:
            button = Gtk.Button(label = device.name)
            button.connect('clicked', self.on_click_device, device.name)
            self.tabBar.append(button)
        # self.props.show_menubar = True

    # TODO move this to a v4l interface class
    def getv4lDevices(self):
        print('getting v4l devices')
        return [Device('Webcam 1', []), Device('Webcam 2', []), Device('Webcam 3', [])]

    def on_click_device(self, clicked_button, deviceName):
        print('clicked device: ' + deviceName)
        self.contentBox