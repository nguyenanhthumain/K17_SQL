import numpy as np
import pandas as pd


# Nhập dữ liệu
y = np.array([2158.70,1678.15,2316.00,2061.30,2207.50,
              1708.30,1784.70,2575.00,2357.90,2256.70,
              2165.20,2399.55,1779.80,2336.75,1765.30,
              2053.50,2414.40,2200.50,2654.20,1753.70])

x = np.array([15.50,23.75,8.00,17.00,5.50,
              19.00,24.00,2.50,7.50,11.00,
              13.00,3.75,25.00,9.75,22.00,
              18.00,6.00,12.50,2.00,21.50])

n = len(x)

# Tính các tổng cần thiết
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x**2)

# Ước lượng beta1
beta1 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)

# Ước lượng beta0
beta0 = (sum_y - beta1*sum_x) / n

print("beta0 =", round(beta0,4))
print("beta1 =", round(beta1,4))

df_reg = 1
df_res = n-2
df_total = n-1

ssr = beta1*(n*sum_xy - sum_x*sum_y)
sst = np.sum((y-(beta0+beta1*x))**2)
ssres = sst - ssr
ms_r = ssr/df_reg
ms_res = ssres/df_res

f0 = ms_r/ms_res

# bảng anova

r2 = ssr/sst
print("R^2 =",r2)



import statsmodels.api as sm
data = pd.DataFrame(
    {
        'Độ tuổi chất làm đầy': [15.50,23.75,8.00,17.00,5.50,
              19.00,24.00,2.50,7.50,11.00,
              13.00,3.75,25.00,9.75,22.00,
              18.00,6.00,12.50,2.00,21.50],
              'độ bền cat' : [2158.70,1678.15,2316.00,2061.30,2207.50,
              1708.30,1784.70,2575.00,2357.90,2256.70,
              2165.20,2399.55,1779.80,2336.75,1765.30,
              2053.50,2414.40,2200.50,2654.20,1753.70]
    }
)
# tach bien
x = data['Độ tuổi chất làm đầy']
y = data['độ bền cat']
X = sm.add_constant(x)
model = sm.OLS(y,X).fit()

#hien thi ket qua
print("\nbảng kết quả")
print(model.summary())



x = np.array(
    [
        6,10,12,14,16
    ]
)
y = np.array(
    [
        40,44,46,48,52
    ]
)

df_data = pd.DataFrame({
    'phân bón': [
        6,10,12,14,16
    ],
    'năng suất' : [
        40,44,46,48,52
    ]
})

df_x = df_data['phân bón']
df_y = df_data['năng suất']
X = sm.add_constant(df_x)
model = sm.OLS(y,X).fit()
print("\nbảng kết quả")
print(model.summary())


sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xx = np.sum(x*x)
sum_xy = np.sum(x*y)

n = len(x)

df_reg = 1
df_res = n-2
df_total = n-1

b1 = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)

b0 = (sum_y - b1*sum_x) / n

ssres = sum((sum_y-(b0+b1*x))**2)

ssr = sum(((b0+b1*x)-(sum_y/n))**2)

sst = ssres + ssr

r2 = ssr/sst

msr = ssr/df_reg
msres = ssres/df_res
f0 =msr/msres


# lập bảng phương sai anova











