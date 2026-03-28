import numpy as np
import pandas as pd
import statsmodels.api as sm

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
model = sm.OLS(df_y,X).fit()
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

mean_y = np.mean(y)

b1 = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)

b0 = (sum_y - b1*sum_x) / n

y_hat = b0+(b1*x)


ssr = sum((y_hat-mean_y)**2)
sst = np.sum((y-mean_y)**2)
ssres = sst - ssr

r2 = ssr/sst

msr = ssr/df_reg
msres = ssres/df_res
f0 =msr/msres

print(r2)

# bảng anova

anova_table = pd.DataFrame({
    'source of variation': [
        'regression','residual','total'],
        'sum of squares': [ssr,ssres,sst],
        'degrees of freedom': [df_reg,df_res,df_total],
        'mean square': [msr,msres,''],
        'f0': [f0,'','']

    
})

print("\n bảng phương sai anova")
print(anova_table.to_string(index = False))