import cv2 as cv
from IPython.display import Image
from IPython.core.magic_arguments import (argument, magic_arguments, parse_argstring)

def cv_img(images, scale=100, format='.png'):
    for img in images:
        decoded_bytes = cv.imencode(format, img)[1].tobytes()
        display(Image(data=decoded_bytes))

    
@magic_arguments()
@argument('-s', '--scale', type=float, help='output image scale. (0-100) percent', default=100.0)
@argument('images', nargs='+', help='images')
def __magic_cv_img(arg):
    args = parse_argstring(__magic_cv_img, arg)
    images = [ip.user_ns[n] for n in args.images]
    cv_img(images, args.scale)


ip = get_ipython()
ip.register_magic_function(__magic_cv_img, 'line', 'cv_img')

