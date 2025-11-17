# 💪 Personal Trainer - AI-Powered Sports Activity Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

AI-powered sports activity detection system using computer vision. Analyzes human movements and identifies sports activities through pose estimation in real-time.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Supported Activities](#supported-activities)
- [Applications](#applications)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Real-time Activity Recognition**: Identify sports activities in real-time from video streams
- **Pose Estimation**: Advanced human pose detection and analysis
- **Movement Analysis**: Analyze and track human movements accurately
- **Multiple Activity Support**: Detect various sports and fitness activities
- **Video Processing**: Process pre-recorded videos for activity analysis
- **Fitness Tracking**: Track exercise form and repetitions
- **Computer Vision**: Built with OpenCV and machine learning models

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Webcam or video file for input
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/talha-eren/Personal_Trainer.git
cd Personal_Trainer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install opencv-python numpy mediapipe tensorflow
```

### Step 3: Verify Installation

```bash
python personal_trainer.py --help
```

## 💻 Usage

### Basic Video Analysis

```bash
python personal_trainer.py --video video1.mp4
```

### Multiple Video Analysis

```bash
python personal_trainer.py --video video1.mp4 video2.mp4
```

### Real-time Webcam Analysis

```bash
python personal_trainer.py --webcam
```

### Custom Options

```bash
python personal_trainer.py \
    --video path/to/video.mp4 \
    --output results/ \
    --confidence 0.5 \
    --display
```

### Parameters

- `--video`: Path to video file(s) for analysis
- `--webcam`: Use webcam for real-time detection
- `--output`: Directory to save analysis results
- `--confidence`: Confidence threshold for detection (default: 0.5)
- `--display`: Display results in real-time window

## 📁 Project Structure

```
Personal_Trainer/
│
├── personal_trainer.py      # Main application script
├── video1.mp4                # Sample video 1
├── video2.mp4                # Sample video 2
├── requirements.txt          # Python dependencies (if exists)
├── README.md                 # Project documentation
└── .gitignore               # Git ignore file
```

## 🏃 Supported Activities

The system can detect and analyze various sports activities including:

- **Running/Jogging**
- **Walking**
- **Cycling**
- **Jumping**
- **Push-ups**
- **Squats**
- **Pull-ups**
- **Yoga Poses**
- **Dancing**
- **Basketball**
- **Soccer**
- **Tennis**
- And more...

## 🔧 Applications

### Fitness Training
- **Form Correction**: Analyze exercise form and provide feedback
- **Repetition Counting**: Automatically count exercise repetitions
- **Workout Tracking**: Track workout sessions and progress
- **Personalized Coaching**: AI-powered coaching recommendations

### Sports Analysis
- **Performance Analysis**: Analyze athlete performance
- **Movement Pattern Recognition**: Identify movement patterns
- **Injury Prevention**: Detect potentially harmful movements
- **Training Optimization**: Optimize training routines

### Healthcare
- **Rehabilitation Monitoring**: Monitor rehabilitation exercises
- **Physical Therapy**: Assist in physical therapy sessions
- **Activity Monitoring**: Track daily physical activities

### Research & Development
- **Biomechanics Research**: Study human movement patterns
- **Sports Science**: Research in sports performance
- **Computer Vision**: Advance pose estimation techniques

## 🛠️ Technical Details

### Technologies Used

- **OpenCV**: Computer vision and image processing
- **MediaPipe**: Pose estimation and human pose detection
- **TensorFlow**: Machine learning framework
- **NumPy**: Numerical computations

### Pose Estimation

The system uses advanced pose estimation algorithms to detect:
- 33 body keypoints (MediaPipe Pose)
- Joint angles and positions
- Movement trajectories
- Activity patterns

### Performance

- **Real-time Processing**: 30+ FPS on modern hardware
- **Accuracy**: High accuracy in controlled environments
- **Latency**: Low latency for real-time applications

## 📊 Output Format

The system provides:
- Activity labels with confidence scores
- Pose keypoints visualization
- Movement analysis data
- Processed video output with annotations

## 🔬 Advanced Usage

### Custom Activity Training

To train custom activity recognition:

```python
from personal_trainer import ActivityDetector

detector = ActivityDetector()
detector.train_custom_activity(
    video_paths=['training_videos/'],
    activity_name='custom_exercise'
)
```

### Batch Processing

```python
import os
from personal_trainer import process_video

video_dir = 'videos/'
for video_file in os.listdir(video_dir):
    if video_file.endswith('.mp4'):
        process_video(os.path.join(video_dir, video_file))
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Talha Eren**

- GitHub: [@talha-eren](https://github.com/talha-eren)

## 🙏 Acknowledgments

- MediaPipe team for excellent pose estimation models
- OpenCV community for computer vision tools
- All contributors and users of this project


# 💪 Kişisel Antrenör - Yapay Zeka Destekli Spor Aktivitesi Tespit Sistemi

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Bilgisayarlı görü kullanarak yapay zeka destekli spor aktivitesi tespit sistemi. İnsan hareketlerini analiz eder ve poz tahmini ile spor aktivitelerini gerçek zamanlı olarak tanımlar.

## 📋 İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Proje Yapısı](#proje-yapısı)
- [Desteklenen Aktiviteler](#desteklenen-aktiviteler)
- [Uygulama Alanları](#uygulama-alanları)
- [Teknik Detaylar](#teknik-detaylar)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## ✨ Özellikler

- **Gerçek Zamanlı Aktivite Tanıma**: Video akışlarından gerçek zamanlı spor aktivitelerini tanımlama
- **Poz Tahmini**: Gelişmiş insan poz tespiti ve analizi
- **Hareket Analizi**: İnsan hareketlerini doğru şekilde analiz etme ve takip etme
- **Çoklu Aktivite Desteği**: Çeşitli spor ve fitness aktivitelerini tespit etme
- **Video İşleme**: Aktivite analizi için önceden kaydedilmiş videoları işleme
- **Fitness Takibi**: Egzersiz formu ve tekrar sayısını takip etme
- **Bilgisayarlı Görü**: OpenCV ve makine öğrenmesi modelleri ile geliştirilmiş

## 🚀 Kurulum

### Gereksinimler

- Python 3.8 veya üzeri
- Giriş için webcam veya video dosyası
- pip paket yöneticisi

### Adım 1: Depoyu Klonlayın

```bash
git clone https://github.com/talha-eren/Personal_Trainer.git
cd Personal_Trainer
```

### Adım 2: Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

Eğer `requirements.txt` yoksa, manuel olarak yükleyin:

```bash
pip install opencv-python numpy mediapipe tensorflow
```

### Adım 3: Kurulumu Doğrulayın

```bash
python personal_trainer.py --help
```

## 💻 Kullanım

### Temel Video Analizi

```bash
python personal_trainer.py --video video1.mp4
```

### Çoklu Video Analizi

```bash
python personal_trainer.py --video video1.mp4 video2.mp4
```

### Gerçek Zamanlı Webcam Analizi

```bash
python personal_trainer.py --webcam
```

### Özel Seçenekler

```bash
python personal_trainer.py \
    --video path/to/video.mp4 \
    --output results/ \
    --confidence 0.5 \
    --display
```

### Parametreler

- `--video`: Analiz için video dosyası yolu(ları)
- `--webcam`: Gerçek zamanlı tespit için webcam kullan
- `--output`: Analiz sonuçlarını kaydetmek için dizin
- `--confidence`: Tespit için güven eşiği (varsayılan: 0.5)
- `--display`: Sonuçları gerçek zamanlı pencerede göster

## 📁 Proje Yapısı

```
Personal_Trainer/
│
├── personal_trainer.py      # Ana uygulama scripti
├── video1.mp4                # Örnek video 1
├── video2.mp4                # Örnek video 2
├── requirements.txt          # Python bağımlılıkları (varsa)
├── README.md                 # Proje dokümantasyonu
└── .gitignore               # Git ignore dosyası
```

## 🏃 Desteklenen Aktiviteler

Sistem çeşitli spor aktivitelerini tespit edebilir ve analiz edebilir:

- **Koşu/Yürüyüş**
- **Yürüme**
- **Bisiklet**
- **Zıplama**
- **Şınav**
- **Squat**
- **Mekik**
- **Yoga Pozları**
- **Dans**
- **Basketbol**
- **Futbol**
- **Tenis**
- Ve daha fazlası...

## 🔧 Uygulama Alanları

### Fitness Eğitimi
- **Form Düzeltme**: Egzersiz formunu analiz edip geri bildirim sağlama
- **Tekrar Sayma**: Egzersiz tekrarlarını otomatik olarak sayma
- **Antrenman Takibi**: Antrenman seanslarını ve ilerlemeyi takip etme
- **Kişiselleştirilmiş Koçluk**: Yapay zeka destekli koçluk önerileri

### Spor Analizi
- **Performans Analizi**: Sporcu performansını analiz etme
- **Hareket Deseni Tanıma**: Hareket desenlerini tanımlama
- **Yaralanma Önleme**: Potansiyel olarak zararlı hareketleri tespit etme
- **Antrenman Optimizasyonu**: Antrenman rutinlerini optimize etme

### Sağlık Hizmetleri
- **Rehabilitasyon İzleme**: Rehabilitasyon egzersizlerini izleme
- **Fizik Tedavi**: Fizik tedavi seanslarında yardımcı olma
- **Aktivite İzleme**: Günlük fiziksel aktiviteleri takip etme

### Araştırma ve Geliştirme
- **Biyomekanik Araştırma**: İnsan hareket desenlerini inceleme
- **Spor Bilimi**: Spor performansı araştırmaları
- **Bilgisayarlı Görü**: Poz tahmini tekniklerini geliştirme

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler

- **OpenCV**: Bilgisayarlı görü ve görüntü işleme
- **MediaPipe**: Poz tahmini ve insan poz tespiti
- **TensorFlow**: Makine öğrenmesi çerçevesi
- **NumPy**: Sayısal hesaplamalar

### Poz Tahmini

Sistem şunları tespit etmek için gelişmiş poz tahmini algoritmaları kullanır:
- 33 vücut anahtar noktası (MediaPipe Pose)
- Eklem açıları ve pozisyonları
- Hareket yörüngeleri
- Aktivite desenleri

### Performans

- **Gerçek Zamanlı İşleme**: Modern donanımda 30+ FPS
- **Doğruluk**: Kontrollü ortamlarda yüksek doğruluk
- **Gecikme**: Gerçek zamanlı uygulamalar için düşük gecikme

## 📊 Çıktı Formatı

Sistem şunları sağlar:
- Güven skorları ile aktivite etiketleri
- Poz anahtar noktaları görselleştirmesi
- Hareket analizi verileri
- Açıklamalı işlenmiş video çıktısı

## 🔬 Gelişmiş Kullanım

### Özel Aktivite Eğitimi

Özel aktivite tanıma eğitmek için:

```python
from personal_trainer import ActivityDetector

detector = ActivityDetector()
detector.train_custom_activity(
    video_paths=['training_videos/'],
    activity_name='custom_exercise'
)
```

### Toplu İşleme

```python
import os
from personal_trainer import process_video

video_dir = 'videos/'
for video_file in os.listdir(video_dir):
    if video_file.endswith('.mp4'):
        process_video(os.path.join(video_dir, video_file))
```

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen bir Pull Request göndermekten çekinmeyin.

1. Depoyu fork edin
2. Özellik dalınızı oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dalınıza push yapın (`git push origin feature/AmazingFeature`)
5. Bir Pull Request açın

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.

## 👤 Yazar

**Talha Eren**

- GitHub: [@talha-eren](https://github.com/talha-eren)

## 🙏 Teşekkürler

- Mükemmel poz tahmini modelleri için MediaPipe ekibine
- Bilgisayarlı görü araçları için OpenCV topluluğuna
- Bu projenin tüm katkıda bulunanlarına ve kullanıcılarına





