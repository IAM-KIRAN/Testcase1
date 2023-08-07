import re
pattern = r"[A-Z]atch"
text = """PS hon p1.py
<re.Match object; span=(0, 14), match='192.168.25.255'>
<re.Catch object; span=(38, 52), match='555.555.555.55'>
<re.Batch object; span=(54, 69), match='195.168.258.165'>
"""
match = re.search(pattern,text)

print(match)