def to_fahrenheit(t_celsius):
  return t_celsius * 1.8 + 32

t_celsius = float(input("enter temperature in celsius: "))
print(f"fahrenheit temperature for {t_celsius} celcisus is {to_fahrenheit(t_celsius)}")
