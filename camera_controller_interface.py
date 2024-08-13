from linuxpy.video.device import Device
from camera import Camera

class CameraControllerInterface:

    def __init__(self):
        self = self

    def getCameras():

        cameras = []
        devices = []

        #call the v4l2 command to get devices        
        #TODO find a way to only get actual devices and stop at that point
        devices.append(Device.from_id(0))
        # devices.append(Device.from_id(1))
        # devices.append(Device.from_id(2))
        # devices.append(Device.from_id(3))
        # devices.append(Device.from_id(4))

        # print(devices)
        # print(dir(devices[0]))
        # print(devices[0].info.card)
        # print(devices[0].io)
        # print(devices[0].controls)
        # print(devices[0]._abc_impl)

        for device in devices:
            device.open()
                
            camera = Camera(device.info.card, device.controls, device)
            cameras.append(camera)

            device.close()

        return cameras

        