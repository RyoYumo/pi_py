import decimal
decimal.getcontext().prec = 1001  # 1001桁指定
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np

PI_1000 = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"




# arctanの値を第upper項まで求める
def arctan( x, upper ):
    summ = 0
    for n in range( upper ):
        summ += Decimal( (-1)**n) / Decimal(2*n+1) * x **(2*n+1)
    return summ

# 計算結果を整数部と５桁の小数に区切って表示する関数
def printNumber( num ):
    snum = str( num )
    rlist = snum.split( "." )
    print( rlist[ 0 ] + "." )
    number = rlist[ 1 ]
    fivelist = [ number[i:i+5] for i in range( 0, len(number), 5) ]
    for five in fivelist:
        print( five, end=" " )
    print()

index = [1,100,200,300,400,500,600,700,800,900,1000]
diffs_Euler =[]

for x in index:
    items = x
    second = Decimal( 1 ) / Decimal( 2 )
    third = Decimal( 1 ) / Decimal( 3 )
    result = (arctan( second, items ) + arctan( third, items )) * Decimal(4)
    # print(Decimal(result - Decimal(PI_1000)))
    # print(math.log10(-1 * Decimal(result - Decimal(PI_1000))))
    diff = Decimal(result - Decimal(PI_1000))
    diffs_Euler.append(np.log10(abs(diff)))


index = [1,100,200,300,400,500,600,700,800,900,1000]
diffs_Machin =[]

for x in index:
    items = x
    fifth = Decimal( 1 ) / Decimal( 5 )
    recip239 = Decimal( 1 ) / Decimal( 239 )
    result = ( Decimal( 4 ) * arctan( fifth, items ) - \
        arctan( recip239, items ) ) * Decimal( 4 )
    diff = Decimal(result - Decimal(PI_1000))
    diffs_Machin.append(np.log10(abs(diff)))
    print(result)

index = [1,100,200,300,400,500,600,700,800,900,1000]
diffs_Gauss =[]

for x in index:
    items = x
    recip18 = Decimal( 1 ) / Decimal( 18 )
    recip57 = Decimal( 1 ) / Decimal( 57 )
    recip239 = Decimal( 1 ) / Decimal( 239 )
    result = ( Decimal( 12 ) * arctan( recip18, items ) + \
        Decimal( 8 ) * arctan( recip57, items ) - Decimal(5) * arctan(recip239, items) ) * Decimal( 4)
    diff = Decimal(result - Decimal(PI_1000))
    diffs_Gauss.append(np.log10(abs(diff)))
    # print(result)

index = [1,100, 200, 300, 400,500,600,700,800,900,1000]
diffs_Stormer =[]

for x in index:
    items = x
    eighth = Decimal( 1 ) / Decimal( 8 )
    recip57 = Decimal( 1 ) / Decimal( 57 )
    recip239 = Decimal( 1 ) / Decimal( 239 )
    result = ( Decimal( 6 ) * arctan( eighth, items ) + \
        Decimal( 2 ) * arctan( recip57, items) + \
        arctan( recip239, items ) ) * Decimal( 4 )
    diff = Decimal(result - Decimal(PI_1000))
    diffs_Stormer.append(np.log10(abs(diff)))

index = [1,100, 200, 300, 400,500,600,700,800,900,1000]
diffs_Takano =[]
for x in index:
    items = x
    recip49 = Decimal( 1 ) / Decimal( 49 )
    recip57 = Decimal( 1 ) / Decimal( 57 )
    recip239 = Decimal( 1 ) / Decimal( 239 )
    recip110443 = Decimal( 1 ) / Decimal( 110443 )
    result = ( Decimal( 12 ) * arctan( recip49, items ) + \
        Decimal( 32 ) * arctan( recip57, items ) - Decimal(5) * arctan(recip239, items)  + Decimal(12) * arctan(recip110443, items)) * Decimal( 4)
    diff = Decimal(result - Decimal(PI_1000))
    diffs_Takano.append(np.log10(abs(diff)))


# print(diffs)
plt.figure()
plt.plot(index, diffs_Euler, 'o-')
plt.plot(index, diffs_Machin, 'x-')
plt.plot(index, diffs_Gauss, 'x-')
plt.plot(index, diffs_Stormer,'x-')
plt.plot(index, diffs_Takano, 'o-')
plt.title('Machin')
plt.ylabel('log10(abs(error))')
plt.xlabel('items')
# plt.yscale('log')
plt.show()

    # print(diff)
    # print(math.log10(abs(diff)))
    # print(math.log10(-1 * (Decimal(result - Decimal(PI_1000)))))



    # print(math.log10(-1))


# # オイラーの公式を用いてπの値を計算する
# # 求める項数をitemsとする
# items = 1000
# second = Decimal( 1 ) / Decimal( 2 )
# third = Decimal( 1 ) / Decimal( 3 )
# result = (arctan( second, items ) + arctan( third, items )) * Decimal(4)
# print(Decimal(result - Decimal(PI_1000)))
# # print( "オイラーの公式で、"+str(items)+"項までarctanを展開" )
# # printNumber( result )
#
#
#
# items = 700
# fifth = Decimal( 1 ) / Decimal( 5 )
# recip239 = Decimal( 1 ) / Decimal( 239 )
# result = ( Decimal( 4 ) * arctan( fifth, items ) - \
#     arctan( recip239, items ) ) * Decimal( 4 )
# # print( "マチンの公式で、"+str(items)+"項までarctanを展開")
# print(Decimal(result - Decimal(PI_1000)))
# # print( "オイラーの公式で、"+str(items)+"項までarctanを展開" )
# # printNumber( result )
