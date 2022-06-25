"""后缀表达式求值"""
import operator

d = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

# se = '4 5 6 * +'
# se = '7 8 + 3 2 + /'
se = '9 3 1 - 3 * + 10 2 / +'
se = se.split(' ')
stack = []
for i in se:
    if i.isdigit():
        stack.append(int(i))
    if i in d:
        a, b = stack.pop(), stack.pop()
        stack.append(d[i](b,a))
print(stack)

