class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_grp = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            ana_grp[key].append(s)
        
        return list(ana_grp.values())
        