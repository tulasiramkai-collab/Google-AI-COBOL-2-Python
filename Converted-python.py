def calculate_age(birth_date: str, current_date: str) -> int:
    # Parse birth date components
    birth_year = int(birth_date[0:4])
    birth_month = int(birth_date[4:6])
    birth_day = int(birth_date[6:8])

    # Parse current date components
    current_year = int(current_date[0:4])
    current_month = int(current_date[4:6])
    current_day = int(current_date[6:8])

    # Calculate age
    age = current_year - birth_year
    if current_month < birth_month:
        age -= 1
    elif current_month == birth_month:
        if current_day < birth_day:
            age -= 1

    return age


if __name__ == "__main__":
    birth_date = input("Enter Birth Date (YYYYMMDD): ")
    current_date = input("Enter Current Date (YYYYMMDD): ")
    age = calculate_age(birth_date, current_date)
    print(f"The person's age is: {age}")