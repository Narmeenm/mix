firstword="Mary"

secondword="army"

def inAngram(first,second):
   wordfirst=first.lower()
   wordsecond=second.lower()
   a = "".join(sorted(list(wordfirst)))
   b = "".join(sorted(list(wordsecond)))
   print(a)
   if (a==b):
       return True
   else:
       return False

print(inAngram(firstword,secondword))
