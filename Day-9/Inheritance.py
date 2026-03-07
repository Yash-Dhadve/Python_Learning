class Camera:
    def click(self):
        print("Photo taken")

class Phone:
    def call(self):
        print("Calling...")

class SmartPhone(Camera, Phone):
    pass

sp = SmartPhone()
sp.click()
sp.call()