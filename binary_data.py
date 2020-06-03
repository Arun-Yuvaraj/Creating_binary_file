import numpy as np
import h5py
import cv2
import os

class binary_data:
    def __init__(self):
        self.class_name = "create_binary_dataset"                  

    @staticmethod
    def build_dataset(original_folder=None, output_binary_dataset=None):

        # to check if output binary file is of correct format
        if not (output_binary_dataset.endswith('.h5')):
            print('Provide a proper hdf5 file')
            return

        # creating binary file with 0 data
        with h5py.File(output_binary_dataset, 'w') as test:
            G1 = test.create_group('000000')
            G1.create_dataset('image', (28,28,3))
            G1.create_dataset('image_mask', (28,28,3))
            G1.create_dataset('image_maskinv', (28,28,3))
            G1.create_dataset('label', ( ))
            G1.create_dataset('points', (10, ))

            # parsing through all the files and storing it in binary file
            for i in os.listdir(original_folder):
                if (i.endswith('.jpg') or i.endswith('.png')):
                    file = os.path.join(os.getcwd(), original_folder,i)
                    data = cv2.imread(file)                    

                else:
                    file = os.path.join(os.getcwd(), original_folder,i)
                    data = np.loadtxt(file)
                    
                filename = i[:-4]
                out = filename.split("_",1)
                key = out[0]
                tag = out[1]
                b = binary_data()
                b.store(key=key, tag=tag, new_data=data, output_binary_dataset=output_binary_dataset)


    # store function to store new values in the binary file
    
    def store(self,key=None, tag=None, new_data=None,output_binary_dataset=None):

        # checking if all the provided parameters are correct in order to store the data in the binary file
        if not (output_binary_dataset.endswith('.h5')):
            print('Provide a proper hdf5 file')
            return

        if (tag != 'image' and tag != 'image_mask' and tag!= 'image_maskinv' and tag!= 'label' and tag != 'points'):
            print('tag is not valid. Please choose and provide tag as image or image_mask or image_maskinv or label '
                  'or points')
            return

        if (type(new_data) != np.ndarray):
            if not (new_data.endswith('.jpg') or new_data.endswith('.png') or new_data.endswith('.txt')):
                print('Please provide image or text data')
                return

        # storing data in binary file
        if (type(new_data) != np.ndarray):
            if (new_data.endswith('.jpg') or new_data.endswith('.png')):
                file = os.path.join(os.getcwd(), "minimnist",  new_data)

                new_data = cv2.imread(file)

            else:
                file = os.path.join(os.getcwd(), "minimnist", new_data)

                new_data = np.loadtxt(file)

        key_tag = key + '/' + tag
        f = h5py.File(output_binary_dataset, 'r+')
        for keys in f.keys():
            if (key == keys):
                data = f[key_tag]
                data[...] = new_data
                return
        f.close()
        
        with h5py.File(output_binary_dataset, 'a') as test:
            
            G1 = test.create_group(key)
            if (tag == 'image'):
                G1.create_dataset('image', data = new_data)
            else:
                G1.create_dataset('image', (28,28,3))
            if (tag == 'image_mask'):
                G1.create_dataset('image_mask', data = new_data)
            else:
                G1.create_dataset('image_mask', (28,28,3))
            if (tag == 'image_maskinv'):
                G1.create_dataset('image_maskinv', data = new_data)
            else:
                G1.create_dataset('image_maskinv', (28,28,3))
            if (tag == 'label'):
                G1.create_dataset('label', data = new_data)
            else:
                G1.create_dataset('label', ( ))
            if (tag == 'points'):
                G1.create_dataset('points', data = new_data)
            else:
                G1.create_dataset('points', (10, ))

    # get function to retrieve all the data from binary file with the help of key

    def get(self,key=None,output_binary_dataset=None):

        if not (output_binary_dataset.endswith('.hd5')):
            print('Provide a proper hdf5 file')
            return

        image = key + '/' + 'image'
        image_mask = key + '/' + 'image_mask'
        image_maskinv = key + '/' + 'image_maskinv'
        label = key + '/' + 'label'
        points = key + '/' + 'points'
        cap = 0
        f = h5py.File(output_binary_dataset, 'r+')
        for keys in f.keys():
            if (key == keys):
                cap = 1
                image = np.array(f[image])
                image_mask = np.array(f[image_mask])
                image_maskinv = np.array(f[image_maskinv])
                label = np.array(f[label])
                points = np.array(f[points])

        if cap == 0:
            print("Key not found")
        f.close()
        return image, image_mask, image_maskinv, label, points
