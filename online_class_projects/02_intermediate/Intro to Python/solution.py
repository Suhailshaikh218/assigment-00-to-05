# Planetary Weight Calculator

def main():
    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt the user for the planet name
    planet = input("Enter a planet: ")
    
    # Define the gravitational constants for each planet
    gravity_constants = {
        'Mercury': 0.376,
        'Venus': 0.889,
        'Mars': 0.378,
        'Jupiter': 2.36,
        'Saturn': 1.081,
        'Uranus': 0.815,
        'Neptune': 1.14
    }
    
    # Calculate the weight on the chosen planet
    planetary_weight = earth_weight * gravity_constants[planet]
    
    # Round the result to two decimal places
    rounded_weight = round(planetary_weight, 2)
    
    # Print the result
    print(f"The equivalent weight on {planet}: {rounded_weight}")

if __name__ == "__main__":
    main()