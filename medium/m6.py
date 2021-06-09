## 6. ZigZag Conversion
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        if numRows==2:
            return s[::2]+s[1::2]
        if 0<len(s):
            outs = s[::2*(numRows-1)]
        else:
            return ""
        for i in range(1,(numRows-1)):
            out1,out2 = "",""
            if i<len(s):
                out1 = s[i::2*(numRows-1)]
                if 2*(numRows-1)-i<len(s):
                    out2 = s[2*(numRows-1)-i::2*(numRows-1)]
                if len(out2)<len(out1):
                    outs+=''.join(map(''.join,zip(out1,out2)))+out1[-1]
                else:
                    outs+=''.join(map(''.join,zip(out1,out2)))
        if (numRows-1)<len(s):    
            outs += s[(numRows-1)::2*(numRows-1)]
        return outs
