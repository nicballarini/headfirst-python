phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# removes "nic!"
for i in range(4):
    plist.pop()
    print(plist)
# removes "D"
plist.pop(0)
print(plist)
# removes "'"
plist.remove("'")
print(plist)
# swap last 2 objects by popping both. Pop displays object being popped
# perfect for this extend
plist.extend([plist.pop(),plist.pop()])
plist.insert(2, plist.pop(3))     
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
