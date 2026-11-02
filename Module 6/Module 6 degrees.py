# Israel Navarro
# November 1, 2026
# Problem 5: Convert user-entered radians to degrees manually and with math.degrees.
import math

radians = float(input("Enter an angle in radians: "))
manual_degrees = radians * 180 / math.pi
module_degrees = math.degrees(radians)

print("Calculated degrees:", manual_degrees)
print("math.degrees result:", module_degrees)
