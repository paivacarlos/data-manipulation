class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording

    def record(self):
        if self.recording is True:
            return print(f'{self.name} is already recording!')

        print(f'{self.name} is recording!')
        self.recording = True

    def picture(self):
        if self.recording is True:
            return print(f'{self.name} it is not possible record and picture and the same time!')

        print(f'Taked picture!')

    def off_record(self):
        if self.recording is True:
            self.recording = False
            return print(f'Record is off!')

camera_canon = Camera('Canon')
camera_sony = Camera('Sony')

camera_canon.record()
camera_canon.record()
camera_canon.picture()
camera_canon.off_record()
camera_canon.picture()
print(camera_canon.recording)
print(camera_sony.recording)