from urllib import request  # Uniform Resource Locator 웹브라우 주소

target  = request.urlopen('http://google.com')
output = target.read()
print(output)

# 크롤링 : 웹페이지를 가져 오는 행위
# 스크래핑 : 가져 온 페이지에서 데이터 추출 하는 행위