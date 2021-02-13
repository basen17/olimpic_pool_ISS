class Pool():
    """  
    Pool class responsible for managing pool values
    """

    def __init__(self, Q=1.0, Tp=1.0, length=1.0, width=1.0, height=1.0):
        self.Q = Q
        self.Tp = Tp

        self.length = length
        self.width = width
        self.height = height

        self.current_water_level = 0
        self.target_water_level = 0

        self.ground_size = self.length * self.width
        self.pool_size = self.length * self.width * self.height

        self.image_path = ''

        self.exit_code = 0


    def SetImagePath(self):
        self.exit_code = 0
        if self.current_water_level == 0:
            self.image_path = 'static/img/water_level_0.0.png'
        elif self.current_water_level > 0 and self.current_water_level <= 0.1:
            self.image_path = 'static/img/water_level_0.1.png'
        elif self.current_water_level > 0.1 and self.current_water_level <= 0.2:
            self.image_path = 'static/img/water_level_0.2.png'
        elif self.current_water_level > 0.2 and self.current_water_level <= 0.3:
            self.image_path = 'static/img/water_level_0.3.png'
        elif self.current_water_level > 0.3 and self.current_water_level <= 0.4:
            self.image_path = 'static/img/water_level_0.4.png'
        elif self.current_water_level > 0.4 and self.current_water_level <= 0.5:
            self.image_path = 'static/img/water_level_0.5.png'
        elif self.current_water_level > 0.5 and self.current_water_level <= 0.6:
            self.image_path = 'static/img/water_level_0.6.png'
        elif self.current_water_level > 0.6 and self.current_water_level <= 0.7:
            self.image_path = 'static/img/water_level_0.7.png'
        elif self.current_water_level > 0.7 and self.current_water_level <= 0.8:
            self.image_path = 'static/img/water_level_0.8.png'
        elif self.current_water_level > 0.8 and self.current_water_level <= 0.9:
            self.image_path = 'static/img/water_level_0.9.png'
        elif self.current_water_level > 0.9 and self.current_water_level <= 1.0:
            self.image_path = 'static/img/water_level_1.0.png'
        elif self.current_water_level > 1.0 and self.current_water_level <= 1.1:
            self.image_path = 'static/img/water_level_1.1.png'
        elif self.current_water_level > 1.1 and self.current_water_level <= 1.2:
            self.image_path = 'static/img/water_level_1.2.png'
        elif self.current_water_level > 1.2 and self.current_water_level <= 1.3:
            self.image_path = 'static/img/water_level_1.3.png'
        elif self.current_water_level > 1.3 and self.current_water_level <= 1.4:
            self.image_path = 'static/img/water_level_1.4.png'
        elif self.current_water_level > 1.4 and self.current_water_level <= 1.5:
            self.image_path = 'static/img/water_level_1.5.png'
        elif self.current_water_level > 1.5 and self.current_water_level <= 1.6:
            self.image_path = 'static/img/water_level_1.6.png'
        elif self.current_water_level > 1.6 and self.current_water_level <= 1.7:
            self.image_path = 'static/img/water_level_1.7.png'
        elif self.current_water_level > 1.7 and self.current_water_level <= 1.8:
            self.image_path = 'static/img/water_level_1.8.png'
        elif self.current_water_level > 1.8 and self.current_water_level <= 1.9:
            self.image_path = 'static/img/water_level_1.9.png'
        elif self.current_water_level > 1.9 and self.current_water_level <= 2.0:
            self.image_path = 'static/img/water_level_2.0.png'
        elif self.current_water_level > 2.0 and self.current_water_level <= 2.1:
            self.image_path = 'static/img/water_level_2.1.png'

        else:
            print ('Error: Incorrect water level! No image chosen!')
            self.exit_code = 1

    def CalculateLevelChange(self, u):
        self.exit_code = 0
        if self.target_water_level != self.current_water_level:
            if self.target_water_level > 0 and self.target_water_level < 2.1:
                if self.target_water_level > self.current_water_level:
                    self.current_water_level = 1 / self.ground_size * (-self.Q * 0.05 * self.Tp + (self.Q * u) / 100) + self.current_water_level
                else:
                    self.current_water_level = 1 / self.ground_size * ((self.Q * u) / 100 + self.Q * 0.05 * self.Tp) + self.current_water_level
            else:
                print('ERROR: Water level out of the range!', flush=True) 
                self.exit_code = 1


