class Water:
    """
    Class Water

        Current water level
        Target water level
        
    """
    def __init__(self):
        self.current_level = 0
        self.target_level = 0

    def SetTargetLevel(self, target_level):
        self.target_level = target_level

    def GetCurrentLevel(self):
        return self.current_level

    def CalculateLevelChange(self, height):
        if self.target_level >= height:
            if self.target_level <= 0:
                if self.target_level != self.current_level:
                    pass
            else:
                print("Target water level is lower than floor...")
        else:
            print("Target water level is higher than pool height...")

        

        