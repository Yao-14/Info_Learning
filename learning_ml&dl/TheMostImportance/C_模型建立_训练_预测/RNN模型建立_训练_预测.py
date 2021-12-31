'''
************ 模型建立和训练通用流程 ************
    from keras.models import Sequential
    # 建立模型    model = Sequential()
    # 加输入层    model.add()
    ...(可以增加任意多层）
    # 加输出层    model.add()
    # 模型配置    model.compile()
    # 模型训练    model.fit(X,y)

************ 基本RNN结构模型 ———— SimpleRNN ************
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN
model = Sequential()
model.add(SimpleRNN(units,input_shape,activation))
model.add(Dense(units,activation))
model.compile(optimizer,loss)
model.fit(X,y,batch_size,epochs)

************ LSTM结构模型 ———— LSTM ************
from keras.models import Sequential
from keras.layers import Dense, LSTM
model = Sequential()
model.add(LSTM(units, input_shape,activation))
model.add(Dense(units,activation))
model.compile(optimizer,loss,metrics)
model.fit(X,y,batch_size,epochs)

'''
