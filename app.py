from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
      
    spark_session = SparkSession.builder.appName('winemap').getOrCreate()   
    #df = spark_session.read.format("jdbc").options(url=url,dbtable="population",driver="org.postgresql.Driver").load()
    #table = df.select('continent', 'sum(population) population').groupBy('continent').orderBy('population', ascending=False)
    continents = []#table.select('continent').collect()
    populationSum = []#table.select('population').collect()		
		
    return 'hello'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
