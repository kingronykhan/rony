class Car():
    car_name = ""
    model_name = ""
    car_color = ""
    def Car_display(self):
        print(f"Car_name:{self.car_name} model_name:{self.model_name} car_color:{self.car_color}")
car1 = Car()
car1.car_name = "tata"
car1.model_name= "sda"
car1.car_color ="whit"
car1.Car_display()
