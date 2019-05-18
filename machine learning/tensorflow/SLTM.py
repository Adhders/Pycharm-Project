
import numpy as np
import tensorflow as tf
from tensorflow.contrib import rnn

learn=tf.contrib.learn
HIDDEN_SIZE=5
NUM_LAYERS=2
TIMESTEPS=10
TRAINING_STEPS=10000
BATCH_SIZE=32

TRAINING_EXAMPLES=10000
TESTING_EXAMPLES=1000
SAMPLE_GAP=0.01

def generate_data(seq):
    X=[]
    y=[]
    for i in range(len(seq)-8-1):
        X.append([seq[i:i+8]])
        y.append([seq[i+8]])
    print(np.shape(X))
    return np.array(X,dtype=np.float32),np.array(y,dtype=np.float32)


def lstm_model(X,y):
    stacked_rnn=[]
    for i in range(3):

        stacked_rnn.append(rnn.BasicLSTMCell(HIDDEN_SIZE))
    cell=rnn.MultiRNNCell(stacked_rnn)
    x_=tf.unstack(X,axis=1)

    output,_ =tf.nn.static_rnn(cell,x_,dtype=tf.float32)
    output=output[-1]
    prediction,loss=learn.models.linear_regression(output,y)

    train_op=tf.contrib.layers.optimize_loss(
        loss,tf.contrib.framework.get_global_step(),
        optimizer='Adagrad',learning_rate=0.1
    )
    return prediction,loss,train_op
regressor=learn.SKCompat(learn.Estimator(model_fn=lstm_model))
test_start=TRAINING_EXAMPLES*SAMPLE_GAP
test_end=(TRAINING_EXAMPLES+TESTING_EXAMPLES)*SAMPLE_GAP

train_X,train_y=generate_data(np.sin(np.linspace(
                                     0,test_start,TRAINING_EXAMPLES,dtype=np.float32)))
test_X,test_y=generate_data(np.sin(np.linspace(
    test_start,test_end,TESTING_EXAMPLES,dtype=np.float32
)))

regressor.fit(train_X,train_y,batch_size=BATCH_SIZE,steps=TRAINING_STEPS)
predicted=[[pred] for pred in regressor.predict(test_X)]
rmse=np.sqrt(((predicted-test_y)**2).mean(axis=0))
print( 'Mean Square Error is : %f' %rmse[0])
