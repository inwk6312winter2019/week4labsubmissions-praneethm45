import os
def word(dir):
 for name in os.listdir(dir):
  path = os.path.join(dir, name)
  if os.path.isfile(path):
   print(path)
  else:
   word(path)


word(os.getcwd())
