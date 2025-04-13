class News:

    def __init__(self, tit, des, img):

        self.tit = tit
        self.des = des
        self.img = img

news1 = News(
    "iPhone 16 Pro Max",
    "The iPhone 16 Pro Max will feature a larger 6.9-inch display, powered by the A18 Pro chip with enhanced AI capabilities, and will include a new dedicated Capture button for improved camera functionality.",
    "https://github.com/elshangurbanow/images/blob/main/iPhone_16_Pro_Max.jpg?raw=true"
)

news2 = News(
    "AirPods Pro 3",
    "The AirPods Pro 3 are expected to feature new adaptive audio technology, improved noise cancellation, and potentially offer new color options. They are still in early development stage.",
    "https://github.com/elshangurbanow/images/blob/main/AirPods_Pro_3.jpg?raw=true"
)

news3 = News(
    "Apple Watch Ultra 3",
    "The Apple Watch Ultra 3 will likely maintain the same rugged design as its predecessor but may include new health features like blood pressure monitoring and sleep apnea detection, alongside minor hardware upgrades.",
    "https://github.com/elshangurbanow/images/blob/main/Apple_Watch_Ultra_3.jpeg?raw=true"
)

news_list = [news1, news2, news3]