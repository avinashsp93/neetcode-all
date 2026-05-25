from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()        
        for email in emails:
            validEmail = ""
            local,domain = "",""
            i = 0
            # keep going , ignore once if . , keep ignoring if + , hardstop at @

            # keep going until @ or +
            while(email[i] != "@" and email[i] != "+"):
                if(email[i] == "."):
                    i+=1
                    continue
                local += email[i]
                i+=1
            
            # ignore everything after + until @
            while(email[i] != "@"):
                i+=1

            domain = email[i:]
            validEmail += local + domain
            unique.add(validEmail)
        return len(unique)
    
    def numUniqueEmails_easy(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local,domain = email.split("@")
            
            # grab only before +
            local = local.split("+")[0]
            
            # remove all periods .
            local = local.replace(".", "")

            #reconstruct
            unique.add(f"{local}@{domain}")

        return len(unique)