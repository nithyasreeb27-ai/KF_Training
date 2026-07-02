class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    def celsius_checker(self):
        try:
            if self.celsius<-273.15:
                raise ValueError
        except ValueError:
            return ("ValueError raised")
t=Temperature(100)
print(t.fahrenheit())