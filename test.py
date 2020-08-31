from validate_email import validate_email

adresse_valide = "laura.busignies@hotmail.com"
test_adress2 = validate_email(adresse_valide, check_mx = True)
# 
# print(test_adress)


print(test_adress2)