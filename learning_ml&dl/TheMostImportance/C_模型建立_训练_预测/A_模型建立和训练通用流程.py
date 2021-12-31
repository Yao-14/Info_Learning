'''

************ 模型建立和训练通用流程 ************
    from keras.models import Sequential
    # 建立模型    Model = Sequential()
    # 加输入层    Model.add()
    ...(可以增加任意多层）
    # 加输出层    Model.add()
    # 模型配置    Model.compile()
    # 模型训练    Model.fit(X,y)

************ Sequential.add(layer) ---- 添加层 ************
Sequential.add(layer): 在层栈的顶部添加一个层实例。

************ Sequential.pop(layer) ---- 删除层 ************
Sequential.pop(layer): 去除模型中的最后一层。

************ Model.compile() ---- 配置用于训练的模型 ************

Model.compile(optimizer="rmsprop",      # 优化器。字符串（优化器名称）或优化器实例。参见 tf.keras.optimizers。
              loss=None,                # 损失函数。 字符串（损失函数的名称）或损失函数实例。参见tf.keras.losses.Loss。
              metrics=None)             # 模型在训练和测试期间要评估的指标列表。参见 tf.keras.metrics。
              ******** 以上是最重要的参数 ********
              其余参数详见 https://keras.io/api/models/model_training_apis/#compile-method

************ Model.fit() ---- 为固定数量的历元(数据集上的迭代)训练模型 ************

Model.fit(x=None,                       # 输入数据.  Numpy array(s) or TensorFlow tensor(s).
          y=None,                       # 目标数据.  Numpy array(s) or TensorFlow tensor(s).
          batch_size=None,              # 每个梯度更新的样本数，默认为32。 Integer or None.
          epochs=1,                     # 训练模型的迭代数。Integer.
          initial_epoch=0)              # 开始训练的迭代次( 对恢复以前的训练运行有益 )。Integer.
          ******** 以上是最重要的参数 ********
          其余参数详见 https://keras.io/api/models/model_training_apis/#fit-method

'''

''' ************ Example ************ '''
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,SimpleRNN
# 建立模型
model = Sequential()
# 添加层————输入层
model.add(SimpleRNN(units=5,input_shape=(10,1),activation='relu'))
#输出层
model.add(Dense(units=1,activation='linear'))
#模型配置
model.compile(optimizer='adam',loss='mean_squared_error')
#模型训练
model.fit(X,y,batch_size=30,epochs=200)
