Tax_Limit = 35300
Tax_Credit = 3300
USC_Band_A = 12012
USC_Band_B = 8472

while True:
    Gross_Wage = float(input("Input Gross Monthly Wage: "))
    if Gross_Wage < Tax_Limit/12:
      Gross_Tax = Gross_Wage * 0.20
    else:
      Higher_Rate = Gross_Wage - Tax_Limit / 12
      Lower_Rate = Gross_Wage - Higher_Rate
      Higher_Tax = Higher_Rate * 0.40
      Lower_Tax = Lower_Rate * 0.20
      Gross_Tax = Higher_Tax + Lower_Tax
    Income_Tax = round(Gross_Tax - Tax_Credit / 12, 2)
    PRSI = round(Gross_Wage * 0.04, 2)
    if Gross_Wage <= USC_Band_A/12:
      USC = Gross_Wage * 0.005
    elif Gross_Wage <= USC_Band_B + USC_Band_A:
      USC_A = USC_Band_A/12 * 0.005
      USC_Taxable = Gross_Wage - USC_Band_A/12
      USC_B = USC_Taxable * 0.02
      USC = USC_A + USC_B
    else:
      USC_A = USC_Band_A/12 * 0.005
      USC_B = USC_Band_B/12 * 0.02
      USC_Taxable = Gross_Wage - USC_Band_A/12 - USC_Band_B/12
      USC_C = USC_Taxable * 0.045
      USC = USC_A + USC_B + USC_C
    USC = round(USC, 2)
    print("Gross Wage:",Gross_Wage)
    print("Income Tax:",Income_Tax)
    print("PRSI:",PRSI)
    print("USC:",USC)
    print("Net Wage:",Gross_Wage-Income_Tax-PRSI-USC)
    print("------------------------------------------")