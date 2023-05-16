#Video Streaming using a Webcam

1. Create a environment

```
    conda create -p venv python==3.7 -y
```

2. Activate environment

```
    conda activate venv/
```

3. Download the required libraries (mentioned in requirements.txt)

```
    pip install -r requirements.txt
```

4. To access webcam

```
    camera = cv2.VideoCapture(0)
```
