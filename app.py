import os
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def list_files(startpath, outputfile):
  output = open(outputfile, "w", encoding="utf-8")
  size = 0
  for root, dirs, files in os.walk(startpath):
      level = root.replace(startpath, '').count(os.sep)
      # print(level)
      # if level == 0:
      #   continue
      output.write('\n')
      indent = ' ' * 4 * (level)

      if level == 1:
        output.write('{}{}{}'.format(indent, 'SIZE (prev) >>> ', convert_size(size)))
        output.write('\n')
        size = 0
      
      output.write('{}{}/'.format(indent, os.path.basename(root)))
      subindent = ' ' * 4 * (level + 1)
      
      for f in files:
        fp = os.path.join(root, f)
        size += os.path.getsize(fp)
      
  print('>>>> END')

list_files('D:\Photos', r'C:\Users\donika.peneva\Desktop\otestPY\outputtest.txt')