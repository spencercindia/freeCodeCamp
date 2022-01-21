def add_time(start, duration, day = False):
  time = []
  time = start.partition(":")
  time2 = time[2].partition(" ")

  hour = int(time[0])
  min = int(time2[0])
  suffix = time2[2]


  weekdays = {'monday': 0, 'tuesday': 1, 'wednesday': 2,
  'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
  weekdays_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  newSuffix = ["AM", "PM"]
  dur = duration.partition(":")
  durHr = int(dur[0])
  durMin = int(dur[2])

  sumMin = min + durMin

  countHr = 0

  if sumMin >= 60:
    countHr = 1
    sumMin = sumMin - 60

  if sumMin < 10:
    sumMin = str(f"0{sumMin}")

  count12 = 0

  sumHr = hour + durHr + countHr

  numberofdays = round(sumHr/24)

  while sumHr > 12:
    sumHr = sumHr - 12
    count12 = count12 + 1
    continue

  if count12 % 2 != 0 or countHr == 1:
    if suffix == newSuffix[0]:
      suffix = newSuffix[1]
    else:
      suffix = newSuffix[0]

  new_time = f"{sumHr}:{sumMin} {suffix}"

  if numberofdays >= 1:
      if numberofdays == 1:
        new_time = f"{sumHr}:{sumMin} {suffix} (next day)"
      else:
        new_time = f"{sumHr}:{sumMin} {suffix} ({numberofdays} days later)"

  if day:
      day = day.lower()
      index = int((weekdays[day]) + numberofdays)
      while index >= 7:
        index = index - 7
        continue
      newday = weekdays_array[index]
      new_time = f"{sumHr}:{sumMin} {suffix}, {newday}"
      if numberofdays >= 1:
        if numberofdays == 1:
          new_time = f"{sumHr}:{sumMin} {suffix}, {newday} (next day)"
        else:
          new_time = f"{sumHr}:{sumMin} {suffix}, {newday} ({numberofdays} days later)"


  return new_time
