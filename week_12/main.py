def check_computers():
    computers = []

    # Check 5 computers
    for number in range(1, 6):
        status = input(f"Computer {number} Status (A/U/M): ")

        computers.append(status.upper())

    return computers


def count_available(computers):
    available = 0  # initial value

    for status in computers:
        if status == "A":
            available += 1

    return available


def display_status(computers, available):
    print("\n========== LAB STATUS ==========")

    for number in range(5):
        print(
            f"Computer {number + 1}: {computers[number]}"
        )

    print("-------------------------------")
    print(f"Available Computers: {available}")
    print("===============================")


# Main programgit 
while True:

    computers = check_computers()

    available = count_available(computers)

    display_status(computers, available)

    again = input("\nPerform another monitoring cycle? (Y/N): ")

    if again.upper() != "Y":
        break

print("Monitoring ended.")