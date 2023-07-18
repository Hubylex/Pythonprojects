import time

class RiceCooker:
    def _init_(self, cooking_time):
        self.cooking_time = cooking_time
    
    def cook_rice(self):
        print("Sending signal to start cooking...")
        time.sleep(2)  # Simulating signal transmission time
        print("Rice cooker is cooking rice...")
        time.sleep(self.cooking_time)
        print("Rice is cooked!")
    
    def send_signal(self):
        print("Sending signal to rice cooker...")
        time.sleep(2)  # Simulating signal transmission time
        print("Signal sent!")
    
    def cook_with_signal(self):
        self.send_signal()
        self.cook_rice()

# Example usage
cooker = RiceCooker(20)  # Cooking time: 20 minutes
cooker.cook_with_signal()