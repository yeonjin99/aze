# aze
![HTML](https://img.shields.io/badge/html-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![css](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
-
<img width="1188" alt="aze" src="https://github.com/yeonjin99/aze/assets/98744367/def152d3-7d1d-4590-a9f1-1f6e96fa488e">

<h3>주제 선정</h3> 

요즘 TV, Youtube, SNS 등을 둘러보면 말장난 같은 농담인 ‘아재 개그’를 흔히 발견할 수 있다. 불과 몇 년 전만 해도 아재개그는 아저씨들의 썰렁한 농담에 그쳤지만 문화의 주류라고 할 수 있는 2030인 MZ세대에 의해 다시 공유되어 많은 이들에게 웃음과 탄식을 제공하고 있다.
아재개그는 단순히 유희적인 측면뿐만 아니라 자기 보호적인 측면 또한 제공하고 있다. 사회 초년생의 경우, 아재개그를 활용하여 기성세대와의 대화를 이끌어가기 위한 아이스브레이킹으로 사용할 수 있다.

이러한 점들을 미루어 보았을 때, AZE팀에서는 이용자의 니즈가 충분할 것이라고 예상하여 아재 개그를 제공하는 서비스를 구현하고자 한다. 단순히 텍스트 형식으로 제공하는 것보다 TTS (Text-to-Speech)를 이용하여 직접 읽어주는 것이 이용자로 하여금 만족과 그로 인한 지속적인 사용을 이끌어 낼 수 있다고 판단했다.

또한 ‘아재’라는 단어가 경상도, 전라도 등 지역 방언인 점과 단어의 이미지 또한 사투리를 쓰는 아저씨를 연상시키는 점을 고려하여 사투리라는 독특한 소재를 사용하기로 결정하였으며, 결론적으로 ‘사투리 아재개그 TTS’라는 주제를 선정하게 되었다.

<h3>분석 목표</h3>

<div>1) 사투리 TTS 모델 개발 </div>
<div>2) 크롤링을 통한 아재개그 데이터 수집 및 활용</div>
<div>3) 공공 OPEN API 데이터 활용</div>
<br>

<h3>모델</h3>
<div>AZE는 사투리 아재개그 TTS 서비스입니다.</div>

<h5>아재개그 TTS 모델 : Tacotron2</h5>

<div>

      tts

      └ taco
      
            └ model

                └ acoustic_지역.ckpt

            └ korean_text
      
       └ tts
 
</div>

<h3>API</h3>

**1. Dad jokes API**

**2. 카카오톡 친구에게 전송하기 API**

* python 3.10.12 version

<h3>서비스시연</h3>
https://youtu.be/KIK-9EieWc8
