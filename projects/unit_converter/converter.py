def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def km_to_miles(km):
    return km * 0.621371

def main():
    print("--- ⚖️ Simple Converter ---")
    c = 25
    print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")
    
    km = 10
    print(f"{km}km is {km_to_miles(km):.2f} miles")

if __name__ == "__main__":
    main()
