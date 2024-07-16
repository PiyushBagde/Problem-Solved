class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join([i.lower() if len(i) <= 2 else i.title() for i in title.split()])

        