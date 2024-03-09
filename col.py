def display_menu(menu_options):
    max_option_length = max(len(option) for option in menu_options)
    box_width = max_option_length + 6
    box_horizontal_line = "+" + "-" * (box_width - 2) + "+"

    print(box_horizontal_line)
    for option in menu_options:
        print("| {:<{width}} |".format(option, width=max_option_length))
    print(box_horizontal_line)

def main():
    menu_options = [
        "1. Option 1",
        "2. Option 2",
        "3. Option 3",
        "4. Option 4",
        "5. Option 5",
        "6. Option 6",
        "7. Option 7",
        "8. Option 8",
        "9. Option 9",
        "10. Option 10"
    ]

    display_menu(menu_options)

if __name__ == "__main__":
    main()
