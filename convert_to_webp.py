from PIL import Image
import os

# convert all images in a folder to webp format
def convert_to_webp(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".svg"):
            from cairosvg import svg2png
            svg2png(url=os.path.join(folder, filename), write_to=os.path.join(folder, filename.replace('.svg', '.png')))
        if filename.endswith(".jpg") or filename.endswith(".png"):
            im = Image.open(os.path.join(folder, filename)).convert('RGB')
            im.save(os.path.join(folder, filename[:-4] + ".webp"), "webp")
            print("Converted {} to webp".format(filename))
            os.remove(os.path.join(folder, filename))
        else:
            print("{} is not a png or jpg file".format(filename))


def responsible_image_resize(image_path):

    # resize image with same aspect ratio, treat original image as biggest size and create small and medium size
    # small size is 1/4 of original image
    # medium size is 1/2 of original image
    # large size is original image
    img = Image.open(image_path)
    width, height = img.size
    if width > height:
        small_width = width // 4
        small_height = height // 4
        medium_width = width // 2
        medium_height = height // 2
    else:
        small_width = width // 4
        small_height = height // 4
        medium_width = width // 2
        medium_height = height // 2
    # resize image
    small_img = img.resize((small_width, small_height), Image.ANTIALIAS)
    medium_img = img.resize((medium_width, medium_height), Image.ANTIALIAS)
    # save image
    small_img.save(image_path[:-4] + "_small.webp", "webp")
    medium_img.save(image_path[:-4] + "_medium.webp", "webp")
    img.save(image_path[:-4] + "_large.webp", "webp")

def resize_width(image_path, width):
    img = Image.open(image_path)
    height = int(width * img.size[1] / img.size[0])
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(image_path[:-4] + "_resized.webp", "webp")

if __name__ == '__main__':
    # for each assets/images in the folder create large, medium and small versions
    for file in os.listdir('assets/images/anto'):
        if file.endswith('.webp'):
            resize_width(os.path.join('assets/images/anto', file), 400)






