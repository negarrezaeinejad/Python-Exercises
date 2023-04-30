# function definition
def validate_zip_code(zip_code):    
    if len(zip_code) == 5 and zip_code.isdigit() == True:
        print("%s is a valid Zip Code!" %(zip_code))
    else:
        print("%s is not a valid Zip Code!" %(zip_code))

    

# function call
zip_code = input("Please Enter Your Zip Code: ")
validate_zip_code(zip_code)555