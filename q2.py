income=int(input('enter your income'))
dependents=int(input('enter number of dependents'))
taxable_income=income-10000-(3000*dependents)
tax=taxable_income*0.2
print('taxable income:',taxable_income )
print('tax=',tax)
