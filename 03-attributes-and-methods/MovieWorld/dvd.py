import calendar


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        if self.is_rented:
            return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: not rented"

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        month_number = int(date.split(".")[1])
        creation_month = calendar.month_name[month_number]
        creation_year = int(date.split(".")[2])
        return cls(name, id, creation_year, creation_month, age_restriction)
