import re


with open('Stevedores emails.txt', 'r') as f:
 with open('Stevedores emails clean.txt', 'w') as w:
      lines = f.readlines() 
      #emails = lines[lines.index("<a href=") + 1: lines.index("</a>")]
      #w.write(str(emails))
      for line in lines:
        def find_between( lines, first, last ):
                  try:
                      start = line.index( first ) + len( first )
                      end = line.index( last, start )
                      return line[start:end]
                  except ValueError:
                      return "error"   
        w.write(str(find_between( line, "mailto", "</a>" )))
        w.write(",\n")






     #emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+[a-z0-9\.\-+_]", str(lines)) 119911

     #lines = f.readlines() 
      
    # emails = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', str(lines))