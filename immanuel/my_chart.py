

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

# and then...

natal = charts.Natal(native)

for object in natal.objects.values():
    print(object)