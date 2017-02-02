
import json
import re
import os
from pprint import pprint
from PIL import Image


## Directory where all photos will be croped
BASE_CROP_DIRECTORY = 'croped'
## Directory where all photos were downloaded
BASE_IMG_DIRECTORY = 'imgs'

"""
    Crop all images bounding boxes described in json_file.

    @json_file: data set file, only test and train.
    @source_dir: directory where all images where downloaded.
    @dest_dir: directory where croped image will be saved.
"""
def cropImages (json_file, source_dir, dest_dir): #'meta/json/test_pairs_hats.json', 'imgs/hats/test'

    with open(json_file) as data_file:
        data = json.load(data_file)

    boxes = {}

    for row in data:
        #Read data from json
        photo_id = row['photo']
        product = row['product']
        bbox = row['bbox']

        #name of saved image file
        img_name = int(photo_id) + ".jpeg"
        #open image file from source_dir
        im = Image.open(source_dir + "/" + f)
        #crop image
        croppedImage = im.crop((bbox['left'],
            bbox['top'],
            bbox['left']+bbox['width'],
            bbox['top']+bbox['height']))

        #save croped image
        croppedImage.save(dest_dir + "/" + image_file_name(product, photo_id))

crop_queue = Queue()

"""
    Name of image that correspond to a product in a photo.
"""
def image_file_name(product, photo):
    return '{}@{}.jpeg'.format(photo, product)

def create_needed_directories():
    for category in categories:
        for partition in partitions:
            if not os.path.exists( directory_path(category, partition) ):
                os.makedirs( directory_path(category, partition) )

def directory_path(category, partition):
    '{}/{}/{}'.format(BASE_CROP_DIRECTORY, category, partition)

"""
    Start croping all images. Ensure that destiny directory already exists.
"""
def start_async_crop():
    partitions = ['train', 'test']
    categories = ['bags', 'belts', 'dresses', 'eyewear', 'footwear', 'hats', 'leggings', 'outerwear', 'pants', 'skirts', 'tops']

    for category in categories:
        for partition in partitions:
            #Set to crop all pictures
            json_file = 'meta/json/{}_pairs_{}.json'.format(partition, category)
            dest_dir = directory_path(category, partition)
            crop_queue.put((json_file, dest_dir))

    print('Set to crop {} pictures'.format(crop_queue.qsize()))

    #Each worker that consume items from photos_queue
    def worker():
        while not photos_queue.empty():
            json_file, dest_dir = crop_queue.get()
            #proccess item
            cropImages(json_file,BASE_IMG_DIRECTORY, dest_dir)
            crop_queue.task_done()

    # Start each worker in a diferent thread
    for i in range(NUM_WORKER_THREAD):
        t = Thread(target = worker)
        t.daemon = True
        t.start()

    photos_queue.join()
    print("All tasks completed")

if __name__ == '__main__':
    create_needed_directories()

    NUM_WORKER_THREAD = 12
    start_async_crop()
