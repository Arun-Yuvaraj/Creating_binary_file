from binary_data import binary_data

def main():
    #binary_data.build_dataset(original_folder="minimnist", output_binary_dataset="bin_dataset.h5")

    #To use get and store functions
    b = binary_data()
    #image, image_mask, image_maskinv, label, points = b.get(key="47",output_binary_dataset="bin_dataset.h5")

    b.store('46','image1','000000_image_maskinv.png','bin_dataset.h5')


if __name__ == "__main__":
    main()    
    