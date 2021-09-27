class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valids = set()
        for email in emails:
            localname, domainname = email.split('@')
            if not localname or not domainname:
                continue
            localname = localname.replace('.', '')
            localname = localname.split('+')[0]
            valids.add(localname + '@' + domainname)
        return len(valids)