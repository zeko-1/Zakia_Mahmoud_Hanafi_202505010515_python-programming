def gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def epf(gross):
    return gross * 0.11


def socso(gross):
    return gross * 0.005


def net_salary(gross):
    return gross - epf(gross) - socso(gross)