'''

************ 模型预测方法合集 ************
    # 模型预测方法一    y_predict = Model.predict(X)
    # 模型预测方法二    y_predict = np.argmax(Model.predict(X),axis=1)
    # 模型预测方法三    y_predict = (Model.predict(x) > 0.5).astype("int32")
    (方法二、三是对以去除的函数Model.predict_classes()的代替）

************ Model.predict(X) ---- 对输入样本生成输出预测 ************
Model.predict(x,                # 输入数据.  Numpy array(s) or TensorFlow tensor(s).
              batch_size=None,  # 每个梯度更新的样本数，默认为32。 Integer or None.
              verbose=0,
              steps=None,
              callbacks=None,
              max_queue_size=10,
              workers=1,
              use_multiprocessing=False)
              ******** 以上是最重要的参数 ********
              其余参数详见https://keras.io/api/models/model_training_apis/#predictonbatch-method

************ np.argmax(Model.predict(X),axis=1) ---- 模型进行多类分类时使用 ************
If your model does multi-class classification: (e.g. the last-layer activation = softmax）:

              y_predict = np.argmax(Model.predict(X),axis=1)

************ (Model.predict(x) > 0.5).astype("int32") ---- 模型进行二分类时使用 ************
if your model does binary classification (e.g. the last-layer activation = sigmoid):

              y_predict = (Model.predict(x) > 0.5).astype("int32")

'''