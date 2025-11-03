from datetime import datetime


# 1 Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute, second)
print("timestamp", timestamp)

# 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
date_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(date_now)
# 3 Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# 4 Calculate the time difference between now and new year.

t1 = datetime.now()
t2 = datetime(year=2026, month=1, day=1, hour=0, minute=0, second=0)
diff = t2 - t1
print("Time left for new year:", diff)

# 5 Calculate the time difference between 1 January 1970 and now.
t1 = datetime.now()
t2 = datetime(year=1970, month=1, day=1, hour=0, minute=0, second=0)
diff = t1 - t2
print("Time diff for 01/1970:", diff)

# 6 Think, what can you use the datetime module for? Examples:
# - Para trabalhar com datas e horários em Python.
# - Para análises de séries temporais (ex: evolução de dados ao longo do tempo).
# - Para registrar o momento exato de uma ação (timestamp) em um sistema.
# - Para definir a data e hora de postagens (ex: em um blog ou aplicativo).
# - Em geral, para qualquer situação que envolva manipulação de tempo.
