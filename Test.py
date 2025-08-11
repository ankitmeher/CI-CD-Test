import datetime

def get_current_datetime():
    """Returns the current date and time."""
    return datetime.datetime.now()

if __name__ == "__main__":
    current_datetime = get_current_datetime()
    print(f"Current date and time: {current_datetime}")