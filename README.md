# Dataset of Weeds in Potato Crops in the Province of Carchi and Imbabura, Ecuador  

This dataset was collected in **the provinces of Carchi and Imbabura, Ecuador**, using images acquired by a drone over potato crop fields.  

## 📂 Dataset Structure  
The dataset is divided into two versions:  

- **Unbalanced/**: Contains the original images without modifications to the class distribution.  
- **Balanced/**: A **class balancing** process was applied to ensure a more equitable representation of all weed categories, improving the segmentation model’s performance.  

### 🔹 **Balancing Process**  
To balance the class distribution in the dataset, the following strategies were applied:  
1. **Data Augmentation**: Techniques such as rotations, translations, and lighting adjustments were used to increase the number of images of underrepresented classes.  
2. **Stratified Selection**: The number of images from overrepresented classes was reduced to achieve a more balanced proportion.  

This balancing improves the model’s ability to accurately recognize all classes.  

### 🎨 **RGB Mask Generation** 
To improve visual interpretation and support the reproducibility of the segmentation results, RGB versions of all masks have been generated and are included in the dataset.

### 🗂️ **New Folder: RGB_masks**
A new folder named RGB_masks has been added inside each data partition (train, val, test) in both versions of the dataset: Balanced/ and Unbalanced/.
Each image in the RGB_masks/ folder corresponds to the original grayscale mask, but with colored classes for easier visualization. The filename includes the suffix _RGB.

### 🎯 **Class-to-Color Mapping**
The following color coding was used for each class:

| Class Name     | RGB Value        | Color Name      |
|----------------|------------------|------------------|
| Cow-tongue     | (0, 0, 255)      | 🔵 Blue          |
| Dandelion      | (255, 165, 0)    | 🟠 Orange        |
| Kikuyo         | (255, 255, 0)    | 🟡 Yellow        |
| Other          | (128, 0, 128)    | 🟣 Purple        |
| Potato         | (0, 128, 0)      | 🟢 Green         |

### 🐍 **Script Used: mask_visualization.py**
The script used to generate the RGB masks is included in the root of this repository.

Functionality:

- It scans all grayscale masks in /masks/
- Converts them to RGB based on class index
- Saves them into the corresponding /RGB_masks/ folder with _RGB added to the filename

## 📄 Additional Information  
This dataset can be used for image segmentation tasks in the automatic detection of weeds in potato crops.  

