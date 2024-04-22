## Generative AI for personalized ecommerce coaching to Amazon sellers

![Static Badge](https://img.shields.io/badge/version-1.0-green)

A platform that offers personalized ecommerce coaching to amazon sellers. Using insights of our dataset, we fine tuned GPT-3.5-Turbo to provide tailored advice on how to improve their product selling by improving their title and description for any given product.

For more information about development documentation please refer to the wiki.

![Gif of repo in action](../gif.gif)

### Dependencies
[Streamlit](https://streamlit.io/) for an easy front-end app build.

[OpenAI](https://platform.openai.com/docs/overview) for API calls to our fine-tuned model.

[IPython](https://ipython.org/) for ipynb test notebooks.

### Compile and run

```bash
# Clone repository
$ git clone https://github.com/solsylph/TheCompany.git

# Install requirements
$ pip install -r requirements.txt

# Execute local streamlit, should open default browser automatically
$ streamlit run app.py
```

### Contributors

[sarwari-mallela](https://github.com/sarwari-mallela): Obtained dataset and formatted the data into the necessary Davinci-002 'completion' format.
[cheblimarc4](https://github.com/cheblimarc4): Created the entire Streamlit frontend.
[11acc](https://github.com/11acc): Fine-tuned Davinci-002 and GPT-3.5-Turbo models. Connected the GPT-3.5-Turbo to the Streamlit frontend allowing API calls based on user input through the frontend. Assisted with the data formatting into 'chat-completion' for GPT-3.5-Turbo.
[solsylph](https://github.com/solsylph): Researched.

### License

Fork it, modify it, push it, eat it, summon a duck god with it. Whatever resonable day-to-day activity you prefer ( •ᴗ•)b
