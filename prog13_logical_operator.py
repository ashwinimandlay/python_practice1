# logical operators for multiple true statement
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print('eligible for loan')

else:
    print('not eligible')
# logical or, and, not

has_criminal_record = False
if has_high_income and not has_criminal_record:
    print("eligible for safe loan")
else:
    print("not eligible")

