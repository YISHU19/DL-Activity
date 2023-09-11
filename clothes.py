plt.figure(figsize=(6,4))

epochs = history.epoch
val = history.history['val_accuracy']
traun = history.history['accuracy']

plt.plot(epochs, val, color = 'black', linestyle = 'solid', label = 'validation')
plt.plot(epochs, train, color = 'blacl', linestyle = 'dashed', label = 'train')

plt.title('Model with, lr=0.001')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.xticks(np.arange)

plt.legend()

plt.savefig('xception_v1_0_01.svg')
plt.show()

!pip install gradio

import gradio as gr

name = train_data.class_indices.keys()
name

def predict_img(img):
    img_3d = img.reshape(-1,180,180,3)
    prediction = model.predict(img_3d)[0]
    return {name[i]: float(prediction[i]) for i in range(5)}

image = gr.inputs.Image(shape=(180,180))
label = gr.outputs.Label(num_top_classes=5)

web = gr.Interface(fn = predict_img, inputs = image, outputs = label, capture_session = True)
web.launch(share = 'True', debug = 'True')

