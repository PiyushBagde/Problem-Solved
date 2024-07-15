class Solution:
    def reformatDate(self, date: str) -> str:
        lst = date.split()
        year = lst[-1]
        date = lst[0][:2] if len(lst[0]) == 4 else f"0{lst[0][:1]}"
        months = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12",
        }
        month = months[lst[1]]
        return f"{year}-{month}-{date}"
        