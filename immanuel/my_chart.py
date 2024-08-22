

from immanuel import charts


native = charts.Subject(
        date_time='2000-01-01 10:00',
        latitude='32n43',
        longitude='117w09',
    )

# or, alternatively...

from datetime import datetime

native = charts.Subject(
        date_time=datetime(2000, 1, 1, 10, 0, 0),
        latitude=32.71667,
        longitude=-117.15,
    )

# Myself

native_mfmaduar = charts.Subject(
    date_time=datetime(1966, 10, 4, 23, 45, 0),
    latitude=-23.566,
    longitude=-46.649,
    )

# and then...

for i in range(4): print()

print('M. F. Máduar')
# natal_mfmaduar = charts.Natal(native_mfmaduar)
# for object in natal_mfmaduar.objects.values():
#     print(object)

from immanuel.const import chart
from immanuel.setup import settings

settings.objects.append(chart.CERES)
# natal_mfmaduar = charts.Natal(native_mfmaduar)

# for object in natal_mfmaduar.objects.values():
#     print(object)

print('===================================')
print('Transits:')
print('===================================')
transits = charts.Transits('23s33', '46w38')
for object in transits.objects.values():
    print(object)

import json

from immanuel.classes.serialize import ToJSON
from immanuel import charts

# print(json.dumps(natal_mfmaduar.objects, cls=ToJSON, indent=4))
print(json.dumps(transits.objects, cls=ToJSON, indent=4))