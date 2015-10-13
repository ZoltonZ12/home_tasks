from  datetime import datetime


name_user = input('Введите ваше имя    ')
time_now = datetime.now()
maket = ' Приветствую вас, {}. Вы вошли в {} часов {} минут '

time_now_hour = time_now.hour
time_now_minute = time_now.minute
print (maket.format(name_user,time_now_hour, time_now_minute))
print( ' Приветствую вас, %s. Вы вошли в  %s часов %s минут  ' % (name_user,time_now_hour, time_now_minute))
