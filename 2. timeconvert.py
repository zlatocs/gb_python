usertime = int(input('Введите, пожалуйста, время в секундах: '))

hours = usertime // 3600
minutes = (usertime // 60) % 60
seconds = usertime%60

if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = str(seconds)

if hours < 10:
    hours = '0' + str(hours)
else:
    hours = str(hours)


print("Получается: " + hours + ":" + minutes + ":" + seconds)