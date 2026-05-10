from typing import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([int(passenger_detail[11:13]) for passenger_detail in details 
                    if int(passenger_detail[11:13]) > 60])