'''

# LSTM文本生成 #

**** 任务 ****
任务：基于task2_data，建立LSTM模型，生成文本：

**** 主要任务流程 ****
1、加载本地文本数据，生成字典
2、数据预处理：将数据转化为符合LSTM模型输入要求的数据，确认数据结构；
3、建立LSTM模型，进行模型训练，计算模型在训练、测试数据集的准确率
4、预测” Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines”的后续字符

**** 模型结构 ****
模型结构：单层LSTM，30神经元。每次使用前30个字符预测第31个字符

'''

''' ******** 数据加载 ********'''
#文本数据加载
data = open('task2_data').read()

''' ******** 数据预处理 ********'''
#移除换行符
data = data.replace('\n','').replace('\r','')
print(data)
#字符字母的去重处理
letters = list(set(data))
print(letters)
features = len(letters)
print(features)

#建立字典
#数字：字符字典
int_to_char = {a:b for a,b in enumerate(letters)}
print(int_to_char)
#字符：数字字典
char_to_int = {b:a for a,b in enumerate(letters)}
print(char_to_int)

#time_step
time_step = 30

#%%

import numpy as np
from tensorflow.keras.utils import to_categorical
#滑动窗口提取数据
def extract_data(data, slide):
    x = []
    y = []
    for i in range(len(data) - slide):
        x.append([a for a in data[i:i+slide]])
        y.append(data[i+slide])
    return x,y
#字符到数字的批量转化
def char_to_int_Data(x,y, char_to_int):
    x_to_int = []
    y_to_int = []
    for i in range(len(x)):
        x_to_int.append([char_to_int[char] for char in x[i]])
        y_to_int.append([char_to_int[char] for char in y[i]])
    return x_to_int, y_to_int
#实现输入字符文章的批量处理，输入整个字符、滑动窗口大小、转化字典
def data_preprocessing(data, slide, num_letters, char_to_int):
    char_Data = extract_data(data, slide)
    int_Data = char_to_int_Data(char_Data[0], char_Data[1], char_to_int)
    Input = int_Data[0]
    Output = list(np.array(int_Data[1]).flatten())
    Input_RESHAPED = np.array(Input).reshape(len(Input), slide)
    new = np.random.randint(0,10,size=[Input_RESHAPED.shape[0],Input_RESHAPED.shape[1],num_letters])
    for i in range(Input_RESHAPED.shape[0]):
        for j in range(Input_RESHAPED.shape[1]):
            new[i,j,:] = to_categorical(Input_RESHAPED[i,j],num_classes=num_letters)
    return new, Output

#字符串处理
# print(data)
X, y = data_preprocessing(data,time_step,features,char_to_int)

#数据分离
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=0)
print(X.shape,X_train.shape,X_test.shape)
print(len(y),len(y_train),len(y_test))
#输出结果的格式转化
y_train_c = to_categorical(y_train,features)

''' ******** 模型建立及模型训练 ********'''
#建立LSTM模型
from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()
#LSTM层
model.add(LSTM(units=30, input_shape=(X_train.shape[1],X_train.shape[2]),activation='relu'))
#输出层
model.add(Dense(units=features,activation='softmax'))
model.summary()
#核心参数配置
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
#模型训练
model.fit(X_train,y_train_c,batch_size=1000,epochs=50)
#训练数据的预测
y_train_predict = np.argmax(model.predict(X_train),axis=1)
#预测结果转化到字符
y_train_predict_char = [int_to_char[i] for i in y_train_predict]
print(y_train_predict_char)
#准确率
from sklearn.metrics import accuracy_score
accuracy_train = accuracy_score(y_train,y_train_predict)
print(accuracy_train)


#测试数据的预测
y_test_predict = np.argmax(model.predict(X_test),axis=1)
y_test_predict_char = [int_to_char[i] for i in y_test_predict]
print(y_test_predict_char)
accuracy_test = accuracy_score(y_test,y_test_predict)
print(accuracy_test)


#新字符串的预测
new_letters = 'Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines'
X_new,y_new = data_preprocessing(new_letters,time_step,features,char_to_int)
y_new_predict =np.argmax(model.predict(X_new),axis=1)
y_new_predict_char = [int_to_char[i] for i in y_new_predict]
print(y_new_predict_char)

for i in range(0,X_new.shape[0]-30):
    print(new_letters[i:i+30],'--predict new letter is>>>',y_new_predict_char[i])

'''

LSTM文本生成实战summary：

1、通过搭建LSTM模型，实现了英文字符文本生成；
2、掌握了文本加载、字典生成方法；
3、掌握了文本的数据预处理方法：字符转化、onehot格式转化、切片提取；
4、完成了基于新文本的字符预测

LSTM模型参考资料：https://keras.io/zh/layers/recurrent/#lstm

'''