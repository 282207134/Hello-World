print('------平均法M・L完成品原価計算--------')
a = int(input('月初仕掛品の個数:'))
b = int(input('月初仕掛品の進捗度(%):'))
c = int(input('当月投入の個数:'))
d = int(input('月初直接材料費:'))
e = int(input('月初加工費:'))

print('----------------------')

f = int(input('月末仕掛品:'))
g = int(input('月末仕掛品の進捗度(%):'))
h = int(input('完成品:'))
i = int(input('直接材料費：'))
j = int(input('加工費：'))

print('----------------------')
M = int(input('完成品のうち、Mの個数：'))
L = int(input('完成品のうち、Lの個数：'))
M1 = int(input('等級係数M：'))
L1 = int(input('等級係数L：'))

print('----------------------')

print('------仕掛品（直接材料費）-------')
print('月初投入:', a, "個", d, "円")
print('当月投入:', c, "個", i, "円")
print('完成品@',(d+i)/(h+f))
print('完成品:', h, '個', (d+i)-(((d+i)/(h+f))*f), "円")
print('月末仕掛品', f, '個')

print('------仕掛品（加工費）-------')
print('月初投入', a, '個×', b, '％＝', a*b/100 )
print(e, '円')
print('当月投入:', h, '＋', f*g/100, '―', a*b/100, '＝', h+f*g/100-a*b/100)
print((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100), '円')
print('完成品@',(e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100)))
print( h, '個', h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))), "円")
print('月末仕掛品',(a*b/100)+(h+f*g/100-a*b/100)-h, '個')
print('------完成品原価-----')
print((d+i)-(((d+i)/(h+f))*f),'円+',h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))),'円=',(d+i)-(((d+i)/(h+f))*f)+h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))),'円',)
print('------積数-----')
print('M:',M,"X",M1,'=',M*M1)
print('M:',L,"X",L1,'=',L*L1)
print('------完成品原価-----')
print('M:',(d+i)-(((d+i)/(h+f))*f)+h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))),'/(',M*M1,'+',L*L1,')X',M*M1,'=',((d+i)-(((d+i)/(h+f))*f)+h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))))/((M*M1)+(L*L1))*(M*M1))
print('L:',(d+i)-(((d+i)/(h+f))*f)+h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))),'/(',M*M1,'+',L*L1,')X',L*L1,'=',((d+i)-(((d+i)/(h+f))*f)+h*((e+((h+f*g/100-a*b/100)*j/(h+f*g/100-a*b/100)))/((a*b/100)+(h+f*g/100-a*b/100))))/((M*M1)+(L*L1))*(L*L1))