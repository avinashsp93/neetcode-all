from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([int(passenger_detail[11:13]) for passenger_detail in details 
                    if int(passenger_detail[11:13]) > 60])
    
    # A more efficient way to count seniors without creating an intermediate list
    # Sum the boolean values directly, where True is treated as 1 and False as 0
    def countSeniors2(self, details: List[str]) -> int:
        return sum(int(passenger_detail[11:13]) > 60 for passenger_detail in details)