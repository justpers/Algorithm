def make_s(s, k):
    if k <= len(s):
        print(s[k-1])
    else:
        s_trans = s
        for i in range(len(s)):
            s_trans = list(s_trans)
            if s_trans[i] == '0':
                s_trans[i] = '1'
            else:
                s_trans[i] = '0'
        
        s = s + ''.join(s_trans)
        make_s(s, k)

k = int(input())
s = "0"
make_s(s, k)