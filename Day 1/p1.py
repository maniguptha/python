def is_isomorphic(s, t):
    if len(s)!= len(t) :
       return False
    char_map ={}
    for i in range(len(s)):
       if s[i] in char_map:
           if char_map[s[i]]!= t[i]:
              return False
       elif t[i] in char_map.values():
              return False
       else:
             char_map[s[i]] = t[i]

    return True
         
s = input("enter string s: ")
t = input("enter string t: ")
result=is_isomorphic(s,t)
if result:
    print("the strings are isomorphic.")
else:
    print("the strings are not isomorphic.")
