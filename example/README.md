# Example Application

This is a demo application using `nemo-api` to show how Nemowallet APIv2 works. 
Instead of running it, it is recommended to read the source code to get a general idea of
how this SDK is used. However, you can modify this code directly to implement your own logic.

## Run

**READ THIS BEFORE YOU RUN ANYTHING**

**This application is shown for demo only. It will try to use your input API key and secret to
trade, lend and borrow, etc. Make sure you know exactly what it does before running it.**

```bash
# run balance demo
python app.py balance -k <YOUR_KEY_ID> -P <YOUR_PRIVATE_KEY> -p <YOUR_PUBLIC_KEY> -u <API_URL>

# run balance demo
python app.py mint -k <YOUR_KEY_ID> -P <YOUR_PRIVATE_KEY> -p <YOUR_PUBLIC_KEY> -u <API_URL>
```
