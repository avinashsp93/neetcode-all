class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        keyWithStrippedHyphens = s.replace('-', '').upper()
        count = 0
        reversedLicenseWithHyphens = ""
        for i in keyWithStrippedHyphens[::-1]:
            count += 1
            reversedLicenseWithHyphens += i
            if count % k == 0 and count != len(keyWithStrippedHyphens):
                reversedLicenseWithHyphens += "-"
        return reversedLicenseWithHyphens[::-1]
        

