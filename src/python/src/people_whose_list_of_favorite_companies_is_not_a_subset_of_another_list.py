# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/description/?envType=company&envId=datadog&favoriteSlug=datadog-all


class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        favs = [(set(favs), person) for person, favs in enumerate(favoriteCompanies)]
        favs.sort(key=lambda x: len(x[0]))

        res = []
        for i, (company_set, person) in enumerate(favs):
            is_subset = False
            for larger_set, _ in favs[i + 1 :]:
                if company_set.issubset(larger_set):
                    is_subset = True
                    break
            if is_subset is False:
                res.append(person)
        return sorted(res)
