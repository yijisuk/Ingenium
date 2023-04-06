from art import text2art


def start_program():

    title_text = "INGENIUM"
    title_art = text2art(title_text)
    print(title_art)


def exit_program():

    print("Exiting program...\n")
    exit_text = "GOODBYE :D"
    exit_art = text2art(exit_text)
    print(exit_art)
