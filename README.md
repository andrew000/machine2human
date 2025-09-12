[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# machine2human

```python
from m2h import Hum2Sec, Sec2Hum

>> print(Sec2Hum(80000, lang="en").string)
'22 hours 13 minutes 20 seconds'


>> print(Hum2Sec("22 hours 13 minutes 20 seconds").seconds)
80000
