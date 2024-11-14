salary = int(input("Enter your salary: "))
if salary >= 30000:
    Years_On_Job = float(input("Enter your years of job: "))
    if Years_On_Job >= 2:
        print('You Quality for the loan congrats!!!')
    else :
        print('unfortunately you have been at your job for less than 2 years')
else :
        print('You should be earning at least 30000')