class Solution:
    def decodeString(self, s: str) -> str:
        num_st = []
        char_st = []
        tmpnum = ''
        for i, c in enumerate(s):
            # print('num_st', num_st, 'char_st', char_st)
            if c.isnumeric():
                tmpnum += c
                if s[i+1] == '[':
                    num_st.append(int(tmpnum))
                    tmpnum = ''
            elif c == ']':
                tmp = ''
                while True:
                    poped = char_st.pop()
                    if poped == '[':
                        break
                    tmp = poped + tmp
                poped_num = num_st.pop()
                char_st.append(poped_num * tmp)
                # print('poped_num', poped_num, 'tmp', tmp, 'char_st', char_st, 'num_st', num_st)
            else:
                char_st.append(c)
        return "".join(char_st)
