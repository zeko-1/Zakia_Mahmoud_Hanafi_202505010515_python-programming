import employee
import salary
import report


def main():

    name, employee_id, basic, allowance = employee.get_employee()

    gross = salary.gross_salary(basic, allowance)

    epf_amount = salary.epf(gross)

    socso_amount = salary.socso(gross)

    net = salary.net_salary(gross)

    report.print_report(
        name,
        employee_id,
        gross,
        epf_amount,
        socso_amount,
        net
    )


if __name__ == "__main__":
    main()