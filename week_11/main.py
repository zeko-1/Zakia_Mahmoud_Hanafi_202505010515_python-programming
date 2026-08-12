import student
import access
import display


def main():

    name, student_id, registered, lab_open, computer_available = student.get_student()

    status = access.check_access(
        registered,
        lab_open,
        computer_available
    )

    reason = access.get_reason(
        registered,
        lab_open,
        computer_available
    )

    display.print_result(
        name,
        student_id,
        status,
        reason
    )


if __name__ == "__main__":
    main()