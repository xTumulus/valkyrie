import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import window_manager

class ValkyrieApp(Gtk.Application):

    title = 'Valkyrie A/V Manager'
    devices = []

    def __init__(self):
        print('init app')
        super().__init__(application_id='com.kitchDevelopment.Valkyrie')

def on_activate(app):
    print('app activated')

    window = window_manager.MainWindow(app, app.title)
    window.present()

print('run main')
app = ValkyrieApp()
app.connect('activate', on_activate)
app.run(None)      
