from classify_triangle import classify_triangle

def valid_input(input_str):
    try:
        value = float(input_str)
        if value > 0:
            return value
        else:
            print("Vnesite pozitivno številko. Decimalna števila ločite z piko.")
    except ValueError:
        print("Vnesite veljavno številko.")

    return None

def main():
    print("Vnesite dolžine stranic trikotnika.")
    a = b = c = None

    while a is None:
        a = valid_input(input("Stranica a: "))

    while b is None:
        b = valid_input(input("Stranica b: "))

    while c is None:
        c = valid_input(input("Stranica c: "))

    print(f"Vrsta trikotnika: {classify_triangle(a, b, c)}")

if __name__ == "__main__":
    main()
