import os # operating system

# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不在
	print('yeah!找到檔案了！')
	with open('products.csv','r',encoding='utf-8') as f:
		for line in f:
			if '商品，價格' in line:
				continue # 繼續；跳到下一回的意思
			name, price = line.strip().split(',')
			products.append([name,price])
	print(products) 

else:
	print('找不到檔案......')

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = []
	p.append(name)
	p.append(price)
	# 以上三行可簡寫成 p = [name,price]
	products.append(p)
	# 或者以上四行簡寫成 products.append([name,price])
print(products)

# 印出所有購買紀錄
for product in products:
	print(product[0],'的價格是',product[1])

# 寫入檔案
with open('products.csv','w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n')