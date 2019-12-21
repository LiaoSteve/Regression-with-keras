import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import Dense
import time
import os

os.makedirs('Data gif',exist_ok=True)
x = np.linspace(-5,5,200)
np.random.shuffle(x)
y = 0.5 * x + 2 + np.random.normal(0,0.5,[200,])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,y)
plt.ion()
plt.show()

x_train,y_train = x[:160],y[:160]
x_test,y_test = x[160:],y[160:]

model = keras.models.Sequential([
    Dense(units=1, input_dim=1)
])

model.compile(loss='mean_squared_error', optimizer='sgd')

print('\nTraining ...')
iter1 = 0
for batch in range(301):
    loss = model.train_on_batch(x_train,y_train)
    if batch % 20 == 0:
        iter1 += 1
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        y_predict = model.predict(x_train)
        lines = ax.plot(x_train,y_predict,'r') 
        plt.title('Training')       
        plt.xlabel('Loss:{}'.format(loss))      
        plt.pause(0.1)                            
        print('trainig loss: ',loss)
        plt.savefig('Data gif/'+str(iter1)+'.png')  

print('\nTesting ...')
loss = model.evaluate(x_test,y_test,batch_size=40)
print('loss: ',loss)
w,b = model.layers[0].get_weights()
print('w:{}, b:{}'.format(w[0,0],b[0]))
plt.ioff()

y_predict = model.predict(x_test)
fig = plt.figure()
ax2 = fig.add_subplot(111)
ax2.scatter(x_test,y_test)
plt.title('Testing')
ax2.plot(x_test,y_predict,'r')
plt.show()