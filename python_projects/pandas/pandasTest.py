import pandas as pd
import re

titles = []
def testDataFrame():
    # 创建示例 DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Salary_USD': [50000, 60000, 70000]
    }
    df = pd.DataFrame(data)

    # 汇率转换函数
    def convert_salary_to_currency(salary_usd, exchange_rate):
        return salary_usd * exchange_rate

    # 汇率字典
    exchange_rates = {
        'USD_to_EUR': 0.88,  # 假设美元转欧元的汇率
        'USD_to_JPY': 113.14  # 假设美元转日元的汇率
    }

    # 对不同汇率应用转换函数
    for currency, rate in exchange_rates.items():
        # 创建新列，并将转换后的薪资赋值给新列
        df[currency] = df['Salary_USD'].apply(convert_salary_to_currency, exchange_rate=rate)

    print(df)

def countword():
    word2count = {}
    for i in range(len(df[titles[1]])):
        for j in df[titles[1]][i].split('，'):
            word2count[j] = word2count.get(j, 0) + 1
    return word2count

def constructDataFrame(df, word2count):
    data = {}
    name = [x for x in re.split('\d', df[titles[0]][1]) if x != '']
    for i in name:
        data[i] = [0 for i in range(df.shape[0])]
    for key, value in word2count.items():
        if value > 1:
            data[key] = [0 for i in range(df.shape[0])]
    return data

def countData(data):
    for i in range(len(df)):
        count = [x for x in re.split('\D', df[titles[0]][i]) if x != '']
        name = [x for x in re.split('\d', df[titles[0]][i]) if x != '']
        for j in range(len(name)):
            data[name[j]][i] = count[j]
        for j in df[titles[1]][i].split('，'):
            if j in data.keys():
                data[j][i] = data[j][i] + 1
    return data

if __name__ == '__main__':
    # 读取 Excel 文件
    df = pd.read_excel('F:\\HUAXINBeforeJob\\python_projects\\pandas\\pandas.xlsx')

    titles = df.columns.tolist()

    print(titles)

    # 显示 DataFrame 中的前几行数据
    print(df.head())

    print(df[titles[1]][0].split('，'))

    word2count = countword()  # Define the "wordCount" dictionary

    print(word2count)
    print(constructDataFrame(df, word2count))

    print(pd.DataFrame(countData(constructDataFrame(df, word2count))))

    df = pd.DataFrame(countData(constructDataFrame(df, word2count)))

    df.to_excel('your_modified_file.xlsx', index=False)


