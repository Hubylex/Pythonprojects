import time

class RiceCooker:
    def _init_(self):
        self.cooking_time = 0
    
    def set_cooking_time(self, minutes):
        self.cooking_time = minutes
    
    def cook_rice(self):
        if self.cooking_time == 0:
            print("Please set the cooking time first.")
        else:
            print(f"Cooking rice for {self.cooking_time} minutes...")
            time.sleep(self.cooking_time * 60)
            print("Rice is cooked!")
    
    def keep_warm(self, minutes):
        print(f"Keeping rice warm for {minutes} minutes...")
        time.sleep(minutes * 60)
        print("Rice is still warm!")
    
    def cook_and_keep_warm(self):
        self.cook_rice()
        self.keep_warm(60)  


cooker = RiceCooker()
cooker.set_cooking_time(20) 
cooker.cook_and_keep_warm()