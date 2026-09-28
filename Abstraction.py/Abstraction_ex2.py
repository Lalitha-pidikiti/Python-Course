from abc import ABC, abstractmethod
class SocialMedia(ABC):
    @abstractmethod
    def messenger(self):
        pass
    @abstractmethod
    def calss(self):
        pass
    @abstractmethod
    def search(self):
        pass
class whatsapp(SocialMedia):
    def messenger(self):
        print("whatsapp messenger")
    def calss(self):
        print("whatsapp voice call")
    def search(self):
        print("whatsapp search")
    def status(self):
        print("status upload")
    def channels(self):
        print("channels")
class Instagram(SocialMedia):
    def messenger(self):
        print("Insta messenger")
    def calss(self):
        print("Insta voice call")
    def search(self):
        print("Insta search")
    def status(self):
        print("reels")
    def channels(self):
        print("follwers") 
Whatsapp = whatsapp()
insta = Instagram()
Whatsapp.messenger()
insta.status()