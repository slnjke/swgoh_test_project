FROM python
WORKDIR /swgoh_test_project/
COPY . .
RUN mkdir allure-results
RUN pip install -r requirements.txt
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -y google-chrome-stable
CMD ["pytest", "tests/test_search_page.py", "--alluredir=allure-results"]
