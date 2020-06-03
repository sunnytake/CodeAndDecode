# coding=utf-8
'''
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''
def patternMatch(str, pattern):
    if len(str) == 0 and len(pattern) == 0:
        return True
    elif len(str) != 0 and len(pattern) == 0:
        return False
    elif len(str) == 0 and len(pattern) != 0:
        if len(pattern) > 1 and pattern[1] == '*':
            return patternMatch(str, pattern[2:])
        else:
            return False
    # s与pattern都不为空的情况
    else:
        # pattern的第二字符为*
        if len(pattern) > 1 and pattern[1] == '*':
            # s与pattern的第一个元素不同，则s不变，pattern后移两位，相当于pattern前两位当成空
            if str[0] != pattern[0] and pattern[0] != '.':
                return patternMatch(str, pattern[2:])
            else:
                # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
                # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
                # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
                # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
                return patternMatch(str[1:], pattern) or patternMatch(str, pattern[2:]) or patternMatch(str[1:], pattern[2:])
        # pattern第二个字符不为*的情况
        else:
            if str[0] != pattern[0] and pattern[0] != '.':
                return False
            else:
                return patternMatch(str[1:], pattern[1:])