print("\n[Problem 1] Create using the exponentiation arithmetic operator")
"""
Code to calculate the thickness when the paper is folded once
"""
THICKNESS = 0.00008
folded_thickness = THICKNESS*(2**43)
print("Thickness: {} meters".format(folded_thickness))

print("\n[Problem 2] Unit Conversion")
# Convert meters to kilometers and display with two decimal places
TEN_THOUSAND_KILOMETER = 1000 * 10000
DISTANCE_TO_MOON = 384400 #in km
print("Thickness: {: .2f} ten thousand kilometers".format(folded_thickness/TEN_THOUSAND_KILOMETER))
print("Cannot reach the Moon." if folded_thickness < DISTANCE_TO_MOON*1000 else "Yes, It reached the Moon.")

print("\n[Problem 3] Create using a for statement")
folded_thickness = THICKNESS
for num_fold in range(0, 43):
    folded_thickness = folded_thickness * 2
print("Thickness: {} meters".format(folded_thickness))
