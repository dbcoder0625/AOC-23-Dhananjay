try:
  nu=0
  while True:
    s=input()
    start="";end="" 
    for i in range(len(s)):
      if s[i].isnumeric():
        start=s[i] 
        break 
    for i in range(len(s)-1,-1,-1):
      if s[i].isnumeric():
        end=s[i] 
        break 
    nu+=int(start+end) 
except:
  print(nu)
