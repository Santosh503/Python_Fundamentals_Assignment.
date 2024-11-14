class temprature:
  def __init__(self,temp:float,unit:str) -> None:
    self.temp=temp
    self.unit=unit

  def celcius_to_ferhenheit(self):
        print((self.temp*9/5)+32)

  def ferhenheit_to_celcius(self):
        print((self.temp-32)*5/9)

  def choose(self):
    if self.unit.lower()=="c":
      self.celcius_to_ferhenheit()

    elif self.unit.lower()=="f":
      self.ferhenheit_to_celcius()

    else:
      print("Invalid unit ")

tem=float(input("Enter the temperature "))
unit1=input("Enter unit ")
t=temprature(tem,unit1)
t.choose()


