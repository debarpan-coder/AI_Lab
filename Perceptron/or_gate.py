def activation_fn(input_data,threshold):
    if input_data >= threshold:
        return 1
    return 0

def perceptron():
    a=[0,1,0,1] # input A
    b=[0,0,1,1] # input B
    r=[0,1,1,1] # actual output
    w = [.2,0.5] # weights
    threshold = 1 # threshold value
    learning_rate = .3 # learning rate

    # training the perceptron
    print("Perceptron training")
    i=0
    while i < len(a):
        summ = a[i]*w[0]+b[i]*w[1]
        out = activation_fn(summ,threshold)
        if out != r[i]:
            w[0] = w[0] + learning_rate*(r[i]-out)*a[i]
            w[1] = w[1] + learning_rate*(r[i]-out)*b[i]
            # restart the perceptron
            i=-1
        i+=1
    # training complete
    print("Perceptron trained")
    print(f"The Weights are : w0={w[0]} and w1={w[1]}")
    summ=int(input("Enter value of a : ")) * w[0] + int(input("Enter value of b : "))*w[1]
    return(activation_fn(summ,threshold))

print(f"The output is {perceptron()}")