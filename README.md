# How to Run This App Locally (Mac OS)

1.  Clone the repository to your local machine

```shell
git clone https://github.com/mariosaputra/openai-flask.git
```

2.  Navigate to the project directory

```shell
cd openai-flask
```

3. Create a virtual environment for your project to isolate dependencies

```shell
python3 -m venv venv
```

4. Activate the virtual environment

```shell
source venv/bin/activate
```

5. Install the required Python packages for your project using pip

```shell
pip install -r requirements.txt
```

6. Start the Flask app with the following command

```shell
flask run --host=0.0.0.0 --port=5001
```

Note: We specify the host as 0.0.0.0 to allow external connections and use port 5001 to avoid conflicts with the default 5000 port used by macOS

7. Once the app is running, check the web address in your terminal

example:

```
* Running on http://192.168.1.9:5001
```

8. Test the /query endpoint using tools like Postman

request sample:

```
{
    "model": "gpt-4",
    "messages": [
      {
        "role": "system",
        "content": "You are an ai model"
      },
      {
        "role": "user",
        "content": "Hello"
      }
    ],
    "temperature": 0,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}
```

response sample

```
{
    "message": "Hello! How can I assist you today?"
}
```
