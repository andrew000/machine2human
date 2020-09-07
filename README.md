[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# machine2human

```python
from m2h import Hum2Sec, Sec2Hum

>> print(Sec2Hum(80000).string)
'22 часа 13 минут 20 секунд'


>> print(Hum2Sec("22 часа 13 минут 20 секунд").seconds)
80000
