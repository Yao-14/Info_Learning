
# 模型加载
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
model_new = load_model('task1_model_1.h5')

# 测试数据集预测准确率
train_datagen = ImageDataGenerator(rescale=1. / 255)
test_set = train_datagen.flow_from_directory('./task1_data/test_set', target_size=(50, 50), batch_size=32,
                                             class_mode='binary')
J_test,accuracy_test = model_new.evaluate(test_set)
print(accuracy_test)

# 单张图片的预测v (pip install pillow)
from keras.preprocessing.image import load_img, img_to_array

pic_1 = './predict_data/1.png'
pic_1 = load_img(pic_1, target_size=(50, 50))
pic_1 = img_to_array(pic_1)
pic_1 = pic_1 / 255
pic_1 = pic_1.reshape(1, 50, 50, 3)

result = (model_new.predict(pic_1) > 0.5).astype("int32")
print('dog' if result == 1 else 'cat')
fig2 = plt.figure()
plt.imshow(pic_1[0])
plt.show()
# %%

# 本地九张图片处理
a = [i for i in range(1, 10)]
fig3 = plt.figure(figsize=(10, 10))
for i in a:
    img_name = f'./predict_data/{i}.png'
    pic_1 = load_img(img_name, target_size=(50, 50))
    pic_1 = img_to_array(pic_1)
    pic_1 = pic_1 / 255
    pic_1 = pic_1.reshape(1, 50, 50, 3)
    result = (model_new.predict(pic_1) > 0.5).astype("int32")
    #     print('dog' if result==1 else 'cat')
    plt.subplot(3, 3, i)
    plt.imshow(pic_1[0])
    plt.title('predict result: dog' if result == 1 else 'predict reuslt:cat')
plt.show()