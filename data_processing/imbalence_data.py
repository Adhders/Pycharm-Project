"""## First, vectorize the CSV data"""
import csv
import numpy as np

# Get the real data from https://www.kaggle.com/mlg-ulb/creditcardfraud/downloads/creditcardfraud.zip/
fname = './creditcard.csv'
all_features = []
all_targets = []
with open(fname) as f:
    for i, line in enumerate(f):
        if i == 0:
            print('HEADER:', line.strip())
            continue  # Skip header
        fields = line.strip().split(',')
        all_features.append([float(v.replace('"', '')) for v in fields[:-1]])
        all_targets.append([int(fields[-1].replace('"', ''))])
        if i == 1:
            print('EXAMPLE FEATURES:', all_features[-1])

features = np.array(all_features, dtype='float32')
targets = np.array(all_targets, dtype='uint8')
print('features.shape:', features.shape)
print('targets.shape:', targets.shape)

"""## Prepare a validation set"""
num_val_samples = int(len(features) * 0.2)
train_features = features[:-num_val_samples]
train_targets = targets[:-num_val_samples]
val_features = features[-num_val_samples:]
val_targets = targets[-num_val_samples:]

print('Number of training samples:', len(train_features))
print('Number of validation samples:', len(val_features))

"""## Analyze class imbalance in the targets"""
counts = np.bincount(train_targets[:, 0])
print('Number of positive samples in training data: {} ({:.2f}% of total)'.format(counts[1],
                                                                                  100 * float(counts[1]) / len(
                                                                                      train_targets)))

weight_for_0 = 1. / counts[0]
weight_for_1 = 1. / counts[1]

"""## Normalize the data using training set statistics"""
mean = np.mean(train_features, axis=0)
train_features -= mean
val_features -= mean
std = np.std(train_features, axis=0)
train_features /= std
val_features /= std

from tensorflow import keras

model = keras.Sequential([
    keras.layers.Dense(256, activation='relu',
                       input_shape=(train_features.shape[-1],)),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(1, activation='sigmoid'),
])
model.summary()

metrics = [keras.metrics.FalseNegatives(name='fn'),
           keras.metrics.FalsePositives(name='fp'),
           keras.metrics.TrueNegatives(name='tn'),
           keras.metrics.TruePositives(name='tp'),
           keras.metrics.Precision(name='precision'),
           keras.metrics.Recall(name='recall')]

model.compile(optimizer=keras.optimizers.Adam(1e-2),
              loss='binary_crossentropy',
              metrics=metrics)

callbacks = [keras.callbacks.ModelCheckpoint('fraud_model_at_epoch_{epoch}.h5')]
class_weight = {0: weight_for_0, 1: weight_for_1}

model.fit(train_features, train_targets,
          batch_size=2048,
          epochs=50,
          verbose=2,
          callbacks=callbacks,
          validation_data=(val_features, val_targets),
          class_weight=class_weight)
