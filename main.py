from bs4 import BeautifulSoup
import bd
import schedule
import requests
import time
def work():
    total_title = []
    for k in range(87):
        url = f'https://codeforces.com/problemset/page/{k}?order=BY_SOLVED_DESC'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.select_one('table[class="problems"]')
        tr = table.find_all('tr')[1:]
        for i in tr:
            title = []
            td = i.find_all('td')
            for j in td:
                span = j.find('span')
                if span:
                    span = span.text
                    title += [span]
                global_a = j.find_all('a')
                if global_a:
                    res = [v.text.rstrip().lstrip().replace('\n\n', '') for v in global_a if v.text]
                    if len(res) > 2:
                        res = [res[0], ', '.join(res[1:])]
                    title += res
            if '\n\n' in title:
                title.remove('\n\n')
            total_title.append(title)
            print(title)
        time.sleep(1)
    db_data = bd.get_data()
    if db_data:
        db_data = [x[0] for x in db_data]
    else:
        db_data = []
    result = []
    for x in total_title:
        if x[0] not in db_data:
            result.append(x)

    for x in result:
        bd.update(x)

if __name__ == '__main__':
    work()
    schedule.every().hour.do(work)
    while True:
        schedule.run_pending()
        time.sleep(1)