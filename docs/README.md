# 🪖 Safety Helmet Detection

> **Note:** The current YOLOv8 model included in this project was trained for only 5 epochs due to limited computational resources. As a result, detection accuracy may not be optimal. For improved results, retrain the model for more epochs on a machine with better computational power.

A computer vision project that uses YOLOv8 to detect safety helmets in images. This project was developed by five students as part of the Intel AI4MFG Internship Program. It includes a Streamlit web application for easy helmet detection and compliance checking.

## 🚀 Features

- **Real-time Helmet Detection**: Detect helmets and heads in images using YOLOv8
- **Web Interface**: User-friendly Streamlit app for easy interaction
- **Industrial Potential**: Can be extended for CCTV camera monitoring
- **High Accuracy**: Trained model with confidence threshold of 0.5
- **Multiple Model Support**: Automatic model path detection
- **Visual Results**: Display detection results with bounding boxes
- **Scalable Architecture**: Ready for industrial deployment

## 📋 Requirements

- Python 3.8+
- OpenCV
- Ultralytics (YOLOv8)
- Streamlit
- PIL (Pillow)
- NumPy

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/arbazansari/helmet-detection-ai.git
   cd helmet-detection-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv helmet_env
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     helmet_env\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source helmet_env/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure

```
helmet-detection/
├── app.py                        # Streamlit web application
├── src/train_Yolo.py             # Training script for YOLOv8 model
├── test_model.py                 # Model testing script
├── convert_xml_to_yolo.py        # XML to YOLO format converter
├── split.py                      # Dataset splitting utility
├── data.yaml                     # YOLO dataset configuration
├── config.yaml                   # Configuration file
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── QUICKSTART.md                 # Quick start guide
├── TEAM.md                       # Team information
├── LICENSE                       # MIT License
└── .gitignore                    # Git ignore file
```

## 🎯 Usage

### Web Application

1. **Start the Streamlit app**
   ```bash
   streamlit run src/app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Upload an image** (JPG, JPEG, or PNG format)

4. **View results** with detection bounding boxes and confidence scores

### Industrial CCTV Implementation

This project can be extended for real-time helmet detection using CCTV cameras in industrial environments.

**Potential Implementation:**
```python
# Example: Real-time CCTV detection
import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO("best.pt")

# Connect to CCTV camera
cap = cv2.VideoCapture(0)  # or IP camera URL

while True:
    ret, frame = cap.read()
    results = model.predict(frame, conf=0.5)
    # Process detections and trigger alerts
```

**Industrial Applications:**
- **Construction Sites**: Monitor workers for helmet compliance
- **Manufacturing Plants**: Ensure safety protocols in hazardous areas
- **Mining Operations**: Remote safety monitoring
- **Oil & Gas Facilities**: Refinery safety compliance

**Key Features for Industrial Use:**
- Real-time helmet detection on video streams
- Multi-camera support for large facilities
- Automatic violation logging and alerting
- Integration with existing CCTV infrastructure
- Scalable for enterprise deployment

### Training Your Own Model

1. **Prepare your dataset** in YOLO format
2. **Update `data.yaml`** with your dataset paths
3. **Run training**
   ```bash
   python src/train_Yolo.py
   ```

### Testing the Model

```bash
python src/test_model.py
```

## 🔧 Configuration

### Model Paths
The application automatically searches for trained models in the following locations:
- `runs/detect/train/weights/best.pt`
- `archive/runs/detect/train/weights/best.pt`
- `archive/runs/detect/train2/weights/best.pt`
- `archive/runs/detect/train3/weights/best.pt`
- `archive/runs/detect/train4/weights/best.pt`
- `archive/runs/detect/train5/weights/best.pt`

### Dataset Configuration (`data.yaml`)
```yaml
train: images/train
val: images/val
nc: 2
names: ['helmet', 'head']
```

## 📊 Model Information

- **Classes**: 2 (helmet, head)
- **Architecture**: YOLOv8
- **Confidence Threshold**: 0.5
- **Input Size**: 640x640 pixels

## 🛠️ Development

### Adding New Classes
1. Update `data.yaml` with new class names
2. Retrain the model with updated dataset
3. Update the application code if needed

### Customizing Detection Parameters
Modify the confidence threshold and other parameters in `app.py`:
```python
results = model.predict(source=img_array, conf=0.5, save=False)
```

## 👥 Team

This project was developed by five students during the Intel AI4MFG Internship Program:

- **Arbaz Ansari Khwaza A** - Project Lead & AI Developer
- **MAHATO Ajaykumar Ramdev** - Machine Learning Engineer
- **MISHRA SHIVAM SANTOSH** - Computer Vision Developer
- **Rain Mohammad Atik** - Frontend Developer
- **SINGH SUKESH SUNIL** - Backend Developer

*For detailed team information, see [TEAM.md](TEAM.md)*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8 implementation
- [Streamlit](https://streamlit.io/) for the web application framework
- [OpenCV](https://opencv.org/) for computer vision capabilities

## 📞 Contact

For questions or support, please open an issue on GitHub.

## 🏭 Industrial Applications

This helmet detection system can be extended for various industrial safety applications:

### Construction Sites
- **Real-time Monitoring**: Detect workers without helmets on construction sites
- **Safety Compliance**: Ensure adherence to safety regulations
- **Incident Prevention**: Proactive safety monitoring

### Manufacturing Plants
- **Production Areas**: Monitor helmet usage in hazardous zones
- **Quality Control**: Ensure safety protocols are followed
- **Automated Auditing**: Continuous safety compliance tracking

### Mining Operations
- **Underground Safety**: Monitor helmet compliance in dangerous areas
- **Remote Monitoring**: Real-time oversight of multiple locations
- **Emergency Response**: Quick identification of safety violations

### Oil & Gas Facilities
- **Refinery Safety**: Monitor helmet usage in high-risk areas
- **Compliance Tracking**: Automated safety audit trails
- **Risk Management**: Proactive safety enforcement

### Implementation Approach
The current image-based detection can be extended to:
- **CCTV Integration**: Connect to existing surveillance cameras
- **Real-time Processing**: Process video streams for live monitoring
- **Alert Systems**: Automatic notifications for safety violations
- **Multi-camera Support**: Scale to multiple locations
- **Cloud Deployment**: Enterprise-level deployment options

## 🎓 Internship Project

This project was completed as part of an internship program, demonstrating practical application of computer vision and machine learning concepts in a real-world safety compliance scenario.

---

**Note**: Make sure to place your trained model file in one of the expected model paths before running the application. 