'''Bar code calculator'''
keep_asking = True
while keep_asking == True:
    barcode = input("Enter a 13-digit barcode: > ")
    if len(barcode) != 13 or not barcode.isdigit():
        print("Invalid barcode. Please enter a 13-digit number.")
    else:
        country_code = barcode[0:2]
        manufacturer_code = barcode[2:7]
        product_code = barcode[7:12]
        check_digit = barcode[12]
        print(f"Country of origin: {country_code}")
        print(f"Manufacturer code: {manufacturer_code}")
        print(f"Product code: {product_code}")
        print(f"Check digit: {check_digit}")
        keep_asking = False