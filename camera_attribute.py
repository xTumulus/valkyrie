class DeviceAttribute:

    def __init__(self, name, attribute_type, max_value, min_value, current_value):
        self.name = name
        self.attribute_type = attribute_type
        self.max_value = max_value
        self.min_value = min_value
        self.current_value = current_value
        