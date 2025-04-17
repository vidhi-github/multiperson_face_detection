# **AURAVISION- Multiperson Real-Time Face Recognition System**  

## **Overview**  
**AURAVISION -** The **Multiperson Real-Time Face Recognition System** is a deep learning-based application designed for real-time face detection and recognition of multiple individuals in a frame. It uses advanced face detection techniques like **MTCNN** for face localization and **DLIB** for face recognition. The system efficiently handles multiframes and batched frames, leveraging GPU acceleration for fast and accurate results.  

This solution is ideal for applications such as automated attendance systems and surveillance systems, ensuring secure and reliable recognition even in real-time scenarios.  

---

## **Aim**  
To detect and recognize multiple faces in real-time using deep learning techniques with high accuracy and optimized performance on GPU-powered systems like NVIDIA DGX.  

---

## **Applications**  
1. 📋 **Attendance System** – Automate attendance tracking by recognizing faces in real-time.  
2. 🛡️ **Surveillance System** – Enhance security through continuous face monitoring and identification.  

---

## **Key Features**  
- 🧑‍🤝‍🧑 Real-time face detection and recognition of multiple people.  
- 🎯 High-accuracy vector embeddings for precise face matching.  
- 📦 Handles **multiframes** and **batched frames** efficiently.  
- ⚡ Optimized for GPU acceleration with CUDA (Batch size: 1 for GPU, 32 for DGX).  
- 🔄 Buffer management with **LOCK & UNLOCK** to prevent deadlock issues.  
- 🎥 Frame-wise processing using **OpenCV**.  
- 🖼️ Resolution reduction through down-sampling and up-sampling techniques.  
- 🌐 Flask-based web interface for easy real-time monitoring.  

---

## **Technologies Used**  
- **Python 3.8+**: Core programming language.  
- **OpenCV**: Image and video processing.  
- **TensorFlow**: Deep learning framework for face detection.  
- **MTCNN**: Multi-task Cascaded Convolutional Networks for face detection.  
- **DLIB**: For generating face embeddings and face recognition.  
- **CUDA**: For GPU acceleration, boosting real-time performance.  
- **Flask**: To build a web interface for real-time result visualization.  
- **NumPy & Pandas**: Data handling and manipulation.  

---

## **How Face Detection Works (MTCNN Architecture)**  
- **P-Net (Proposal Network):** Proposes candidate facial regions using non-maximum suppression.  
- **R-Net (Refine Network):** Refines proposals by returning bounding box coordinates.  
- **O-Net (Output Network):** Final face detection output with precise facial landmarks.  

---

## **Drawing Rectangles on Faces**  
To highlight detected faces with bounding boxes:  
```python
for face in faces:
    x, y, w, h = face['box']
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

output_path = "output.jpg"
cv2.imwrite(output_path, image)
print("Output saved successfully at:", output_path)
```  

---

## **Project Setup**  

### 🔄 **1. Clone the Repository**  
```bash
git clone https://github.com/vidhi-github/multiperson_face_detection.git
cd multiperson_face_detection
```  

### 💾 **2. Set Up the Virtual Environment**  
```bash
python -m venv myenv
```

### 🔌 **3. Activate the Environment**  
- **Windows:**  
```bash
myenv\Scripts\activate
```
- **Linux/macOS:**  
```bash
source myenv/bin/activate
```  

### 📦 **4. Install Dependencies**  
```bash
pip install tensorflow
pip install mtcnn
pip install opencv-python
pip install dlib
```  

### 🚀 **5. Run the Application**  
```bash
python app.py
```  

---

## **Deployment on NVIDIA DGX Server**  

### 🌐 **1. Access the DGX Server**  
Navigate to the DGX server's IP address:  
```plaintext
http://<DGX_IP_address>:<application_port>
```  

### 📂 **2. Transfer Project Files to DGX Server**  
```bash
scp -r -P <port_number> <local_folder> user@<DGX_IP>:<remote_folder>
```  

### 🎬 **3. Execute the Application on DGX**  
```bash
python3 app.py
```  

---

## **Output**  
- The system displays a real-time video feed with **bounding boxes** around detected faces.  
- Recognized faces are matched using **DLIB embeddings** with real-time updates on the web interface.  
- The processed frames are saved locally for further review.  

---

## **Buffer Management and Optimization**  
- The system manages **buffer overflow** by cleaning it whenever it exceeds a threshold (e.g., 10 frames).  
- Implements a **LOCK & UNLOCK** mechanism to prevent **deadlock** issues when processing multiframes and batched frames.  

---

## **Conclusion**  
The **Multiperson Face Recognition System** offers a robust solution for real-time face detection and recognition using advanced deep learning techniques. With efficient GPU utilization, buffer management, and accurate face embeddings, the system is suitable for large-scale deployments like attendance automation and surveillance systems.  

---

✨ **Built by:** *Vidhi Jindal*  
💡 *Thanks for exploring this project. Happy Learning!*  
