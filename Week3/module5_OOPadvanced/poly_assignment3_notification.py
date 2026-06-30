class Email:
    def __init__(self,recepient,message):
        self.recepient=recepient
        self.message=message
    def send(self):
        print(f"Received an email from {self.recepient} saying {self.message}")
class SMS:
    def __init__(self,number,message):
        self.number=number
        self.message=message
    def send(self):
        print(f"Received an SMS from {self.number} saying {self.message}")
class Whatsapp:
    def __init__(self,number,message):
        self.number=number
        self.message=message
    def send(self):
        print(f"Received a whatsapp message {self.number} saying {self.message}")
email=Email("nithya","Thank you")
sms=SMS(982387467,"hi")
whatsapp=Whatsapp(7617645312,"Hello")
notifications=[email,sms,whatsapp]
for notification in notifications:
    notification.send()