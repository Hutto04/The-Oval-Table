from openpyxl import load_workbook
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

wb = load_workbook(filename = 'loggedMacro.xlsx')

sheet = wb.active

print(sheet.cell(2,2,).value)

counter = 1

for x in range(1, sheet.max_row):
        counter = counter + 1
       

print(counter)

lst = []

lst.append([1,2,3])
lst.append([4,5,6])
print(lst[1])

mainlst = []
templst= []
print("row count & column count:")
print(sheet.max_row)
print(sheet.max_column)

for column in range(1, sheet.max_column+1):
    for row in range(1, sheet.max_row+1):
        cellData = sheet.cell(row, column).value
        templst.append(cellData)
    mainlst.append(templst)
    templst = []

#print(mainlst[sheet.max_column-1][sheet.max_row-1])

firstfeature = mainlst[1][1:] #x rpi
firstfeature = np.array(firstfeature)
response = mainlst[-1][1:] #y oil
plt.figure(figsize=(1,1))
plt.scatter(firstfeature, response)
#plt.show()

poly = PolynomialFeatures(degree=2, include_bias=False)

poly_features = poly.fit_transform(firstfeature.reshape(-1, 1))
poly_reg_model = LinearRegression()
poly_reg_model.fit(poly_features, response)

y_predicted = poly_reg_model.predict(poly_features)

plt.figure(figsize=(10,6))
plt.title("Feature (x-axis) vs. Real Oil Prices(y-axis)", size=16)
plt.scatter(firstfeature, response)
plt.plot(firstfeature, y_predicted, c="red")
plt.show()







