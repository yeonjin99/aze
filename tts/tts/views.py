from django.shortcuts import render, redirect
import requests
import json
import random
from taco.test import aaaa



def home(request):
    return render(request, "01home.html")

def yes(request):
    return render(request, "02yes.html")

def choice(request):
    return render(request, "03ko_en.html")


def loading_ccd(request):
    global quiz, ans, num
    with open('static/text/korea_aze_gag.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    num = random.randint(0, len(data))
    full_sen = data[num]
    quiz = full_sen.split('|')[0]
    ans = full_sen.split('|')[1]

    numb = random.randint(1, 41)
    test_path = f'../static/images/aze_test{numb}.png'
    aaaa(quiz, 'ccd')
    return render(request, "loading.html", {'aze_test': test_path})

def loading_jjd(request):
    global quiz, ans, num
    with open('static/text/korea_aze_gag.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    num = random.randint(0, len(data))
    full_sen = data[num]
    quiz = full_sen.split('|')[0]
    ans = full_sen.split('|')[1]

    numb = random.randint(1, 41)
    test_path = f'../static/images/aze_test{numb}.png'
    aaaa(quiz, 'jjd')
    return render(request, "loading.html", {'aze_test': test_path})

def loading_jld(request):
    global quiz, ans, num
    with open('static/text/korea_aze_gag.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    num = random.randint(0, len(data))
    full_sen = data[num]
    quiz = full_sen.split('|')[0]
    ans = full_sen.split('|')[1]

    numb = random.randint(1, 41)
    test_path = f'../static/images/aze_test{numb}.png'
    aaaa(quiz, 'jld')
    return render(request, "loading.html", {'aze_test': test_path})

def loading_ksd(request):
    global quiz, ans, num
    with open('static/text/korea_aze_gag.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    num = random.randint(0, len(data))
    full_sen = data[num]
    quiz = full_sen.split('|')[0]
    ans = full_sen.split('|')[1]

    numb = random.randint(1, 41)
    test_path = f'../static/images/aze_test{numb}.png'
    aaaa(quiz, 'ksd')
    return render(request, "loading.html", {'aze_test': test_path})

def loading_kwd(request):
    global quiz, ans, num
    with open('static/text/korea_aze_gag.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    num = random.randint(0, len(data))
    full_sen = data[num]
    quiz = full_sen.split('|')[0]
    ans = full_sen.split('|')[1]

    numb = random.randint(1, 41)
    test_path = f'../static/images/aze_test{numb}.png'
    aaaa(quiz, 'kwd')
    return render(request, "loading.html", {'aze_test': test_path})


def koreaQ(request):
    if request.method == 'GET':
        return render(request, "04koreaQ.html", {'quiz':quiz, 'number': num})

    else:
        with open('static/text/korea_aze_gag.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()

        answer = data[num].split('|')[1]
        user_answer = request.POST['user_answer']


        if user_answer.replace('\n', '').strip() == answer.replace('\n', '').strip():
            return redirect('right_kor')
        else:
            return render(request,'06ko_worng.html', {'ans':answer})
def engQ(request):
    if request.method == "GET":
        while True:
            limit = 1
            api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
            response = requests.get(api_url, headers={'X-Api-Key': 'MyFGOiymeHcPetNyssdiNA==V4RuxyT0rsWkbrtS'})
            if "?" in response.text:
                if response.status_code == requests.codes.ok:
                    print(response.text)
                    break
                else:
                    print("Error:", response.status_code, response.text)
                    break
            else:
                continue

        CLIENT_ID, CLIENT_SECRET = 'sHC4D_AlrlogXJDwa2Qf', '5CwvelcJDZ'
        text = response.text.split(':')[1][:-2].replace('/','')
        url = 'https://openapi.naver.com/v1/papago/n2mt'
        headers = {
            'Content-Type': 'application/json',
            'X-Naver-Client-Id': CLIENT_ID,
            'X-Naver-Client-Secret': CLIENT_SECRET
        }
        data = {'source': 'en', 'target': 'ko', 'text': text}
        response = requests.post(url, json.dumps(data), headers=headers)
        kor_text = response.json()['message']['result']['translatedText']
        en_quiz = text.split('?')[0]
        en_ans = text.split('?')[1]
        ts_quiz = kor_text.split('?')[0]
        ts_ans = kor_text.split('?')[1]
        print(kor_text)

        return render(request, "04englishQ.html", {'en_quiz': en_quiz,
                                                   'ts_quiz': ts_quiz,
                                                   'en_ans':en_ans,
                                                   'ts_ans': ts_ans})

    else:
        user_answer = request.POST['user_answer']
        en_ans = request.POST['en_ans']
        ts_ans = request.POST['ts_ans']
        print(en_ans[:-2])
        print(ts_ans[:-2])

        if user_answer == en_ans:
            return redirect('right_eng')
        elif user_answer == ts_ans:
            return redirect('right_eng')
        else:
            return render(request, '06en_worng.html', {'en_ans': en_ans,
                                                       'ts_ans': ts_ans})



def right_kor(request):
    return render(request, "05ko_right.html")

def right_eng(request):
    return render(request, "05en_right.html")

def wrong_kor(request):
    return render(request, "06ko_worng.html")

def wrong_eng(request):
    return render(request, "06en_worng.html")

def data_dashboard(request):
    return render(request, "data_dashboard.html")


