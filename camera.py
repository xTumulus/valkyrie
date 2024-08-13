from linuxpy.video.device import Device

class Camera:

    name = ''
    controls = []
    device = ''

    # instance attribute
    def __init__(self, name, controls, device):
        self.name = name
        self.controls = controls
        self.device = device

    def setControl(control, value):
        self.controls[control].value = value
        #make a call to the v4lInterface to set it there
