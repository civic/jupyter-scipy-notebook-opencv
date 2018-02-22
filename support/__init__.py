import cv2 as cv
from IPython.display import Image

def cv_img(image, format='.png'):
    decoded_bytes = cv.imencode(format, image)[1].tobytes()
    display(Image(data=decoded_bytes))
    
def __magic_cv_img(line):
    ip.run_code("import support; support.cv_img("+line+")")

ip = get_ipython()
ip.register_magic_function(__magic_cv_img, 'line', 'cv_img')

