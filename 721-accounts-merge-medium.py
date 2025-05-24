# Problem link: https://leetcode.com/problems/accounts-merge
# Union Find shit: https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
# this problem is a bit hard to understand if you don't understand Union Find, i do have a video for it if it will help: https://www.youtube.com/watch?v=PAztir6pCTo&t=1360s


# Create Union Find class
class UF:
    def __init__(self, N): # N = number of nodes
        self.parents = list(range(N))

    def find(self, x):
        if x != self.parents[x]: # if x is not its own parent
            self.parents[x] = self.find(self.parents[x]) # path compression
        return self.parents[x]

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

# Every account is a disjoint set, join when there's overlap between emails + names
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UF(len(accounts))
        emailGroup = defaultdict(list) # idx of accounts => list of emails
        email_to_account = {}

        # The first value is always the account name, then the emails
        # So skip the first value (0-th index)
        for accIdx, account in enumerate(accounts):
            for email in account[1:]:

                if email in email_to_account:
                    # if this email exists previously,
                    # the current accIdx and the one we inserted previously need to be 
                    # unioned
                    uf.union(accIdx, email_to_account[email])
                else:
                    email_to_account[email] = accIdx

        # Once the union happens, the email has to be appended to the proper leader
        # so if email  'X' shows up in acc index 0 and 1, it should be grouped to 0, not 1
        for email, accIdx in email_to_account.items():
            leader = uf.find(accIdx)
            emailGroup[leader].append(email)

        # We have grouped emails, now they have to be sorted (stupid problem)
        ans = []
        for accIdx, emails in emailGroup.items():
            name = accounts[accIdx][0]
            ans.append([name] + sorted(emailGroup[accIdx]))

        return ans


        
