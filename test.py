from binary_data import binary_data


def main():

     # static method to create a binary file
     binary_data.build_dataset(original_folder="minimnist", output_binary_dataset="bin_dataset.h5")

     # To use get and store functions
     #b = binary_data()
     # image, image_mask, image_maskinv, label, points = b.get(key="46",output_binary_dataset="bin_dataset.h5")
     # print(image)

     # For storing data, please use image or text file as new_data and tag should be either image or image_mask or image_maskinv or label or points
     #b.store(key='46', tag='image_mask', new_data='000000_image_maskinv.png', output_binary_dataset='bin_dataset.h5')


if __name__ == "__main__":
    main()
