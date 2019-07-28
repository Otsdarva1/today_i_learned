import codecs

a='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
s = 'fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}'
ans=''
for si in s:
    if si == '{' or si == '}' or si=='_':
        ans+=si
    else:
        if si.isupper():
            ans+=a[a.find(si.lower())-3].upper()
        else:
            print(a.find(si.lower()))
            ans+=a[a.find(si)-3]

print(ans)