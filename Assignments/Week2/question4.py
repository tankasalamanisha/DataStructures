startmsg = "python"
endmsg = ""
for i in range(1,1+len(startmsg)):
  endmsg = startmsg[-i] + endmsg
print(endmsg)
