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

## 📄 Additional Information  
This dataset can be used for image segmentation tasks in the automatic detection of weeds in potato crops.  
