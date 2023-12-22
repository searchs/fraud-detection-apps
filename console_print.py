"""Print details e.g. customer record, to the console in formatted view"""


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = (
        f"| Name: {passenger} |"
        f" Flight: {flight_number} |"
        f" Seat: {seat} |"
        f" Aircraft: {aircraft}"
        " |"
    )
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"

    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()


# Check output
console_card_printer("Ola Traveller", "A6", "NG1029", "Airbus A319")
