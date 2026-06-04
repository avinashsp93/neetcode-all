class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        # cricket score validator
        score, wickets = 0,0
        for e in events:
            if e == "W":
                wickets+=1
                if wickets == 10:
                    return [score, wickets]
            elif e == "WD" or e == "NB":
                score+=1
            else:
                score+=int(e)
        return [score, wickets]
        