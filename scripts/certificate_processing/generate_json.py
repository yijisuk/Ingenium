from datetime import datetime, date


def generate_json():

    print("<<Generate certificate>>")

    title = input("Enter the program title: ")
    organizer = input("Enter the name of the organizer: ")

    while True:
        start_date = input(
            "Enter the start date of the program (YYYY-MM-DD): ")

        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            if start_date_obj.date() > date.today():
                raise ValueError(
                    "Start date cannot be later than current date.")

            start_date = start_date_obj.strftime("%Y-%m-%d")

            break
        except ValueError as e:
            print(
                "Start date format is invalid or earlier than start date. Please enter again.")
            print(e)

    while True:
        end_date = input("Enter the end date of the program (YYYY-MM-DD): ")

        try:
            end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
            if end_date_obj < start_date_obj:
                raise ValueError("End date cannot be earlier than start date.")

            end_date = end_date_obj.strftime("%Y-%m-%d")

            break
        except ValueError as e:
            print(
                "End date format is invalid or earlier than start date. Please enter again.")
            print(e)

    name = input("Enter the name of the person in subject: ")
    role = input("Enter the role of the person in subject: ")

    description = input("Enter the description for this certificate: ")

    certificate = {
        "title": title,
        "organizer": organizer,
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "role": role,
        "description": description,
        "issued_on": datetime.now().strftime("%Y-%m-%d")
    }

    return certificate
