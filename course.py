from dataclasses import dataclass

@dataclass
class Course:
    class_number: str
    course: str
    section: str
    seminar: str
    title: str
    instructor: str
    days: str
    time: str
    location: str
    seats: str