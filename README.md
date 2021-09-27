# MLOps

```
python3 -m http.server
```

# Flask

```
python3 -m venv venv
./venv/bin/activate
pip install -r requirements.txt

docker build -t myflaskapi .
docker run -d -p 80:80 myflaskapi
```

# Streamlit

```
pip install -r requirements.txt
streamlit run app.py
```

# CDK & Lambda

```
cdk init sample-app --language python
source .venv/bin/activate
pip install -r requirements.txt
cdk deploy
```

# TensorFlow Serving

```
docker pull tensorflow/serving
docker run -it --rm -p 8501:8501 \
    -v "$(pwd)/save/fmnist:/models/fmnist" \
    -e MODEL_NAME=fmnist \
    tensorflow/serving

docker run -it --rm -p 8501:8501 \
    --mount type=bind,source="$(pwd)/save/",target="/models" \
    tensorflow/serving --model_config_file=/models/models.config

curl -d '{"instances": []}' \
    -X POST http://localhost:8501/v1/models/fmnist:predict
```
