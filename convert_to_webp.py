from PIL import Image
import os

# convert all images in a folder to webp format
def convert_to_webp(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            im = Image.open(os.path.join(folder, filename)).convert('RGB')
            im.save(os.path.join(folder, filename[:-4] + ".webp"), "webp")
            print("Converted {} to webp".format(filename))
        else:
            print("{} is not a png or jpg file".format(filename))


if __name__ == '__main__':
    for folder in os.listdir('assets/images/'):
        convert_to_webp('assets/images/' + folder)

