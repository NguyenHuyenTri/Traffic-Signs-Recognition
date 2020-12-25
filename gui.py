import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy

# tải mô hinh đã train
from keras.models import load_model
model = load_model('traffic_classifier.h5')
# từ điển nhận diện biển báo
classes = {1: 'Tốc độ giới hạn (20km/h)',
           2: 'Tốc độ giới hạn (30km/h)',
           3: 'STốc độ giới hạn (50km/h)',
           4: 'Tốc độ giới hạn (60km/h)',
           5: 'Tốc độ giới hạn (70km/h)',
           6: 'Tốc độ giới hạn (80km/h)',
           7: 'Hết giới hạn tốc độ (80km/h)',
           8: 'Tốc độ giới hạn (100km/h)',
           9: 'Tốc độ giới hạn (120km/h)',
           10: 'Cấm vượt',
           11: 'Không vượt quá 3,5 tấn',
           12: 'Quyền ưu tiên tại giao lộ',
           13: 'Đường ưu tiên',
           14: 'Yield',
           15: 'Dừng',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'Cấm vào',
           19: 'General caution',
           20: 'Đường cong nguy hiểm bên trái',
           21: 'Đường cong nguy hiểm bên phải',
           22: 'Đường cong kép',
           23: 'Đường ghập ghềnh',
           24: 'Đường trơn trượt',
           25: 'Đường thu hẹp ở bên phải',
           26: 'Công trình đang thi công',
           27: 'Tín hiệu giao thông',
           28: 'Người đi bộ',
           29: 'Trẻ em băng đường',
           30: 'Xe đạp băng qua',
           31: 'Cẩn thận với băng / tuyết',
           32: 'Động vật hoang dã băng qua',
           33: 'Tốc độ kết thúc + giới hạn vượt',
           34: 'Rẽ phải phía trước',
           35: 'Rẽ trái phía trước',
           36: 'Ahead only',
           37: 'Đi thẳng hoặc sang phải',
           38: 'Đi thẳng hoặc sang trái',
           39: 'Đi bên phải',
           40: 'Đi bên trái',
           41: 'Bắt buộc đi vòng',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}
# khoi tao gui.py
top = tk.Tk()
top.geometry('800x600')
top.title('Phân loại biển báo giao thông')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign = classes[pred + 1]
    print(sign)
    label.configure(foreground='#011638', text=sign)


def show_classify_button(file_path):
    classify_b = Button(top, text="Phân loại hình ảnh", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload Ảnh", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))

upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Xác định biển báo GIAO THÔNG", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()
