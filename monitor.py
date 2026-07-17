print("DEBUG VERSION 2")
from notifier import notify
from berkeley import fetch_courses
from state import load_state, save_state


def seats_available(status):
    """
    Returns True if the status indicates there are open seats.
    """

    status = status.lower().strip()

    # Definitely no seats
    if "no open seats" in status:
        return False

    # Look for a number followed by "open seat"
    import re
    match = re.search(r"(\d+)\s+open seat", status)

    if match:
        return int(match.group(1)) > 0

    # Handle statuses like "Open"
    if "open" in status:
        return True

    return False 

courses = fetch_courses()

old_state = load_state()
new_state = {}

for c in courses:

    key = c.class_number

    new_state[key] = {
        "course": c.course,
        "section": c.section,
        "seats": c.seats,
    }

    if key in old_state:

        old_seats = old_state[key]["seats"]
        new_seats = c.seats

        if old_seats != new_seats:

            # Notify only when seats become available
            if not seats_available(old_seats) and seats_available(new_seats):

                
                print("Calling notify...", flush=True)
                print(repr(" Berkeley Seat Open!"), flush=True)
                notify(
                    " Berkeley Seat Open!",
                    f"{c.course} Section {c.section}\n\nStatus: {new_seats}"
                )

                print(f" Seat opened for {c.course} Section {c.section}")

            else:
                print(
                    f"Seat status changed ({old_seats} → {new_seats}), "
                    "but no seats opened."
                )

save_state(new_state)

print("Finished checking.")