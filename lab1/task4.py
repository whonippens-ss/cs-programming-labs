seconds = int(input())

hours = seconds // 3600
remaining = seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print("%02d:%02d:%02d" % (hours, minutes, seconds))