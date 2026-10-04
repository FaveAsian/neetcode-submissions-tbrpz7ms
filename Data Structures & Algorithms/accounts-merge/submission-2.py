class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = list(range(len(accounts)))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j 
        # Build out mapping
        # name will be
        email_to_acc = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i

        email_to_index = defaultdict(set)
        for i, account in enumerate(accounts):
            root = find(i)
            email_to_index[root].update(account[1:])

        merged_list = []
        for root, emails in email_to_index.items():
            merged_list.append([accounts[root][0]] + sorted(emails))
        
        return merged_list