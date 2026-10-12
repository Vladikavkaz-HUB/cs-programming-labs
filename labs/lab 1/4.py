#4
sek= int(input())
hh = sek // 3600
mini = (sek%3600)//60
s = sek % 60
print(f"{hh:02d}:{mini:02d}:{s:02d}")