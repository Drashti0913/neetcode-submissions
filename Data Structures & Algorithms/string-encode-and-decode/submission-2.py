class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return chr(258)

        delimiter = chr(257)
        encode = delimiter.join(strs)
        return encode

    def decode(self, s: str) -> List[str]:
        if s == chr(258):
            return []
        delimiter = chr(257)
        decode = s.split(delimiter)
        return decode

