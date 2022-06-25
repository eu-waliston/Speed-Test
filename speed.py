import speedtest
from time import sleep

option=int(input('''
What do you want to know:
1) Download speed
2) Upload speed
3) Both Download and Upload
4) Ping
Your choice: '''))

if option<1 or option>4:
  sleep(1)
  print()
  print('please enter values from 1-4 only')
else:
  sleep(1)
  print()
  print('Pls wait, test in progress...')
  print()
  down_speed=round(speed.download()/1000000,3)
  up_speed=round(speed.upload()/1000000,3)
  print('One more sec please...')
  sleep(2.5)
  print()
  if option == 1:
    print('Your Download speed is: ',down_speed,'Mbps')
  elif option == 2:
    print('Your Upload speed is: ', up_speed, 'Mbps')
  elif option == 3:
    print('Your Download speed is: ', down_speed, 'Mbps', end=" ")
    print(', and your Upload speed is: ', up_speed, 'Mbps')
  elif option == 4:
    s=[]
    speed.get_servers(s)
    print(speed.results.ping,'ms')
  else:
    print('Something went wrong, pls try again...')