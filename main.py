t = input()
t=t.lower()

punct = [',', ';', ':', '.', '-', '?', '!']

for i in punct:
    t=t.replace(i, '')

ts = t.split()
print('Всего слов:', len(ts))
tset = set(ts)
ts1 = list(tset)
tmax=''
print(len(ts1))
tmin=ts1[0]

for i in ts1:
    if len(i)>len(tmax):
        tmax=i
    if len(i)<len(tmin):
        tmin=i

tw = {}
for i in t:
    if i in tw:
        tw[i] += 1
    else:
        tw[i] = 1

tc={}
for i in ts:
    if i not in tc:
        tc[i] = 1
    else:
        tc[i] += 1
tsimb={}
for i in t:
    if i not in tsimb:
        tsimb[i] = 1
    else:
        tsimb[i] += 1

print("Количество разных слов:", len(tset))
print("Самое длинное слово:", tmax)
print("Самое короткое слово:", tmin)
print("Частота слов:")
for word, frequency in tc.items():
    print(f"{word}: {frequency}")

print('Всего букв:', len(t))
print("Частота букв:")
for word, frequency in tw.items():
    print(f"{word}: {frequency}")
