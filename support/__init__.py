import cv2 as cv
from IPython.display import Image
from IPython.core.magic_arguments import (argument, magic_arguments, parse_argstring)
import argparse

def cv_img(image, scale=100, format='.png'):
    decoded_bytes = cv.imencode(format, image)[1].tobytes()
    display(Image(data=decoded_bytes))

    
@magic_arguments()
@argument('-s', '--scale', type=float, help='output image scale. (0-100) percent', default=100.0)
@argument('image', nargs=argparse.REMAINDER, help='image')
def __magic_cv_img(arg):
    args = parse_argstring(__magic_cv_img, arg)
    ip.run_code("__a=%s" % "".join(args.image))
    cv_img(ip.user_ns['__a'], args.scale)


ip = get_ipython()
ip.register_magic_function(__magic_cv_img, 'line', 'cv_img')

