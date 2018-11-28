#!/usr/bin/env python
import re

str1 = 'Aass|0.414659772907;Abat|0.332171453524;Acadl|0.453759577659;Acadm|0.417543959714;Acmsd|0.231647015473;Acsm1|0.269807059126;Acsm3|0.289172045976;'

data = re.match(r'([^|].*?)\|', str1).group(1)
print(data)



