def mystery(l,v):
  if len(l) == 0:
    return (v)
  else:
    return (mystery(l[:-1],l[-1]+v))

def mystery2(l):
     if l == []:
        return (l)
     else:
        return (l[-1:] + mystery2(l[:-1]))
def mystery3(l):
    if l == []:
        return(l)
    else:
        return(mystery3(l[1:])+l[:1])

if __name__ == "__main__":
  print(mystery([22,14,19,65,82,55],1))
  print(mystery2([31,32,71,18,51]))
  print(mystery3([22,34,18,57,92,45]))