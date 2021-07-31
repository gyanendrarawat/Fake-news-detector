from flask import Flask, render_template,request
import pickle

app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

#default home page

@app.route('/')
def Home():
	return render_template('index.html')
	
#now involving ml model
@app.route('/predict',methods=['POST'])
def predict():
	st=[x for x in request.form.values()]
	type(st)
	print(st)
	temp=model[0].transform(st)
	
	output=model[1].predict(temp)
	print(output[0])

	return render_template('index.html', prediction_text='{} '.format(output[0]))
	
if __name__=="__main__":
    app.run(debug=True)
