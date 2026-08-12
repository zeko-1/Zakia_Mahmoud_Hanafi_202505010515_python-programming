def print_report(name, employee_id, gross, epf_amount, socso_amount, net):

    print("\n========== SALARY REPORT ==========")

    print(f"Employee Name : {name}")
    print(f"Employee ID   : {employee_id}")

    print("-----------------------------------")

    print(f"Gross Salary  : RM {gross:.2f}")
    print(f"EPF (11%)     : RM {epf_amount:.2f}")
    print(f"SOCSO (0.5%)  : RM {socso_amount:.2f}")

    print("-----------------------------------")

    print(f"Net Salary    : RM {net:.2f}")

    print("===================================")