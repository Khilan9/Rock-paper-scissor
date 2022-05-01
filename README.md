
# Rock-paper-scissor

Created Rock Paper Scissor game using basic concepts of deep learning and Opencv.
This game is for 2 Player where both player do some gesture within particular frame and model will predict winner based on gesture.

## Installation
 
1. Install [Python 3](https://www.python.org/downloads/)

2. Install required dependenicies using below command

```bash
  pip install -r requirements.txt
```
3. Gather Training data for rock,paper and scissor

```bash
  python gathertraining.py rock
  python gathertraining.py paper
  python gathertraining.py scissor
```
4. Train the model using below command
```bash
  python train.py
```
5. Start Playing game using below command
```bash
  python rpsmain.py
```

## References

- [OpenCV](https://www.youtube.com/playlist?list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K)
- [Deep Learning With Tensorflow,Keras and Python](https://www.youtube.com/playlist?list=PLeo1K3hjS3uu7CxAacxVndI4bE_o3BDtO)




## Screenshots
