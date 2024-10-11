def swap(s, i, j):
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

def permute_string(s, begin, end):
    if begin == end - 1:
        per_lst.append(s)
    else:
        for i in range(begin, end):
            s = swap(s, begin, i)
            permute_string(s, begin + 1, end)
            s = swap(s, begin, i)

def permute(s):
    permute_string(s, 0, len(s))

t = int(input())
for _ in range(t):
    s = input()
    per_lst = []
    
    permute(s)
    result = 0
    
    for i in range(len(per_lst)):
        perm = per_lst[i]
        sum = 0
        for j in range(len(perm)):
            w = ((-1)**j) * (ord(perm[j]) - ord('a'))
            sum += w
        if sum > 0:
            result += 1
    print(result)
    
# c++코드
# #include <iostream>
# #include <vector>
# #include <string>
# #include <algorithm>
# #include <cmath>

# using namespace std;

# int result;

# void permute_string(string &s, int begin, int sum) {
#     if (begin == s.size()) {
#         if (sum > 0) {
#             result++; 
#         }
#         return;
#     }
    
#     for (int i = begin; i < s.size(); ++i) {
#         swap(s[begin], s[i]);

#         int w = ((begin % 2 == 0) ? 1 : -1) * (s[begin] - 'a');
#         permute_string(s, begin + 1, sum + w);

#         swap(s[begin], s[i]);
#     }
# }

# int main() {
#     int t;
#     cin >> t;  
#     while (t--) {
#         string s;
#         cin >> s;

#         result = 0;
    
#         permute_string(s, 0, 0);

#         cout << result << endl; 
#     }

#     return 0;
# }
