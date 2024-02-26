class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp = "[.]".join(address.split("."))
        return temp
        